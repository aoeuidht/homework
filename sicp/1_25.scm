#lang racket

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))

;(define (expmod base exp m)
;  (remainder (fast-expt base exp) m))
; the new expmod doesn't do the same job
; for it will have to calc the real base^exp,
; which will cause overflow