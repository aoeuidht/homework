#lang racket
; Exercise 2.14. Demonstrate that Lem is right.
; Investigate the behavior of the system on a variety of arithmetic expressions.
; Make some intervals A and B, and use them in computing the expressions A/A and A/B.
; You will get the most insight by using intervals whose width is a small percentage of the center value.
; Examine the results of the computation in center-percent form (see exercise 2.12).
(define (add-interval x y)
  (make-interval (+ (lower-bound x) (lower-bound y))
                 (+ (upper-bound x) (upper-bound y))))

(define (mul-interval x y)
  (let ((p1 (* (lower-bound x) (lower-bound y)))
        (p2 (* (lower-bound x) (upper-bound y)))
        (p3 (* (upper-bound x) (lower-bound y)))
        (p4 (* (upper-bound x) (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
                   (max p1 p2 p3 p4))))

(define (div-interval x y)
  (mul-interval x (make-interval (/ 1.0 (upper-bound y))
                                (/ 1.0 (lower-bound y)))))

(define (make-interval a b) (cons a b))
(define (upper-bound r)
  (cdr r))
(define (lower-bound r)
  (car r))

(define (par1 r1 r2)
  (div-interval (mul-interval r1 r2)
                (add-interval r1 r2)))
(define (par2 r1 r2)
  (let ((one (make-interval 1 1)))
    (div-interval one
                  (add-interval (div-interval one r1)
                                (div-interval one r2)))))


(let ((r1 (make-interval 9999 10001))
      (r2 (make-interval 19998 20002)))
  (par1 r1 r2)
  )

; the result is '(6664.666933306669 . 6668.666933360003)
; whit (center . percent) it's (6666.67, 0.0003)

(let ((r1 (make-interval 9999 10001))
      (r2 (make-interval 19998 20002)))
  (par2 r1 r2)
  )

; the resurt is '(6665.999999999999 . 6667.333333333333)
; whit (center . percent) it's (6666.67, 0.0001)

; Why? as a conclusion of 2.13, mul will add the tolerance (percentage together)
; also, check the div implementation, it also have the mul operation in it, so 
; the more mul/div operations a fromula have, the bigger torlance in result.