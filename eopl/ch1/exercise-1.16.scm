#lang racket
; (invert lst), where lst is a list of 2-list (list of length two),
; returns a list with each 2-list reversed.

; invert: List(List of 2-list) --> List(List of 2-list)
; usage: (invert ’((a 1) (a 2) (1 b) (2 b)))
;        = ((1 a) (2 a) (b 1) (b 2))

(define (invert lst)
  (if (null? lst)
      '()
      (cons (cons (cadar lst)
                  (caar lst))
            (invert (cdr lst)))))

(invert '((a 1) (a 2) (1 b) (2 b)))