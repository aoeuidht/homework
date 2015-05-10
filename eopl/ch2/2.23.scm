#lang eopl
;;; exercise 2.23

#|
The definition of lc-exp ignores the condition in definition 1.1.8
 that says “Identifier is any symbol other than lambda.”
 Modify the definition of identifier? to capture this condition.
 As a hint, remember that any predicate can be used in define-datatype, even ones you define.
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
   (bound-var identifier?)
   (body lc-exp?))
  (app-exp
   (rator lc-exp?)
   (rand lc-exp?)))

(define occurs-free?
  (lambda (search-var exp)
    (cases lc-exp exp
           (var-exp (var) (eqv? var search-var))
           (lambda-exp (bound-var body)
                       (and
                        (not (eqv? search-var bound-var))
                        (occurs-free? search-var body)))
           (app-exp (rator rand)
                    (or
                     (occurs-free? search-var rator)
                     (occurs-free? search-var rand))))))

;; test items
(check-equal? (occurs-free? 'x (var-exp 'x)) #t)

(check-equal? (occurs-free? 'x (var-exp 'y)) #f)

(check-equal? (occurs-free?
               'x
               (lambda-exp 'x
                           (app-exp (var-exp 'x) (var-exp 'y))))
              #f)
