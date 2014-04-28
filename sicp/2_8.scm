#lang racket
; Exercise 2.8. Using reasoning analogous to Alyssa's,
; describe how the difference of two intervals may be computed.
; Define a corresponding subtraction procedure, called sub-interval.
(define (sub-interval x y)
  (let ((xu (upper-bound x))
        (xl (lower-bound x))
        (yu (upper-bound y))
        (yl (lower-bound y)))
    (make-interval (- xl yu)
                   (- xu yl))))