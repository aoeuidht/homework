#lang racket
; Exercise 2.73. Section 2.3.2 described a program that performs symbolic differentiation:

#|
(define (deriv exp var)
  (cond ((number? exp) 0)
        ((variable? exp) (if (same-variable? exp var) 1 0))
        ((sum? exp)
         (make-sum (deriv (addend exp) var)
                   (deriv (augend exp) var)))
        ((product? exp)
         (make-sum
           (make-product (multiplier exp)
                         (deriv (multiplicand exp) var))
           (make-product (deriv (multiplier exp) var)
                         (multiplicand exp))))
        ;<more rules can be added here>
        (else (error "unknown expression type -- DERIV" exp))))
|#
; We can regard this program as performing a dispatch on the type of the expression to be differentiated.
; In this situation the ``type tag'' of the datum is the algebraic operator symbol (such as +) 
; and the operation being performed is deriv. We can transform this program into data-directed
; style by rewriting the basic derivative procedure as

(define (deriv exp var)
   (cond ((number? exp) 0)
         ((variable? exp) (if (same-variable? exp var) 1 0))
         (else ((get 'deriv (operator exp)) (operands exp)
                                            var))))

(define (operator exp) (car exp))
(define (operands exp) (cdr exp))

; a. Explain what was done above. Why can't we assimilate the predicates number? and same-
; variable? into the data-directed dispatch?

; Answer:
; Because you can't list all numbers or variables.

; b. Write the procedures for derivatives of sums and products, and the auxiliary code required to install
; them in the table used by the program above.
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

(define (=number? exp num)
  (and (number? exp) (= exp num)))

(define (install-algebric-package)
  (define (make-sum a1 a2)
    (cond ((=number? a1 0) a2)
          ((=number? a2 0) a1)
          ((and (number? a1) (number? a2)) (+ a1 a2))
          (else (list '+ a1 a2))))
  
  (define (sum? x)
    (and (pair? x) (eq? (car x) '+)))
  (define (sum-deriv exp)
    (if (sum? exp)
        (make-sum (deriv (car exp) var)
                  (deriv (cdr exp) var))
        (error "use sum deriv for unsupport exp" exp)))
  
  (put 'make-exp '+ make-sum)
  (pub 'deriv '+ sum-deriv)
  
  (define (make-product m1 m2)
    (cond ((or (=number? m1 0) (=number? m2 0)) 0)
          ((=number? m1 1) m2)
          ((=number? m2 1) m1)
          ((and (number? m1) (number? m2)) (* m1 m2))
          (else (list '* m1 m2))))
  
  (define (product? x)
    (and (pair? x) (eq? (car x) '*)))
  
  (define (product-deriv exp)
    (make-sum
     (make-product (car exp)
                   (deriv (cdr exp) var))
     (make-product (deriv (car exp) var)
                   (cdr exp))))
  (put 'make-exp '* make-product)
  (pub 'deriv '* sum-deriv))

(install-algebric-package)

    