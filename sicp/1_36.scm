#lang racket
(define tolerance 0.00001)
(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))

(define (calc-x-xth-power-equal n)
  (fixed-point (lambda (x) (/ (log n) (log x))) 2))
(calc-x-xth-power-equal 10000)