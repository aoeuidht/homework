#lang racket
; Exercise 2.28. Write a procedure fringe that takes as argument a tree (represented as a list) 
; and returns a list whose elements are all the leaves of the tree arranged in left-to-right order. For example,
; (define x (list (list 1 2) (list 3 4)))
; (fringe x)
; (1 2 3 4)
; (fringe (list x x))
; (1 2 3 4 1 2 3 4)

; Answer
; Apparently, this is a depth-first tree travel

(define (fringe tree)
  (if (pair? tree)
      (let ((l (car tree))
            (r (cdr tree)))
        (append (fringe l)
                (fringe r)))
      (if (null? tree)
          '()
          (list tree))
      ))
(define x (list (list 1 2) (list 3 4)))
(fringe x)
(fringe (list x x))
  