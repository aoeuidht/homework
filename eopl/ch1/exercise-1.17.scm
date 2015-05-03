#lang racket

#|
(down lst) wraps parentheses around each top-level element of lst.
> (down ’(1 2 3))
((1) (2) (3))
> (down ’((a) (fine) (idea)))
(((a)) ((fine)) ((idea)))
> (down ’(a (more (complicated)) object))
 ((a) ((more (complicated))) (object))
|#


#|
down: list --> list(of 1-list)
|#

(define (down lst)
  (if (null? lst)
      '()
      (cons (list (car lst))
            (down (cdr lst)))))

(display (down '(1 2 3)))
(newline)

(display (down '((a) (fine) (idea))))
(newline)

(display (down '(a (more (complicated)) object)))