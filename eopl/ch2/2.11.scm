#lang racket

; ribs implementation

(define empty-env '())
(define (empty-env? env)
  (and
   (list? env)
   (null? env)))

(define (extend-env var val env)
  (cons (cons (list var) (list val))
        env))

(define (apply-env env var)
  (if (empty-env? env)
      (report-no-binding-found)
      (let ((lookup-rst (lookup-variable-list (caar env) (cdar env) var)))
        (if (car lookup-rst)
            (cdr lookup-rst)
            (apply-env (cdr env) var))))
  )

(define (lookup-variable-list var-list val-list var)
  (if (null? var-list)
      (cons #f #f)
      (if (equal? (car var-list) var)
          (cons #t (car val-list))
          (lookup-variable-list (cdr var-list) (cdr val-list) var))))

(define report-no-binding-found
  (lambda (search-var)
    (error 'apply-env "No binding for ~s" search-var)))

(define (extend-env* var-list val-list env)
  (cons (cons var-list val-list)
        env))

