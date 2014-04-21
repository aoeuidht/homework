#lang racket
; The sum procedure is only the simplest of a vast number of similar abstractions
; that can be captured as higher-order procedures.
; Write an analogous procedure called product that returns the product of the values
; of a function at points over a given range. Show how to define factorial in terms of product.
; Also use product to compute approximations to using the formula

(define (product term a next b)
  (if (> a b)
      1
      (* (term a)
         (product term (next a) next b))))

; tests
(define (identity x) x)
(define (next-yita x) (+ x 1))

(product identity 1 next-yita 5)

; the iterative version

(define (product-iter term a next b)
  (define (iter-prod a prod)
    (if (> a b)
        prod
        (iter-prod (next a) (* prod (term a)))))
  (iter-prod a 1))

(product-iter identity 1 next-yita 5)

; now we calc pi
(define (square x) (* x x))
(define (pi-next x)
  (+ x 2))
(define (pi-term x)
  (/ (* (- x 1) (+ x 1) 1.0)
     (square x)))
     
(* 4 (product pi-term 3 pi-next 13))
(* 4 (product-iter pi-term 3 pi-next 151))
(* 4 (product-iter pi-term 3 pi-next 1511))

