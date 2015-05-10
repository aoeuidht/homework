#lang eopl
;;; exercise 2.21

#|
Implement the data type of environments, as in section 2.2.2,
 using define-datatype. Then include has-binding? of exercise 2.9.
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

(define-datatype env-exp env-exp?
  (empty-env-exp)
  (non-empty-env-exp
   (identifier symbol?)
   (value s-exp?)
   (old-env env-exp?)))

(define (has-binding? search-var search-env)
  (cases env-exp search-env
         (non-empty-env-exp
          (identifier value old-env)
          (or (eq?
               (cases s-exp value
                      (symbol-s-exp (sym) sym)
                      (s-list-s-exp (slst) slst))
               search-var)
              (has-binding? search-var old-env)))
         (else #f)))

(display (has-binding? 'a (non-empty-env-exp 'b (symbol-s-exp 'a) (empty-env-exp))))
