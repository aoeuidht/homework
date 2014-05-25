#lang racket
; Exericse
; this exercise descripe how to calculate pi:
; 1. in a square whih border 2, we can draw a cycle whose radius 1; so we get their area 4r^2 vs pi.r^2 
; 2. choose n points in the square randomly, we got n' points in the cycle
; 3. if it's a qualify random produrce, 4 / pi = n / n' = > pi = 4 . n' / n

(define (random-in-range low high)
  (let ((range (- high low)))
    (+ low (random range))))

(define (square x) (* x x))
(define (cesaro-gen x1 y1 x2 y2)
  (let ((x-aver (/ (+ x2 x1) 2))
        (y-aver (/ (+ y1 y2) 2))
        (radius (/ (- x2 x1) 2)))
  (lambda ()
    (< (+ (square (- (random-in-range x1 x2) x-aver))
          (square (- (random-in-range y1 y2) y-aver)))
       (square radius))
    )))

(define (estimate-pi x1 y1 x2 y2 trials)
  (* 4 (monte-carlo trials (cesaro-gen x1 y1 x2 y2))))

(define (monte-carlo trials experiment)
  (define (iter trials-remaining trials-passed)
    (cond ((= trials-remaining 0)
           (/ trials-passed trials))
          ((experiment)
           (iter (- trials-remaining 1) (+ trials-passed 1)))
          (else
           (iter (- trials-remaining 1) trials-passed))))
  (iter trials 0))


(estimate-pi 0 0 1000 1000 1000)