#lang racket

#|

Write down a rule for doing type inference for let expressions. Using your rule, derive types for each of the following expressions, or determine that no such type exists.

|#

#| the lang rule
let-exp (e1 e2 e3)

t_e1 = t_e2
t_e3 = t_let-exp
|#

#|
let x = 4 in (x 3)

exp                       type-variable
---------------------------------------
let x = 4 in (x 3)        t0
x                         t1
4                         t2
(x 3)                     t3


exp                       equations
---------------------------------------
let x = 4 in (x 3)        t2 = int
                          t1 = t2
                          t0 = t3
(x 3)                     t1 = int -> t3

equations                 subsituation
---------------------------------------
t2 = int                  t1 = t2
t0 = t3
t1 = int -> t3

equations                 subsituation
---------------------------------------
t0 = t3                   t1 = int
int = int -> t3            t2 = int
~~~~~~~~~~~~~~~Fail



-------let f=proc(z) z in proc(x) -((f x),1)

exp                                type-variable
------------------------------------------------
letf=proc(z)zinproc(x)-((fx),1)    t0
f                                  t_f
proc(z) z                          t1
z                                  t_z
proc(x) -((f x), 1)                t2
x                                  t_x
-((f x), 1)                        t3
(f x)                              t4

exp                                equations
------------------------------------------------
letf=proc(z)zinproc(x)-((fx),1)    t0 = t2
                                   t_f = t1
                                   t1 = t_z -> t_z
proc(x) -((f x), 1)                t2 = t_x -> t3
                                   t3 = int
                                   t4 = int
                                   t_f = t_x -> t4

equations                          subsituation
-----------------------------------------------
t1 = t_z -> t_z                    t0 = t2
t2 = t_x -> t3                     t_f = t1
t3 = int
t4 = int
t1 = t_x -> t4

equations                          subsituation
-----------------------------------------------
                                   t0 = t2
                                   t_f = t1
t3 = int                           t1 = t_z -> t_z
t4 = int                           t2 = t_x -> t3
t1 = t_x -> t4

equations                          subsituation
-----------------------------------------------
                                   t0 = t2
                                   t_f = t1
                                   t1 = t_z -> t_z
                                   t2 = t_x -> int
t1 = t_x -> t4                     t3 -> int
                                   t4 -> int

equations                          subsituation
-----------------------------------------------
                                   t0 = int -> int
                                   t_f = int-> int
                                   t2 = int -> int
                                   t3 = int
                                   t4 = int
                                   t1 = int -> int
                                   t_x = int
                                   t_z = int


|#
