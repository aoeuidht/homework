#lang racket
; Exercise 2.18. Define a procedure reverse that takes a list as argument and returns a list of the same elements in reverse order:
(define (reverse tgt)
  (define (reverse-wrapper left cadidate)
    (if (null? left)
        cadidate
        (reverse-wrapper (cdr left) (cons (car left) cadidate))))
  (reverse-wrapper tgt '()))
        
(reverse (list 1 4 9 16 25))
