#lang racket
; Exercise 2.47. Here are two possible constructors for frames: 
(define (make-frame origin edge1 edge2)
 )
(define (make-frame origin edge1 edge2)
  (cons origin (cons edge1 edge2)))
;For each constructor supply the appropriate selectors to produce an implementation for frames.

; Answer
; the point of this exercise is `how list are constructed`.
; so we can rewrite the first `make-frame`
;  (list origin edge1 edge2)
; to
; (cons origin (cons edge1 (cons edge2 nil)))

; and compare the second `make-frame` to
; (cons origin (cons edge1 edge2)))

; we have the answer
; for define 1
(define (orgin-frame f)
  (car f))
(define (edge1-frame f)
  (cadr f))
(define (edge2-frame)
  (caddr f))

; for define 2
(define (origin-frame f)
  (car f))
(define (edge1-frame f)
  (cadr f))
(define (edge2-frame f)
  (cddr f))
  