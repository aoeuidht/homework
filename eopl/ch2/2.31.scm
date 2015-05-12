#lang eopl
;;; exercise 2.31

#|
Write a parser to convert a prefixlist to the abstract syntax
|#
(require eopl/tests/private/utils)

(define-datatype s-list s-list?
  (an-s-list
   (sexps (list-of s-exp?))))

(define list-of
  (lambda (pred)
    (lambda (val)
      (or (null? val)
          (and (pair? val)
               (pred (car val))
               ((list-of pred) (cdr val)))))))

(define-datatype s-exp s-exp?
  (symbol-s-exp
   (sym symbol?))
  (s-list-s-exp
   (slst s-list?)))

(define identifier?
  (lambda (id-name)
    (and (symbol? id-name)
         (not (eq? id-name 'labmda)))))

(define-datatype lc-exp lc-exp?
  (var-exp (var identifier?))
  (lambda-exp
   (bound-vars (list-of identifier?))
   (body lc-exp?))
  (app-exp
   (rator lc-exp?)
   (rands (list-of lc-exp?))))

(define report-invalid-concrete-syntax
  (lambda (datum)
        (eopl:error "invalid concrete syntax ~s" datum)))

(define-datatype prefix-exp prefix-exp?
  (const-exp
   (num integer?))
  (diff-exp
   (operand1 prefix-exp?)
   (operand2 prefix-exp?)))

(define (parse-prefix-exp-wrapper exp)
  (if (null? exp)
      '()
      (let ((ehead (car exp))
            (rleft (parse-prefix-exp-wrapper (cdr exp))))
        (if (eqv? '- ehead)
            (cons (diff-exp (car rleft)
                            (cadr rleft))
                  (cddr rleft))
            (cons (const-exp ehead) rleft)
            )
        ))
  )

(define (parse-prefix-exp exp)
  (car (parse-prefix-exp-wrapper exp)))

(display (parse-prefix-exp '(- - 3 2 - 4 - 12 7)))

