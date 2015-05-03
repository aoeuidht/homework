#lang racket

#|
(flatten slist)  returns a list of the symbols contained in slist in the order
 in which they occur when slist is printed. Intuitively,
 flatten removes all the inner parentheses from its argument.

|#


; flatten: List --> List

(define (flatten slist)
  (if (symbol? slist)
      (list slist)
      (if (null? slist)
          '()
          (append-map flatten slist))))

(display (flatten '(a b c)))
(newline)

(display (flatten '((a) () (b ()) () (c))))
(newline)

(display (flatten '((a b) c (((d)) e))))
(newline)