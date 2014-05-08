#lang racket
; Exercise 2.37. Suppose we represent vectors v = (vi) as sequences of numbers, and matrices m = (mij) as
; sequences of vectors (the rows of the matrix). For example, the matrix

; is represented as the sequence ((1 2 3 4) (4 5 6 6) (6 7 8 9)). 
; With this representation, we can use sequence operations to concisely express the basic matrix and vector operations. 
; These operations (which are described in any book on matrix algebra) are the following:

; We can define the dot product as17 
;(define (dot-product v w)
;  (accumulate + 0 (map * v w)))

; Fill in the missing expressions in the following procedures for computing the other matrix operations.
; (The procedure accumulate-n is defined in exercise 2.36.)
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

(define (accumulate-n op init seqs)
  (if (null? (car seqs))
      '()
      (cons (accumulate op init
                        (map (lambda (s) (car s)) seqs))
            (accumulate-n op init (map (lambda (s) (cdr s)) seqs)))))

(define (op-combian op x y)
  (if (pair? x)
      (cons (op (car x)
                (car y))
            (op-combian op (cdr x) (cdr y)))
      '()))
                        

(define (matrix-*-vector m v)
  (map
   (lambda (m-item) (accumulate + 0 (op-combian * m-item v)))
   m))

(matrix-*-vector '((1 2 3 4) (4 5 6 6) (6 7 8 9)) '(2 0 0 0))
(matrix-*-vector '((1 2 3 4) (4 5 6 6) (6 7 8 9)) '(2 3 4 5))

; transpose
; for matrix
; 1 2 3        1 4 7
; 4 5 6  ==>   2 5 8
; 7 8 9        3 6 9
; so the first column becomes to first line
; just the accumulate-n, just do nothing to the groups

(define (transpose mat)
  (accumulate-n cons
                '()
                mat))

(transpose '((1 2 3 4) (4 5 6 6) (6 7 8 9) (10 11 12 13)))

; It's interesting, if we want to combine the first line of A and the first column of B,
; It's equal to  combine first line of A and the first line of B', which is transpose of B.

(define (matrix-*-matrix m n)
  (let ((cols (transpose n)))
    (map
     (lambda (m-line)
       (map (lambda (n-line)
              (accumulate + 0 (op-combian * m-line n-line))) n))
     m)))

(matrix-*-matrix '((1 2 3) (4 5 6) (7 8 9)) '((1 1 1) (2 2 2) (3 3 3)))