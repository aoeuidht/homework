#lang racket

; Exercise 1.3. Define a procedure that 
; takes three numbers as arguments and 
; returns the sum of the squares of the two larger numbers.
(define (squ-num n)
  (* n n))
(define (sum-squ n1 n2)
  (+ (squ-num n1)
     (squ-num n2)))

(define (sum-squ-2 n1 n2 n3)
  (if (> n1 n2)
      (if (> n2 n3)
          (sum-squ n1 n2)
          (sum-squ n1 n3))
      (if (> n1 n3)
          (sum-squ n1 n2)
          (sum-squ n2 n3))))

; here are the tests
(sum-squ-2 1 2 3)
(sum-squ-2 1 3 2)
(sum-squ-2 2 1 3)
(sum-squ-2 2 3 1)
(sum-squ-2 3 1 2)
(sum-squ-2 3 2 1)
