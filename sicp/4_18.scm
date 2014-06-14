#lang r5rs
#|
Exercise 4.18. Consider an alternative strategy for scanning out definitions that translates
 the example in the text to
(lambda <vars>
  (let ((u '*unassigned*)
        (v '*unassigned*))
    (let ((a <e1>)
          (b <e2>))
      (set! u a)
      (set! v b))
    <e3>))

Here a and b are meant to represent new variable names, created by the interpreter, that do 
not appear in the user's program. Consider the solve procedure from section 3.5.4:
(define (solve f y0 dt)
  (define y (integral (delay dy) y0 dt))
  (define dy (stream-map f y))
  y)
Will this procedure work if internal definitions are scanned out as shown in this exercise?
 What if they are scanned out as shown in the text? Explain.
|#

; answer
(define (scan-out-defines exp-body)
  ; make a distinct name by the variable name
  (define (variable-wrapper var)
    (string->symbol (string-append (symbol->string var) "-keyword")))
  (let ((define-body (filter definition? exp-body))
        (value-body (filter-not definition? exp-body)))
    (let ((define-varis (map definition-variable define-body))
          (define-values (map (lambda (db) (list (variable-wrapper (definition-variable db)) (definition-value db))) define-body)))
      (list 'let (map (lambda (v) (list v '*unassigned*)) define-varis)
              (list 'let define-values
                    (append (map (lambda (v) (list 'set v (variable-wrapper v))) define-varis)
                            value-body))))))

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

; 
(display 
 (scan-out-defines '((define y (integral (delay dy) y0 dt))
                      (define dy (stream-map f y))
                      y)))

#|
(let ((y *unassigned*)
      (dy *unassigned*))
  (let ((y-keyword (integral (delay dy) y0 dt))
        (dy-keyword (stream-map f y)))
    ((set y y-keyword)
     (set dy dy-keyword)
     y)))

this will not work, consiger thin line:
 (dy-keyword (stream-map f y)))

it will give unanngined error

the scan in text will generate

(let ((y *unassigned*)
      (dy *unassigned*))
  (set! y (integral (delay dy) y0 dt))
  (set! dy (stream-map f y))
  y)

this works, for delay will not evaluate the ``dy''.
|#
