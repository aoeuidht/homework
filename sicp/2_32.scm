#lang racket
; Exercise 2.32. We can represent a set as a list of distinct elements, and we can represent the set of
; all subsets of the set as a list of lists. For example, if the set is (1 2 3),
; then the set of all subsets is (() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3)).
; Complete the following definition of a procedure that generates the set of subsets
; of a set and give a clear explanation of why it works:
(define (subsets s)
  (if (null? s)
      (list '())
      (let ((rest (subsets (cdr s))))
        (append rest (map (lambda (rest-item) (cons (car s) rest-item))
                          rest)))))
(subsets '(1 2 3))