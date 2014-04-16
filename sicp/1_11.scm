#lang racket
; Exercise 1.11. A function f is defined by the rule that
; f(n) = n if n<3 and 
; f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) if n> 3.
; Write a procedure that computes f by means of a recursive process.
; Write a procedure that computes f by means of an iterative process.

; Answers
; recursive version
(define (fn-recursive n)
  (if (< n 3)
      n
      (+ (fn-recursive (- n 1))
         (* 2 (fn-recursive (- n 2)))
         (* 3 (fn-recursive (- n 3))))))

; iterative version
; let's say we have a, b, c, then the next term of a, b, c will be
; c = c + 2b + 3a
; b = c
; a = b
(define (fn-iter a b c n)
  (if (> n 0)
      (fn-iter b c (+ c (* 2 b) (* 3 a)) (- n 1))
      c))
(define (fn-iterative n)
  (if (< n 3)
      n
      (fn-iter 0 1 2 (- n 2))))

; tests
(fn-recursive 0)
(fn-iterative 0)
(fn-recursive 1)
(fn-iterative 1)
(fn-recursive 2)
(fn-iterative 2)
(fn-recursive 3)
(fn-iterative 3)
(fn-recursive 4)
(fn-iterative 4)
(fn-recursive 5)
(fn-iterative 5)
(fn-recursive 10)
(fn-iterative 10)

  