#lang racket
; Exercise 2.7. Alyssa's program is incomplete because she has not specified the implementation of the
; interval abstraction. Here is a definition of the interval constructor:
(define (make-interval a b) (cons a b))
;Define selectors upper-bound and lower-bound to complete the implementation.

; Answer
(define (upper-bound r)
  (cdr r))
(define (lower-bound r)
  (car r))
  