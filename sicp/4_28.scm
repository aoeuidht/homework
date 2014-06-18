#lang r5rs
#|
Exercise 4.28. Eval uses actual-value rather than eval to evaluate the operator before passing it to apply,
 in order to force the value of the operator. Give an example that demonstrates the need for this forcing.
|#

; Answer
#|
let's see the hov procedure are applied
((application? exp)
 (apply (actual-value (operator exp) env)
        (operands exp)
        env))

it use the (actual-value (operator exp)) instead of (operator exp) because in scheme/lisp, we can returun 
a procedure in another procedure, so if the operator of exp is returned by another procedure,
it will be a thunk instead of a real procedure, so we have to got the actual-value first.
e.g.

(define (act-val f)
  (f 10))
(act-val (lambda (x) (+ x 2))
|#