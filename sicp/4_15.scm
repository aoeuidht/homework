#lang racket
#|
Exercise 4.15. Given a one-argument procedure p and an object a, p is said to ``halt'' on a if evaluating the expression (p a) returns a value (as opposed to terminating with an error message or running forever). Show that it is impossible to write a procedure halts? that correctly determines whether p halts on a for any procedure p and object a. Use the following reasoning: If you had such a procedure halts?, you could implement the following program:
(define (run-forever) (run-forever))
(define (try p)
  (if (halts? p p)
      (run-forever)
      'halted))
Now consider evaluating the expression (try try) and show that any possible outcome (either halting or running forever) violates the intended behavior of halts?.23
|#

; Answer
; when we call (try try), then in the try procedure, it will call (halts? try try)
; so, if try can halt try, it will return #t, then the if clause will run, and (try try) will go to infinite
; loop, this is conflict with 'try can halt try'

; if try can't halt try, it return #f, then the else clause will run, then it will return 'halted,
; now try can halt try, also conflict. This is the famous ``halt theory''.