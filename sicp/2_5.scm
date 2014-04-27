#lang racket
; Exercise 2.5. Show that we can represent pairs of nonnegative integers
; using only numbers and arithmetic operations if we represent the pair a and b 
; as the integer that is the product 2a 3b. 
; Give the corresponding definitions of the procedures cons, car, and cdr.

(define (pow b e)
  (if (= e 0)
      1
      (* b (pow b (- e 1)))))
(define (cons a b)
  (* (pow 2 a)
     (pow 3 b)))

(define (remain-wrapper denom num rst)
  (if (and (= 0 (remainder denom num))
           (> denom 0))
      (remain-wrapper (/ denom num) num (+ rst 1))
      rst))
(define (car pr)
  (remain-wrapper pr 2 0))

(define (cdr pr)
  (remain-wrapper pr 3 0))

(car (cons 0 4))
(car (cons 4 0))
(cdr (cons 2 5))
  