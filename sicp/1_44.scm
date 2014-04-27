#lang racket
(define (compose f g)
  (lambda (x)
    (f (g x))))

(define (repeated f n)
  (if (= 1 n)
      f
      (compose f (repeated f (- n 1)))))

(define (smooth f n dx)
  (repeated
   (lambda (x)
     (/ (+ (f x)
           (f (- x dx))
           (f (+ x dx)))
        3))
   n))