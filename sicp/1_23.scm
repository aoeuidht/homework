#lang racket


(define (square n) (* n n))

(define (smallest-divisor n)
  (find-divisor n 2))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))

(define (divides? a b)
  (= (remainder b a) 0))

(define (prime? n)
  (= n (smallest-divisor n)))

(define (timed-prime-test n)
  (start-prime-test n (current-inexact-milliseconds)))
(define (start-prime-test n start-time)
  (if (prime? n)
      (begin (newline)
       (display n)
       (report-prime (- (current-inexact-milliseconds) start-time)))
      #f))
(define (report-prime elapsed-time)
  (display " *** ")
  (display elapsed-time)
  #t)

; Use your procedure to find the three smallest primes larger than 1000; larger than 10,000; larger than 100,000; larger than 1,000,000

(define (get-latest-primes-bigger-than than-what pri-num)
  (when (> pri-num 0)
      (if (timed-prime-test than-what)
          (get-latest-primes-bigger-than (+ than-what 1) (- pri-num 1))
          (get-latest-primes-bigger-than (+ than-what 1) pri-num))))
(get-latest-primes-bigger-than 1000 3)
(get-latest-primes-bigger-than 10000 3)
(get-latest-primes-bigger-than 100000 3)
      
    
      

