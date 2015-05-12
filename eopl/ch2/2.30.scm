#lang eopl
;;; exercise 2.30

#|
The procedure parse-expression as defined above is fragile:
 it does not detect several possible syntactic errors,
such as (a b c), and aborts with inappropriate error messages for other
 expressions, such as (lambda). 

Modify it so that it is robust, accepting any s-exp and issuing
 an appropriate error message if the s-exp does
 not represent a lambda-calculus expression.
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

(define (parse-expression datum)
  (cond
   [(symbol? datum) (var-exp datum)]
   [(pair? datum)
    (if (eqv? (car datum) 'lambda)
                                        ; do lambda check 1st
        (if (and (pair? (cdr datum))
                 (list? (cadr datum))
                 (pair? (cddr datum))
                 (null? (cdddr datum)))
            (lambda-exp
             (cadr datum)
             (parse-expression (caddr datum)))
            (report-invalid-concrete-syntax datum))

                                        ; do app-exp check here
        (if (and (pair? (cdr datum))
                 (null? (cddr datum)))
            (app-exp (parse-expression (car datum))
                     (map parse-expression (cadr datum))
                     )
            (report-invalid-concrete-syntax datum))
        )]
   [else (report-invalid-concrete-syntax 'invalid-syntax)]))

(display (parse-expression 'x))
(newline)
(display (parse-expression '(x (y))))
(newline)
(display (parse-expression '(lambda (x) y)))
(newline)
(display (parse-expression '(lambda () y)))
(newline)
(display (parse-expression '(a b c)))
(newline)
