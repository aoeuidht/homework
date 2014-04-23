#lang racket
; Exercise 1.33. You can obtain an even more general version of accumulate (exercise 1.32) by
; introducing the notion of a filter on the terms to be combined.
; That is, combine only those terms derived from values in the range that satisfy a specified condition.
; The resulting filtered-accumulate abstraction takes the same arguments as accumulate,
; together with an additional predicate of one argument that specifies the filter.
; Write filtered-accumulate as a procedure. Show how to express the following using filtered-accumulate:


; copy the old prime? test code here
(define (square n) (* n n))

(define (smallest-divisor n)
  (find-divisor n 2))

(define (next n)
  (if (= n 2)
      3
      (+ n 2)))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (next test-divisor)))))

(define (divides? a b)
  (= (remainder b a) 0))

(define (prime? n)
  (= n (smallest-divisor n)))

; white the accumulate with filter
(define (accumlate combiner filter null-value term a next b)
  (if (> a b)
      null-value
      (if (filter a)
          (combiner (term a)
                    (accumlate combiner filter null-value term (next a) next b))
          (accumlate combiner filter null-value term (next a) next b))
      ))

; a. the sum of the squares of the prime numbers in the interval a to b
; (assuming that you have a prime? predicate already written)
(define (pnext n) (+ n 1))

; 2^2 + 3^2 + 5^2 + 7^2
(accumlate + prime? 0 square 2 pnext 10)