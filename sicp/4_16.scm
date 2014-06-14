#lang r5rs
#|
Exercise 4.16. In this exercise we implement the method just described for interpreting 
internal definitions. We assume that the evaluator supports let (see exercise 4.6).
a. Change lookup-variable-value (section 4.1.3) to signal an error if 
the value it finds is the symbol *unassigned*.
b. Write a procedure scan-out-defines that takes a procedure body and returns 
an equivalent one that has no internal definitions, by making the 
transformation described above.
c. Install scan-out-defines in the interpreter, either in
 make-procedure or in procedure- body (see section 4.1.3). 
Which place is better? Why?
|#

; a

#|
(define (lookup-variable-value var env)
  (define (env-loop env)
    (define (scan vars vals)
      (cond ((null? vars)
             (env-loop (enclosing-environment env)))
            ((eq? var (car vars))
             (car vals))
            (else (scan (cdr vars) (cdr vals)))))
    (if (eq? env the-empty-environment)
        (error "Unbound variable" var)
        (let ((frame (first-frame env)))
          (scan (frame-variables frame)
                (frame-values frame)))))
  (let ((lookup-rst (env-loop env)))
    (if (and (symbol? lookup-rst)
             (eq? lookup-rst '*unassigned*))
        (error "unassigned value")
        lookup-rst)))
|#
;b
(define (scan-out-defines exp-body)
  (let ((define-body (filter definition? exp-body))
        (value-body (filter-not definition? exp-body)))
    (let ((define-varis (map definition-variable define-body))
          (define-values (map (lambda (db) (list 'set! (definition-variable db) (definition-value db))) define-body)))
      (append (list 'let (map (lambda (v) (list v '*unassigned*)) define-varis))
              define-values
              value-body))))

; test b
; I have to write a filter and filter-not for r5rs under racket
; can't find them

(define (filter vali items)
  (if (null? items)
      '()
      (let ((rest (filter vali (cdr items))))
        (if (vali (car items))
            (cons (car items) rest)
            rest))))
(define (filter-not vali items)
  (filter (lambda (i) (not (vali i))) items))

(define (tagged-list? exp tag)
  (if (pair? exp)
      (eq? (car exp) tag)
      #f))
(define (definition? exp)
  (tagged-list? exp 'define))
(define (definition-variable exp)
  (if (symbol? (cadr exp))
      (cadr exp)
      (caadr exp)))
(define (definition-value exp)
  (if (symbol? (cadr exp))
      (caddr exp)
      (make-lambda (cdadr exp)   ; formal parameters
                   (cddr exp)))) ; body

(define (make-lambda parameters body)
  (cons 'lambda (cons parameters body)))

(define (lambda? exp) (tagged-list? exp 'lambda))
(define (lambda-parameters exp) (cadr exp))
(define (lambda-body exp) (cddr exp))
(display 
 (scan-out-defines '((define (even? n)
                       (if (= n 0)
                           true
                           (odd? (- n 1))))
                     (define (odd? n)
                       (if (= n 0)
                           false
                           (even? (- n 1))))
                     (even? (odd? 3)))))

; we got
#|
(let ((even? *unassigned*)
      (odd? *unassigned*))
  (set! even? (lambda (n)
                (if (= n 0) true (odd? (- n 1)))))
  (set! odd? (lambda (n)
               (if (= n 0) false (even? (- n 1)))))
  (even? (odd? 3)))

|#



;c `make-procedure is better, u only make it once, but get procedure body more than once.