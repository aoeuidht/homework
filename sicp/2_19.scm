#lang racket
; counting changes
; The number of ways to change amount a using n kinds of coins equals
; the number of ways to change amount a using all but the first kind of coin, plus
; the number of ways to change amount a - d using all n kinds of coins, where d is the denomination of the first kind of coin. 

(define (cc amount coin-values)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (no-more? coin-values)) 0)
        (else
         (+ (cc amount
                (except-first-denomination coin-values))
            (cc (- amount
                   (first-denomination coin-values))
                coin-values)))))

; Define the procedures first-denomination, except-first-denomination, and no-more? 
; in terms of primitive operations on list structures.
(define (first-denomination cvs)
  (car cvs))

(define (except-first-denomination cvs)
  (cdr cvs))

(define no-more? null?)

(define us-coins (list 50 25 10 5 1))
(define uk-coins (list 100 50 20 10 5 2 1 0.5))
(cc 100 us-coins)
; this is too slow (cc 100 uk-coins)

; Does the order of the list coin-values affect the answer produced by cc? Why or why not?
; Of course not. Check the subsection 1.2.2, the tree recursion.
; swap any 2 coins order, will just influence the travel order of the huge process tree,
; buy still, any branch will be travelled


