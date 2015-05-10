#lang eopl
;;; exercise 2.29

#|
Where a Kleene star or plus (page 7) is used in concrete syntax,
it is most convenient to use a list of associated subtrees when
constructing an abstract syntax tree. For example, if the grammar
for lambda-calculus expressions had been
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
        (lambda-exp
         (cadr datum)
         (parse-expression (caddr datum)))
        (app-exp (parse-expression (car datum))
                 (map parse-expression (cadr datum))
         )
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
