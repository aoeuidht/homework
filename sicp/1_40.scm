#lang racket
(define tolerance 0.00001)
(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))

(define dx 0.00001)

(define (deriv g)
  (lambda (x)
    (/ (- (g (+ x dx)) (g x))
       dx)))

(define (newton-transform g)
  (lambda (x)
    (- x (/ (g x) ((deriv g) x)))))
(define (newtons-method g guess)
  (fixed-point (newton-transform g) guess))

(define (square x) (* x x))
(define (cube x) (* x x x))
(define (sqrt x)
  (newtons-method (lambda (y) (- (square y) x))
                  1.0))

(define (fixed-point-of-transform g transform guess)
  (fixed-point (transform g) guess))

; Exercise 1.40. Define a procedure cubic that can be used together with the newtons-method procedure in expressions of the form
; (newtons-method (cubic a b c) 1)
; to approximate zeros of the cubic x3 + ax2 + bx + c.

(define (cubic a b c)
  (lambda (x)
    (+ (cube x)
       (* (square x) a)
       (* x b)
       c)))

(newtons-method (cubic (- 6) (- 2) 35) 3.0)

((cubic -6 -2 35) 3.19)
((cubic -6 -2 35) 5.0)

