#lang racket
; Exercise 2.17. Define a procedure last-pair that returns the list that contains only the last element of a given (nonempty) list:
(define (last-pair tgt)
  (if (null? (cdr tgt))
      tgt
      (last-pair (cdr tgt))))
             
(last-pair (list 23 72 149 34))