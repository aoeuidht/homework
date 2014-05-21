#lang racket
; Exercise 2.82. Show how to generalize apply-generic to handle coercion in the general case of multiple arguments.
; One strategy is to attempt to coerce all the arguments to the type of the first argument,
; then to the type of the second argument, and so on. Give an example of a
; situation where this strategy (and likewise the two-argument version given above) is not sufficiently general.
; (Hint: Consider the case where there are some suitable mixed-type operations present in the table that will not be tried.)

; Answer
; Suppose  we have a system with this hierarchy
; D <-- B <-- A
; ^
; |
; C

; so if we have a procedure (p A B C)
; U can never choose a type, and both other types can change to it.
; But you can convert them to D and do some calculation.