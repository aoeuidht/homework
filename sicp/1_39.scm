#lang racket
; use continue fraction to calc the tan

; with the cont-frac method
(define (cont-frac-iter term-n term-d k)
  (define (cont-frac-iter-wrap term-n term-d k rst)
    (if (> k 0)
        (cont-frac-iter-wrap term-n
                             term-d
                             (- k 1)
                             (/ (term-n k)
                                (+ (term-d k) rst)))
                             rst))
  (cont-frac-iter-wrap term-n term-d k 0))

; N rule:
; N_i = x     ----> i = 1
;       x^2   ----> else
; D rule:
; D_i = 2x-1
; so here we go
(define (gen-term-n-tan x)
  (lambda (i)
    (if (= i 1)
           x
           (- (* x x)))))

(define (tan-cf x k)
  (cont-frac-iter
   (gen-term-n-tan x)
   (lambda (i) (- (* 2 i) 1))
   k))

(tan-cf 1.5 100)
