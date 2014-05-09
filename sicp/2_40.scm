#lang racket
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

(define (flatmap proc seq)
  (accumulate append '() (map proc seq)))

; Exercise 2.40. Define a procedure unique-pairs that, given an integer n, 
; generates the sequence of pairs (i,j) with 1< j< i< n. 
; Use unique-pairs to simplify the definition of prime-sum-pairs given above.

(define (unique-pairs n)
  (flatmap (lambda (j) 
             (map (lambda (i) (cons i j))
                  (range 1 j)))
           (range 2 n)))
(unique-pairs 5)
(unique-pairs 4)
