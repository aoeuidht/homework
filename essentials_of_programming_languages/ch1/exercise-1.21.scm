#lang racket

#|
(product sos1 sos2) , where sos1 and sos2 are each a list of symbols without repetitions,
 returns a list of 2-lists that represents the Cartesian product of sos1 and sos2.
 The 2-lists may appear in any order.

> (product ’(a b c) ’(x y))
  ((a x) (a y) (b x) (b y) (c x) (c y))
|#


; product List X List --> List

(define (product sos1 sos2)
  (append (map (lambda (v)
                 (map (lambda (iv)
                        (cons v iv))
                      sos2))
               sos1)))

(display (product '(a b c) '(x y)))
