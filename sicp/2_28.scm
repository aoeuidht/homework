#lang racket
; Exercise 2.28. Write a procedure fringe that takes as argument a tree (represented as a list) and returns a
; list whose elements are all the leaves of the tree arranged in left-to-right order. For example,
(define x (list (list 1 2) (list 3 4)))
;(fringe x)
;(1 2 3 4)
;(fringe (list x x))
;(1 2 3 4 1 2 3 4)

; Answer:
; Apparently, this is a deep-first tree search program
(define (fringe tgt)
  (if (pair? tgt)
      (let ((ta (car tgt))
            (td (cdr tgt)))
        (fringe ta)
        (fringe td))
      (cond ((not (null? tgt)) 
             (display tgt))
  )))

(fringe (list x x x))