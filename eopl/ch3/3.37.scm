#lang eopl

;;; the recursion in dynamic binding
#|
let fact = proc (n) add1(n)
in let fact = proc (n)
               if zero?(n)
               then 1
               else *(n,(fact -(n,1)))
   in (fact 5)
|#


;;; The fact call after the ``in'', was calling the 2nd defined fact.
;;; The fact call in the 1st ``in'', was calling the 1st defined fact.
