#lang racket
; Exercise 3.2. In software-testing applications, it is useful to be able to count the number
; of times a given procedure is called during the course of a computation. Write a procedure
; make-monitored that takes as input a procedure, f, that itself takes one input.
; The result returned by make-monitored is a third procedure, say mf, that keeps track
; of the number of times it has been called by maintaining an internal counter.
; If the input to mf is the special symbol how-many-calls?, then mf returns the value of the counter.
; If the input is the special symbol reset-count, then mf resets the counter to zero.
; For any other input, mf returns the result of calling f on that input and increments
; the counter. For instance, we could make a monitored version of the sqrt procedure:


(define (square n) (* n n))
(define (average x y) (/ (+ x y) 2))

(define (sqrt-iter guess old-guess x)
  (if (good-enough? guess old-guess)
      guess
      (sqrt-iter (improve guess x) guess
                 x)))

(define (improve guess x)
  (average guess (/ x guess)))

; we old-guess and current-guess are nearby, done!
(define (good-enough? guess old-guess)
  (< (abs (- guess old-guess)) 0.001))

(define (sqrt x)
  (sqrt-iter 1.0 x x))

(define (make-monitored f)
  (let ((ic 0))
    (lambda (v)
      (if (eq? v 'how-many-calls?)
          ic
          (begin (set! ic (+ 1 ic))
                 (f v)
                 )))))

(define s (make-monitored sqrt))
(s 100)
(s 'how-many-calls?)