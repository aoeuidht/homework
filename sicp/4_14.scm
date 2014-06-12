#lang racket
#|
Exercise 4.14. Eva Lu Ator and Louis Reasoner are each experimenting with the metacircular
 evaluator. Eva types in the definition of map, and runs some test programs that use it. 
They work fine. Louis, in contrast, has installed the system version of map as a primitive
 for the metacircular evaluator. When he tries it, things go terribly wrong. Explain
 why Louis's map fails even though Eva's works.

|#

; Answer
; after we handle map by eval, the 1st parameter of map will no be a lambda clause or a procedure
; already defined, but a list starts with 'lambda or 'primitive or 'procedure
; so the system wide map will fail.

; I do a little experiment below
(define (adder x) (+ x 1))
(define primitive-procedures
  (list (list 'car car)
        (list 'cdr cdr)
        (list 'cons cons)
        (list 'null? null?)
        (list 'adder adder)
        (list 'map map)
        ;<more primitives>
        ))

; then get the following error

#|
;;; M-Eval input:
(map adder '(1 2 3 4))
((primitive #<procedure:adder>) (1 2 3 4)) 
application: not a procedure;
 expected a procedure that can be applied to arguments
  given: (mcons 'primitive (mcons #<procedure:adder> '()))
-------------------------- notice here, expect a procedure, got a list.
  arguments...:
   1
|#