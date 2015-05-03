#lang racket

; Rewrite apply-env in figure 2.1 to give a more informative error message.

#|
(define apply-env
  (lambda (env search-var)
    (cond
      ((eqv? (car env) ’empty-env)
       (report-no-binding-found search-var))
      ((eqv? (car env) ’extend-env)
       (let ((saved-var (cadr env))
             (saved-val (caddr env))
             (saved-env (cadddr env)))
         (if (eqv? search-var saved-var)
             saved-val
             (apply-env saved-env search-var))))
      (else (report-invalid-env env)))))

(define report-no-binding-found
  (lambda (search-var)
  (eopl:error ’apply-env "No binding for ~s" search-var)))
(define report-invalid-env
  (lambda (env)
  (eopl:error ’apply-env "Bad environment: ~s" env)))

|#

(define apply-env
  (lambda (env search-var)
    (cond
      ((eqv? (car env) ’empty-env)
       (report-no-binding-found search-var))
      ((eqv? (car env) ’extend-env)
       (let ((saved-var (cadr env))
             (saved-val (caddr env))
             (saved-env (cadddr env)))
         (if (eqv? search-var saved-var)
             saved-val
             (apply-env saved-env search-var))))
      (else (report-invalid-env env)))))

(define report-no-binding-found
  (lambda (search-var env)
  (eopl:error ’apply-env "No binding for ~s on env" search-var env)))
(define report-invalid-env
  (lambda (env)
  (eopl:error ’apply-env "Bad environment: ~s" env)))