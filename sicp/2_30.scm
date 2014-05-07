#lang racket
; Exercise 2.30. Define a procedure square-tree analogous to the square-list procedure of
; exercise 2.21. That is, square-list should behave as follows:

;(1 (4 (9 16) 25) (36 49))

(define (square x) (* x x))

(define (square-tree tree)
  (map (lambda (sub-tree)
         (if (pair? sub-tree)
             (square-tree sub-tree)
             (square sub-tree)))
       tree))
  
(square-tree
 (list 1
       (list 2
             (list 3 4)
             5)
       (list 6 7)))