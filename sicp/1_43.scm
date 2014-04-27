#lang racket
; Write a procedure that takes as inputs a procedure that computes f and a
; positive integer n and returns the procedure that computes the nth repeated application of f.
; Your procedure should be able to be used as follows:
;((repeated square 2) 5)

(define (square x) (* x x))
(define (compose f g)
  (lambda (x)
    (f (g x))))

(define (repeated f n)
  (if (= 1 n)
      f
      (compose f (repeated f (- n 1)))))

((repeated square 3) 5)

