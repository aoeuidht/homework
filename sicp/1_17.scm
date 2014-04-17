#lang racket
; Exercise 1.17. The exponentiation algorithms in this section are
; based on performing exponentiation by means of repeated multiplication.
; In a similar way, one can perform integer multiplication by means of repeated addition.
; The following multiplication procedure (in which it is assumed that our language can only add,
; not multiply) is analogous to the expt procedure:
;(define (* a b)
;  (if (= b 0)
;      0
;      (+ a (* a (- b 1)))))
; This algorithm takes a number of steps that is linear in b.
; Now suppose we include, together with addition, operations double, which doubles an integer,
; and halve, which divides an (even) integer by 2.
; Using these, design a multiplication procedure analogous to fast-expt that uses a logarithmic number of steps.
(define (even? n) (= (remainder n 2) 0))
(define (double n) (arithmetic-shift n 1))
(define (halve n) (arithmetic-shift n -1))
(define (fast-mul-iter product a b)
  (if (= b 0)
      product
      (if (even? b)
          (fast-mul-iter product (double a) (halve b))
          (fast-mul-iter (+ product a) a (- b 1)))))

(define (fast-mul a b)
  (fast-mul-iter 0 a b))

(fast-mul 4 5)