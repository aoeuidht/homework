#lang racket
; Exercise 1.4. 
; Observe that our model of evaluation allows for combinations whose operators are compound expressions.
; Use this observation to describe the behavior of the following procedure:
; (define (a-plus-abs-b a b)
;   ((if (> b 0) + -) a b))


; Answers:
; in this scenario, the operator of `a b' would be different based on the value of `b',
; so the body of `a-plus-abs-b` is equal to:
(define (a-p-a-b a b)
  (if (> b 0)
       (+ a b)
       (- a b)
       ))

; tests
(a-p-a-b 2 3)
(a-p-a-b 2 -3)
(a-p-a-b -2 3)
(a-p-a-b -2 -3)