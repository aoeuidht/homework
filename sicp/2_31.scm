#lang racket
; Exercise 2.31. Abstract your answer to exercise 2.30 to produce a procedure tree-map with the property
; that square-tree could be defined as
; (define (square-tree tree) (tree-map square tree))

(define (tree-map tree oper)
  (map (lambda (sub-tree)
         (if (pair? sub-tree)
             (tree-map sub-tree oper)
             (oper sub-tree)))
       tree))

(define (square-tree tree)
  (tree-map tree (lambda (x) (* x x))))
(square-tree
 (list 1
       (list 2
             (list 3 4)
             5)
       (list 6 7)))