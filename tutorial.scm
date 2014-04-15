#lang racket

; this is the exercises of http://www.shido.info/lisp/scheme5_e.html
(define (incr addend)
  (+ addend 1))

; white a function to return the absolute value
(define (ab-value ipt)
  (if (> ipt 0)
      ipt
      (- ipt)))

(ab-value 10)
(ab-value -10)

; A function to return the reciprocal of a real number. Make it return #f if the argument is 0. 
(define (reci-real ipt)
  (if (= ipt 0)
      #f
      (/ 1 ipt)
  ))

(reci-real 10)
(reci-real 0.1)
(reci-real 0)
(reci-real 0.0)

; A function to convert a integer to a graphical character of ASCII characters.
; The integers that can be converted to graphical characters are 33 – 126.
; Use integer->char to convert a integer to a character.
; Make it return #f if the given integer can not be converted to a graphical character. 
(define (draw-ascii ipt)
  (if (and (< 32 ipt)
           (> 127 ipt))
      (integer->char ipt)
      #f))

(draw-ascii 31)
(draw-ascii 32)
(draw-ascii 33)
(draw-ascii 34)
(draw-ascii 124)
(draw-ascii 125)
(draw-ascii 126)
(draw-ascii 127)

; A function that takes three real numbers as arguments.
; It returns the product of these three numbers if all them is positive. 
(define (prod-positive p1 p2 p3)
  (if (and (> p1 0)
           (> p2 0)
           (> p3 0))
      (* p1 p2 p3)
      #f))

(prod-positive 0 1 2)
(prod-positive 3 1 2)
(prod-positive 3 1 -2)

; A function that takes three real numbers as arguments.
; It returns the product of these three numbers if at least one of them is negative. 
(define (prod-any-nega n1 n2 n3)
  (if (or (< n1 0)
          (< n2 0)
          (< n3 0))
      (* n1 n2 n3)
      #f))

(prod-any-nega 0 1 2)
(prod-any-nega 0 1 -2)
(prod-any-nega 3 1 2)
(prod-any-nega 3 -1 2)
(prod-any-nega 3 -1 -2)
(prod-any-nega -3 -1 -2)

; The fee of a city-run swimming pool of Foo city depends on the age of users (age): 
; 
;   free if age ≤ 3 or age ≥ 65.
;    0.5 dollars for 4 ≤ age ≤ 6.
;    1.0 dollars for 7 ≤ age ≤ 12.
;    1.5 dollars for 13 ≤ age ≤ 15.
;    1.8 dollars for 16 ≤ age ≤ 18.
;    2.0 dollars for others. 
(define (charge-pull age)
  (cond
    ((or (<= age 3)
         (>= age 65))
     0)
    ((and (>= age 4)
          (<= age 6))
     0.5)
    ((and (>= age 7)
          (<= age 12)) 1.0)
    (else 2.0)
    ))

(charge-pull 3)
(charge-pull 64)
(charge-pull 65)
(charge-pull 4)
(charge-pull 6)
(charge-pull 7)
          