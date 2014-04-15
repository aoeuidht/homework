#lang racket
; Exercise 1.8. Newton's method for cube roots is based on the fact that if y is an approximation to the cube root of x,

(define (square n) (* n n))
(define (cube n) (* n n n))

(define (average x y) (/ (+ x y) 2))

; here we add a param named `old-guess' torecord the old guess
(define (cube-iter guess old-guess x)
  (if (good-enough? guess old-guess)
      guess
      (cube-iter (improve guess x) guess
                 x)))

(define (improve guess x)
  (/ (+ (/ x (square guess)) (* 2 guess)) 3))

; we old-guess and current-guess are nearby, done!
(define (good-enough? guess old-guess)
  (< (abs (- guess old-guess)) 0.001))

(define (cube-root x)
  (cube-iter 1.0 x x))

; tests
(cube-root 10)
(cube (cube-root 10))