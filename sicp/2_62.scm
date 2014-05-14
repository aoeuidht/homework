#lang racket
; Exercise 2.62. Give a Theta(n) implementation of union-set for sets represented as ordered lists.

(define (union-set s1 s2)
  (cond ((null? s1) s2)
        ((null? s2) s1)
        (else   (let ((s1i (car s1))
                      (s2i (car s2))
                      (s1t (cdr s1))
                      (s2t (cdr s2)))
                  (cond 
                    ((= s1i s2i) (cons s1i (union-set s1t s2t)))
                    ((> s1i s2i) (cons s2i (union-set s1 s2t)))
                    (else (cons s1i (union-set s1t s2))))))))

(union-set '(1 2 3 5 6) '(5 7 8 9))