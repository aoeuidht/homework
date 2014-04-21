#lang racket

; Exercise 1.29. Simpson's Rule is a more accurate method of numerical integration than the method
; illustrated above. Using Simpson's Rule, the integral of a function f between a and b is approximated as
; ...

; Define a procedure that takes as arguments f, a, b, and n and
; returns the value of the integral, computed using Simpson's Rule.
; Use your procedure to integrate cube between 0 and 1 (with n = 100 and n = 1000),
; and compare the results to those of the integral procedure shown above.

; the original sum method

(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))

(define (integral f a b dx)
  (define (add-dx x) (+ x dx))
  (* (sum f (+ a (/ dx 2.0)) add-dx b)
     dx))

(define (cube x) (* x x x))

(integral cube 0 1 0.01)
(integral cube 0 1 0.001)

; the simpson-rule
(define (even? n)
  (= (remainder n 2) 0))

(define (simpson-integral f a b dx)
  (define (add-dx x) (+ x (* 2 dx)))
  (define (term-simp x)
      (+ (f x)
       (* 4 (f (+ x dx)))
       (f (+ x (* 2 dx))))
    )
  (* (/ dx 3) (sum term-simp a add-dx b)))

(define (simp-wrapper f a b n)
  (if (or #t (even? n))
      (simpson-integral cube a b (/ (* 1.0 (- b a)) n))
      (display #'n-isnt-even)))

(simp-wrapper cube 0 1 100)
(simp-wrapper cube 0 1 1000)
    


