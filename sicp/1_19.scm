#lang racket
; Exercise 1.19. There is a clever algorithm for computing the Fibonacci numbers in a logarithmic number of steps
(define (fib n)
  (fib-iter 1 0 0 1 n))
(define (square n) (* n n))
(define (fib-iter a b p q count)
  (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                   (+ (square p) (square q)) ; compute p'
                   (+ (* 2 p q) (square q)) ; compute q'
                   (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
                        (+ (* b p) (* a q))
                        p
                        q
                        (- count 1)))))

; Answers:
; a = bq + aq + ap
; b = bp + aq
; so we have
; a' = bq + aq + ap
; b' = bp + aq
; a'' = b'q + a'q + a'p
; b'' = b'p + a'q
; then we extend a' and b', we got:
; a'' = (bp + aq)q + (bq + ap + aq )(p + q)
;     = bpq + aq^2 + bpq + ap^2 +apq + bq^2 + apq + aq^2
;     = 2bpq + 2apq + ap^2 + bq^2 + 2aq^2
;     = b(2pq +q^2) + a(2pq + q^2) + a(p^2 + q^2)
; so we got q' = 2pq + q^2 and p' = p^2 + q^2

; Also, if u extend the b'', you will got the same result
(fib 3)
(fib 4)
(fib 5)
(fib 6)
(fib 7)
