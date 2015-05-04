#lang racket

; implement the has-binding

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
     (lambda () #f)
     (lambda (search-val)
       (if (eqv? search-val saved-val)
           #t
           (has-binding? saved-env search-val))))))

(define empty-env
  (lambda ()
    (list
     (lambda (search-var)
       (report-no-binding-found 'apply-val search-var))
     (lambda () #t)
     (lambda (search-val) #f)
     )))
  
(define (empty-env? env)
  ((cadr env)))

(define (has-binding? env val)
  ((caddr env) val)
  )



(define report-no-binding-found
  (lambda (search-type search-var)
  (error search-type "No binding for ~a" search-var)))
  

(let ((env (extend-env 'symbol "value" (empty-env))))
  (display (empty-env? env))
  (display (apply-env env
           'symbol))
  (display (has-binding? env "value"))
  (display (has-binding? env "value-not-binded"))
  (display (apply-env env 'symbol-not-exists)))
