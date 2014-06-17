#lang racket
#|
Exercise 4.25.  Suppose that (in ordinary applicative-order Scheme) we define unless as shown above and then define factorial in terms of unless as

(define (factorial n)
  (unless (= n 1)
          (* n (factorial (- n 1)))
          1))

What happens if we attempt to evaluate (factorial 5)? Will our definitions work in a normal-order language? 
|#

; Answer
#|
the procedure will NEVER renurn.
for the unless is equals to
(if (= n 1)
    1
    (factorial (- n 1))

In the application order language, the 1st call of factorial will 
call (factorial (- n 1); then we go into the 2nd call. the 2nd call
will call (factorial (- n 1); then we go into the 3rd call, etc.

whit n descrease each level, will will call (factorial 1).

(if (= 1 1)
    1  <------------------ normal order evaluate will return here, but
    (factorial (- 1 1)) <--- applicatin order will try to evaluate (factorial 0)
so we got infinite loop here, and the procedure will never return
|#