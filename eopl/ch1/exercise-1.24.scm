#lang racket

#|
(every? pred lst) returns #f if any element of lst
 fails to satisfy pred, and returns #t otherwise.
|#

; every?: lambda X List --> BOOL

(define (every? pred lst)
  (if (null? lst)
      #t
      (if (pred (car lst))
          (every? pred (cdr lst))
          #f
          )))

(display (every? number? '(a b 3)))
(newline)

(display (every? number? '(1 2 3 4 5)))