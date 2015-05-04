#lang racket

; implement the empty-env?

(define apply-env
  (lambda (env search-var)
    ((car env) search-var)))


(define extend-env
  (lambda (saved-var saved-val saved-env)
    (list
     (lambda (search-var)
       (if (eqv? search-var saved-var)
           saved-val
           (apply-env saved-env search-var)))
     (lambda ()
       #f))))

(define empty-env
  (lambda ()
    (list
     (lambda (search-var)
       (report-no-binding-found search-var))
     (lambda ()
       #t))))

(define (empty-env? env)
  ((cadr env)))
  

(define report-no-binding-found
  (lambda (search-var)
  (error 'apply-env "No binding for ~a" search-var)))


(let ((env (extend-env 'symbol "value" (empty-env))))
  (display (empty-env? env))
  (display (apply-env env
           'symbol))
  (display (apply-env env 'symbol-not-exists)))
