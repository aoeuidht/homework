#lang racket
; Exercise 2.1. Define a better version of make-rat that handles both positive and negative arguments.
; Make-rat should normalize the sign so that if the rational number is positive,
; both the numerator and denominator are positive, and if the rational number is negative, only the numerator is negative.

(define (gcd a b)
  (if (= b 0)
      a
      (gcd b (remainder a b))))

(define (numer x) (car x))
(define (denom x) (cdr x))
(define (print-rat x)
  (newline)
  (display (numer x))
  (display "/")
  (display (denom x)))

(define (make-rat n d)
  (let ((g (gcd (abs n) (abs d)))
        (pos (eqv? (= n (abs n))
                   (= d (abs d)))))
    (cons ((if pos + -)
           (/ (abs n) g))
          (/ (abs d) g))))

(print-rat (make-rat 1 2))
(print-rat (make-rat 2 4))
(print-rat (make-rat -2 6))
(print-rat (make-rat 2 -6))
(print-rat (make-rat 3 9))
              