#lang racket
#|
(exists? pred lst) returns #t if any element of lst satisfies pred, and returns #f otherwise.
|#

; exists? lambda X List --> Bool

(define (exists? pred lst)
  (if (null? lst)
      #f
      (if (pred (car lst))
          #t
          (exists? pred (cdr lst)))))

(exists? number? '(a b c d))
(exists? number? '(a b c d 1))