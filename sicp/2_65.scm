#lang racket
; Exercise 2.65. Use the results of exercises 2.63 and 2.64 to give theta (n) 
; implementations of union-set and intersection-set for sets implemented as (balanced) binary trees.41

; Answer
; Since we have theta n tree to list ande theat n list to tree, just
; (list->tree (union-set (tree->list set) (tree->list set)))

(define (wrapper-set op)
  (lambda (s1 s2)
    (list->tree (op (tree->list-2 s1)
                    (tree->list-2 s2)))))
  
(define (union-set s1 s2)
  ((wrapper-set union-set-list) s1 s2))

(define (intersection-set s1 s2)
  ((wrapper-set intersection-set-list) s1 s2))