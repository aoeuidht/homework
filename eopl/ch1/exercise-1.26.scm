#lang racket
#|
(up lst) removes a pair of parentheses from each top-level element of list.
If a top-level element is not a list, it is included in the result, as is.
 The value of (up (down lst)) is equivalent to lst, but (down (up lst))
 is not necessarily lst. (See exercise 1.17.)
|#

(define (up lst)
  ;(display (list? (cdr lst)))
  (append-map (lambda (x)
                (if (list? x) x (list x))
                  )
               lst))

(display (up (list (list 1 2) (list 3 4))))
(newline)

(display (up '((x (y)) z)))