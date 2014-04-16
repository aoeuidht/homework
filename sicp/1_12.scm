#lang racket
; Exercise 1.12. The following pattern of numbers is called Pascal's triangle.

; The numbers at the edge of the triangle are all 1, 
; and each number inside the triangle is the sum of the two numbers above it.
; Write a procedure that computes elements of Pascal's triangle by means of a recursive process.

; Answer:

; based on the rule `each number inside the triangle is the sum of the two numbers above it`,
; let's format the pascal's triangle
; 1
; 1 1
; 1 2 1
; 1 3 3 1
; ......
; so asume we have a procedure `pa-tri row col` to calc the number at row & line, we have the rules:
; pa-tri x y -> pa-tri x-1 y-1 + pa-tri x-1 y
; pa-tri x y -> 1 if x < 3

(define (pa-tri row line)
  (if (or (< row 3)
          (= line 1)
          (= row line))
      1
      (+ (pa-tri (- row 1) (- line 1))
         (pa-tri (- row 1) line))))

; now we do some tests
(pa-tri 1 1)
(pa-tri 2 1)
(pa-tri 2 2)
(pa-tri 3 1)
(pa-tri 3 2)
(pa-tri 4 2)
(pa-tri 4 3)
(pa-tri 5 4)

