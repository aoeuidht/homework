#lang racket

; apply extend-nev*


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

(define (extend-env* var-list val-list env)
  (if (null? var-list)
      env
      (extend-env* (cdr var-list) (cdr val-list)
                   (extend-env (car var-list) (car val-list)
                               env))))