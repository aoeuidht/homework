#lang racket

(define (i-equal? x y)
  (cond ((and (pair? x) (pair? y))
         (and (i-equal? (car x) (car y))
              (i-equal? (cdr x) (cdr y))))
        ((and (not (pair? x)) (not (pair? y)))
         (eq? x y))
        (else #f)))
(i-equal? '(this is a list) '(this is a list))
(i-equal? '(this is a list) '(this (is a) list))