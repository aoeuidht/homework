#lang racket
; white the method of the k-term finite continued fraction

; here comes the recursive version
(define (cont-frac term-n term-d k)
  (define (cont-frac-wrap n)
    (/ (term-n n)
       (if (>= n k)
           (term-n k)
           (+ (term-n k)
              (cont-frac-wrap (+ n 1))))))
  (cont-frac-wrap 1))


; the iterative version
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

(cont-frac (lambda (i) 1.0)
           (lambda (i) 1.0)
           10)

(cont-frac-iter (lambda (i) 1.0)
                (lambda (i) 1.0)
                10)
        