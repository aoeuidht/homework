#lang racket

; Exercise 1.38. In 1737, the Swiss mathematician Leonhard Euler published a memoir De Fractionibus Continuis,
; which included a continued fraction expansion for e - 2,
; where e is the base of the natural logarithms. In this fraction, the Ni are all 1, and the Di are
; successively 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ....
; Write a program that uses your cont-frac procedure from exercise 1.37 to approximate e, based on Euler's expansion.

; Answers:
; the di list is 
; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8
; we add a `1` to the di line and  new line under it, here we go:
; 1, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8
; 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12
; so the rule is
; D_i = (i+1) * 2/3  ----> ((i+1) % 3) == 0
;       1            ----> others
; so we have the new term-d
(define (term-d-e i)
  (if (= 0 (remainder (+ i 1) 3))
      (* 2 (/ (+ i 1) 3))
      1))

; with the cont-frac method
(define (cont-frac-iter term-n term-d k)
  (define (cont-frac-iter-wrap term-n term-d k rst)
    (if (> k 0)
        (cont-frac-iter-wrap term-n
                             term-d
                             (- k 1)
                             (/ (term-n k)
                                (+ (term-d k) rst)))
                             rst))
  (cont-frac-iter-wrap term-n term-d k 0))

; here we cale the e
(define (cont-frac-e k)
  (+ 2 (cont-frac-iter (lambda (i) 1.0)
                        term-d-e
                        k)))

(cont-frac-e 10)