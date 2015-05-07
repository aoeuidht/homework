#lang racket

#|
Implement the lambda-calculus expression interface for the representation specified by the grammar above.
|#

(define (var-exp var)
  var)

(define (lambda-exp var body)
  (list 'lambda (list var) body))

(define (app-exp rator rand)
  (list rator rand))

(define (var-exp? lc-exp)
  (not (list? lc-exp)))

(define (lambda-exp? lc-exp)
  #|
  (display lc-exp)
  (newline)
  (display
   (and (list? lc-exp)
        (not (null? lc-exp))
        (eq? 'lambda (car lc-exp))))
  (newline)
  |#
  (and (list? lc-exp)
       (not (null? lc-exp))
       (eq? 'lambda (car lc-exp)))
  )

(define (app-exp? lc-exp)
  (and (list? lc-exp)
       (not (null? lc-exp))
       (not (eq? 'lambda (car lc-exp)))))

(define (var-exp->var lc-exp) lc-exp)
(define (lambda-exp->bound-var lc-exp) (caadr lc-exp))
(define (lambda-exp->body lc-exp) (caddr lc-exp))
(define (app-exp->rator lc-exp) (car lc-exp))
(define (app-exp->rand lc-exp) (cadr lc-exp))


; here is the test

(define occurs-free?
  (lambda (search-var exp)
    (cond
      ((var-exp? exp) (eqv? search-var (var-exp->var exp)))
      ((lambda-exp? exp)
       (and
        (not (eqv? search-var (lambda-exp->bound-var exp)))
        (occurs-free? search-var (lambda-exp->body exp))))
      (else (or (occurs-free? search-var (app-exp->rator exp))
                (occurs-free? search-var (app-exp->rand exp)))))))

(occurs-free? 'x 'x)
(occurs-free? 'x 'y)
(occurs-free? 'x '(lambda (x) (x y)))
(occurs-free? 'x '(lambda (y) (x y)))
(occurs-free? 'x '((lambda (x) x) (x y)))
(occurs-free? 'x '(lambda (y) (lambda (z) (x (y z)))))
