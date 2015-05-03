#lang racket
#|
We can use any data structure for representing environments, 
if we can distinguish empty environments from non-empty ones, 
and in which one can extract the pieces of a non-empty environment. 
Implement environments using a representation in which the empty 
environment is represented as the empty list, 
and in which extend-env builds an environment that looks like

...

This is called an a-list or association-list representation.
|#

(define empty-env '())
(define (empty-env? env)
  (and
   (list? env)
   (null? env)))

(define (extend-env var val env)
  (cons (cons var val)
        env))

(define (apply-env env var)
  (if (empty-env? env)
      (report-no-binding-found)
      (if (eq? (car (car env)) var)
          (cdr (car env))
          (apply-env (cdr env) var)))
  )

(define report-no-binding-found
  (lambda (search-var)
    (eopl:error ’apply-env "No binding for ~s" search-var)))