#lang racket
; Exercise 2.35. Redefine count-leaves from section 2.2.2 as an accumulation: 
; (define (count-leaves x)
;  (cond ((null? x) 0)
;        ((not (pair? x)) 1)
;        (else (+ (count-leaves (car x))
;                 (count-leaves (cdr x))))))
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

(define (count-leaves t)
  (accumulate +
              0
              (map (lambda (node)
                     (cond ((pair? node) (count-leaves node))
                           ((null? node) 0)
                           (else 1)))
                   t)))

(define x (cons (list 1 2) (list 3 4)))
(count-leaves x)
(count-leaves (list x x))