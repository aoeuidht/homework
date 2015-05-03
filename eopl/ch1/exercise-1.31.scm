#lang racket

#|
Write the following procedures for calculating on a bintree (defi- nition 1.1.7):
 leaf and interior-node, which build bintrees,
 leaf?, which tests whether a bintree is a leaf, and
 lson, rson, and contents-of, which extract the components of a node.
 contents-of should work on both leaves and interior nodes.
|#

#|
Bintree ::= Int | (symbol Bintree Bintree)
|#

; leaf Int --> Int
(define (leaf n) n)

; leaf? S-exp -> Bool
(define leaf? number?)

; interior: Sym X Bintree X Bintree --> Bintree
(define (interior sym lson rson)
  (list sym lson rson))

;lson Bintree --> Bintree | #f
(define (lson fat)
  (if (leaf? fat)
      #f
      (cadr fat)))

;rson: Bintree --> Bintree | #f
(define (rson fat)
  (if (leaf? fat)
      #f
      (caddr fat)))

; contents-of: Bintree --> Int | Symbol
(define (contents-of root)
  (if (leaf? root)
      root
      (car root)))