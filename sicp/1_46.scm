#lang racket

(define (iter-improve good-chk imp-guess)
  (define (ii-wrapper current-guess)
    (if (good-chk current-guess)
        current-guess
        (ii-wrapper (imp-guess current-guess))))
  ; how i can save the wrapper here, and write recursion in lambda?
  ; check this post out: http://yinwang0.wordpress.com/2012/04/09/reinvent-y/
  (lambda (f-guess)
    (ii-wrapper f-guess)))

; now the sqrt procedure
(define (sqrt x)
  ((iter-improve
    (lambda (g) (< (abs (- (* g g) x)) 0.001))
    (lambda (g) (/ (+ g (/ x g)) 2)))
   1.0))

(sqrt 2)


; the fixed-point procedure
(define (fixed-point f)
  ((iter-improve
    (lambda (g) (< (abs (- (f g) g)) 0.001))
    (lambda (g) (/ (+ g (f g)) 2)))
   1.0))

(fixed-point (lambda (x) (/ 3 x)))
    