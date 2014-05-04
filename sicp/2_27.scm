#lang racket
; Exercise 2.27. Modify your reverse procedure of exercise 2.18 to produce a deep-reverse procedure
; that takes a list as argument and returns as its value the list with its elements
; reversed and with all sublists deep-reversed as well. For example,
;(define x (list (list 1 2) (list 3 4)))
;x
;((1 2) (3 4))
;(reverse x)
;((3 4) (1 2))
;(deep-reverse x)
;((4 3) (2 1))

; we copy the reverse form exec 2.18
(define (reverse tgt)
  (define (reverse-wrapper left cadidate)
    (if (null? left)
        cadidate
        (reverse-wrapper (cdr left) (cons (car left) cadidate))))
  (reverse-wrapper tgt '()))

; to imply the deep-reverse, wo have to reverse the car part of the tgt
(define (deep-reverse tgt)
  (define (reverse-wrapper left cadidate)
    (if (null? left)
        cadidate
        (reverse-wrapper (cdr left)
                         (let ((hd (car left)))
                           (if (pair? hd)
                               (cons (deep-reverse hd) cadidate)
                               (cons hd cadidate)      
                               )))))
  (reverse-wrapper tgt '()))

(deep-reverse '((1 2) (3 4)))
    
    
