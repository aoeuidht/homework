#lang racket
#|
(list-index pred lst) returns the 0-based position of the first element of
 lst that satisfies the predicate pred. If no element of lst
 satisfies the predicate, then list-index returns #f.

> (list-index number? ’(a 2 (1 3) b 7))
 1
> (list-index symbol? ’(a (b c) 17 foo))
 0
> (list-index symbol? ’(1 2 (a b) 3))
 #f
|#

; list-index: lambda X List -> Int | Bool
(define (list-index pred lst)
  (list-index-wrapper pred lst 0))

; list-index-wrapper: lambda X List X Int --> Int | Bool
(define (list-index-wrapper pred lst n)
  (if (null?  lst)
      #f
      (if (pred (car lst))
          n
          (list-index-wrapper pred (cdr lst) (+ n 1)))))

(display  (list-index number? '(a 2 (1 3) b 7)))
(newline)

(display (list-index symbol? '(a (b c) 17 foo)))
(newline)

(display (list-index symbol? '(1 2 (a b) 3)))

