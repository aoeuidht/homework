#lang racket
; exercise 2.4
#|
Consider the data type of stacks of values, with an interface consisting
 of the procedures empty-stack, push, pop, top, and empty-stack?. 
Write a specification for these operations in the style of the example above. 
Which operations are constructors and which are observers?
|#


#|

(empty-stack)     = |[]|
(empty-stack? s)    = #f if s is |[]| else #t 
(push |[v1 v2 ... vn]| v)  = |[v1 v2 ... vn v]|
(pop |[v1 v2 ... vn-1 vn]|)  = vn, |[v1 v2 ... vn-1]|
(top |[v1 v2 ... vn]|) = vn

|#