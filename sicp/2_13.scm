#lang racket
; Exercise 2.13. Show that under the assumption of small percentage tolerances 
; there is a simple formula for the approximate percentage tolerance of the product of two intervals
; in terms of the tolerances of the factors.
; You may simplify the problem by assuming that all numbers are positive.

; Answer
; I think the formular is (+ percent_x precent_y)
; (p0 + p1) / (1 + p0 * p1) percisely

; here is how
; asume we have (n0, p0) and (n1 p1) like this:
; (n0, p0)           |__________________________|
; (n1, p1) |______|

; according to excrcise 2.11, we have:
; max = n0(1+p0) * n1(1+p1)
; min = n0(1-p0) * n1(1-p1)

; so the new_p equals to
; (max - min) / (max + min)

; put `max` `min` in, you will get 
; new_p =  (p0 + p1) / (1 + p0 * p1)

; since both `p0` and `p1` are small percentage tolerance, so the denomnator is almost equal to 1
; so ther formular is `p_x + p_y`
