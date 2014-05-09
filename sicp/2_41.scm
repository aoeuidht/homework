#lang racket
; Exercise 2.41. Write a procedure to find all ordered triples of distinct
; positive integers i, j, and k less than or equal to a given integer n that sum to a given integer s.

; Answer: this is an easy one. Just use the result of 2.40 -- generate all the ordered pairs lower than n/2, and calc the
; thired number in the turple

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

(define (sum-equal n)
  (let ((pairs (unique-pairs (/ n 2))))
    (filter (lambda (r) (> (caddr r) (cadr r)))
     (map (lambda (p) (list (car p)
                            (cdr p)
                            (- n (car p) (cdr p))))
          pairs))))

(sum-equal 5)
(sum-equal 6)
(sum-equal 7)
(sum-equal 8)
