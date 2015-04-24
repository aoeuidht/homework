#lang racket
#|
(list-set lst n x)
returns a list like lst, except that the n-th element, using zero-based indexing, is x.
> (list-set ’(a b c d) 2 ’(1 2))
(a b (1 2) d)
> (list-ref (list-set ’(a b c d) 3 ’(1 5 10)) 3)
 (1 5 10)
|#

#|
list-set: List X Int X S-exp  --> List
|#

(define (list-set lst n x)
  (if (null? lst)
      '()
      (cons (if (= n 0)
                x
                (car lst))
            (list-set (cdr lst)
                      (- n 1)
                      x))))

(display (list-set '(a b c d) 2 '(1 2)))
(newline)

(display (list-ref (list-set '(a b c d) 3 '(1 5 10)) 3))