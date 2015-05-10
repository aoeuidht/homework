#lang eopl
;;; exercise 2.28

#|
Write an unparser that converts the abstract syntax of an lc-exp into a string that matches the second grammar in this section (page 52).
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

(define-datatype lc-exp lc-exp?
  (var-exp (var identifier?))
  (lambda-exp
   (bound-var identifier?)
   (body lc-exp?))
  (app-exp
   (rator lc-exp?)
      (rand lc-exp?)))

(define identifier?
  (lambda (id-name)
    (and (symbol? id-name)
         (not (eq? id-name 'labmda)))))

(define (unparse-lc-exp exp)
  (cases lc-exp exp
         (var-exp (var) (symbol->string var))
         (lambda-exp (bound-var body)
                     (string-append
                      "proc "
                      (symbol->string bound-var)
                      " => \n"
                      (unparse-lc-exp body)))
         (app-exp (rator rand)
                  (string-append
                   (unparse-lc-exp rator)
                   " ("
                   (unparse-lc-exp rand)
                   ")\n"))))


(display (unparse-lc-exp (var-exp 'x)))

(display (unparse-lc-exp
          (lambda-exp
           'x
           (app-exp (var-exp 'x) (var-exp 'y)))))
