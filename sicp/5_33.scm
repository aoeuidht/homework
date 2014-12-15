#lang r5rs

#|
Exercise 5.33.  Consider the following definition of a factorial procedure, which is slightly different from the one given above:

(define (factorial-alt n)
  (if (= n 1)
      1
      (* n (factorial-alt (- n 1)))))

Compile this procedure and compare the resulting code with that produced for factorial. Explain any differences you find. Does either program execute more efficiently than the other? 
|#

#|
I diffed two version factorial, they make results with same lines of code, so the two functions are identical.
(* (factorial (- n 1)) n)

will push argl

and 

(* n (factorial-alt (- n 1)))

will push env for factorial-alt will invoked before n was read,

so the two procedures are identical
|#
