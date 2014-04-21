#lang racket
; Exercise 1.30. The sum procedure above generates a linear recursion.
; The procedure can be rewritten so that the sum is performed iteratively.
; Show how to do this by filling in the missing expressions in the following definition:

(define (sum term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (+ result (term a)))))
  (iter a 0))

; now the tests
; use sigma-cube for testing

(define (integral f a b dx)
  (define (add-dx x) (+ x dx))
  (* (sum f (+ a (/ dx 2.0)) add-dx b)
     dx))

(define (cube x) (* x x x))

(integral cube 0 1 0.01)
(integral cube 0 1 0.001)