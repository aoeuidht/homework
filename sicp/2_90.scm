#lang racket
; Exercise 2.88. Extend the polynomial system to include subtraction of polynomials.
; (Hint: You may find it helpful to define a generic negation operation.)

(define (nega-term l)
  (cons (- (coeff l)) (order l)))

(define (add-terms L1 L2)
  (cond ((empty-termlist? L1) (map nega-term L2))
        ((empty-termlist? L2) L1)
        (else
         (let ((t1 (first-term L1)) (t2 (first-term L2)))
           (cond ((> (order t1) (order t2))
                  (adjoin-term
                   t1 (add-terms (rest-terms L1) L2)))
                 ((< (order t1) (order t2))
                  (adjoin-term
                   (nega-term t2) (add-terms L1 (rest-terms L2))))
                 (else
                  (adjoin-term
                   (make-term (order t1)
                              (sub (coeff t1) (coeff t2)))
                   (add-terms (rest-terms L1)
                              (rest-terms L2)))))))))