#lang racket
; Exercise 2.39. Complete the following definitions of reverse (exercise 2.18) in terms of fold-right and fold-left from exercise 2.38:

; Apparently, the `reduce` method in python use the fold-left
(define (fold-left op initial sequence)
  (define (iter result rest)
    (if (null? rest)
        result
        (iter (op result (car rest))
              (cdr rest))))
  (iter initial sequence))

(define (fold-right op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (fold-right op initial (cdr sequence)))))

(define (reverse-right sequence)
  (fold-right (lambda (x y) (append y (list x))) '() sequence))
(define (reverse-left sequence)
  (fold-left (lambda (x y) (cons y x)) '() sequence))

(reverse-right '(1 2 3 4 5 6))
(reverse-left '(1 2 3 4 5 6))