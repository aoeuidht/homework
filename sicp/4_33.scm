#lang r5rs
#|
Exercise 4.33.  Ben Bitdiddle tests the lazy list implementation given above by evaluating the expression

(car '(a b c))

To his surprise, this produces an error. After some thought, 
he realizes that the ``lists'' obtained by reading in quoted expressions
 are different from the lists manipulated by the new definitions of cons,
 car, and cdr. Modify the evaluator's treatment of quoted expressions so
 that quoted lists typed at the driver loop will produce true lazy lists. 
|#

(define (text-of-quotation exp)
  (define (quota-wrapper exp)
    (if (null? (cdr exp))
        (car exp)
        (list 'cons (car exp) (quota-wrapper (cdr exp)))))
  (if (pair? (cadr exp))
      (eval (quota-wrapper (cadr exp)))
      (cadr exp)))

(display (text-of-quotation (list 'quote '(a b c))))
