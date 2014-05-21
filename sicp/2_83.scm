#lang racket
; Exercise 2.83. Suppose you are designing a generic arithmetic system for dealing with the tower of types
; shown in figure 2.25: integer, rational, real, complex. For each type (except complex), design a procedure
; that raises objects of that type one level in the tower. 
; Show how to install a generic raise operation that will work for each type (except complex).

;
(define (raise arg)
  (let ((atype (type-tag arg)))
    (cond ((eq? atype 'scheme-number) (make-rational (cdr arg) 1))
          ((eq? atype 'rational) (make-from-mag-ang (/ (cadr arg) (cddr arg)) 0))
          ((eq? atype 'complex) (error "got complex"))
          (else (error "Error")))))