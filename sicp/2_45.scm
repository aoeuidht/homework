#lang racket
; Exercise 2.45. Right-split and up-split can be expressed as instances of a general splitting operation.
; Define a procedure split with the property that evaluating
; (define right-split (split beside below))
; (define up-split (split below beside))
; produces procedures right-split and up-split with the same behaviors as the ones already defined.

(define (split big-small small-small)
  (define (split-wrapper painter n)
    (if (= n 0)
        painter
        (let ((small-img (split-wrapper painter (- n 1))))
          (big-small painter
                     (small-small small-img smal-img)))))
  split-wrapper)

