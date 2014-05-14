#lang racket
; Exercise 2.58. Suppose we want to modify the differentiation program so that it 
; works with ordinary mathematical notation, in which + and * are infix rather than prefix operators.
; Since the differentiation program is defined in terms of abstract data, 
; we can modify it to work with different representations of expressions solely by
; changing the predicates, selectors, and constructors that define the representation of the algebraic expressions 
; on which the differentiator is to operate.

; a. Show how to do this in order to differentiate algebraic expressions presented in infix form,
; such as (x + (3 * (x + (y + 2)))).
; To simplify the task, assume that + and * always take two arguments and that expressions are fully parenthesized.
;(define (in-to-pre exp)
;  (let ((oper (car exp))
;        (opet (cadr exp))
;        (opnd (caddr exp)))
;    (if (pair? opnd)
;        (let ((opnd-rst (in-to-pre opnd)))
;          (if (eq? opet (car opnd-rst))  ; we do some merge job here
;              (append (list opet oper) (cdr opnd-rst))
;              (list opet
;                    oper 
;                    (in-to-pre opnd))))
;        (list opet oper opnd))))

; (in-to-pre '(x + (3 * (x + (y + 2)))))

; Answers
#|
(define (sum? x)
  (and (pair? x) (eq? (cadr x) '+)))

(define (addend s) (car s))
(define (augend s) (caddr s))

(define (product? x)
        (and (pair? x) (eq? (cadr x) '*)))

; change these
(define (multiplier p) (car p))
; (define (multiplicand p) (caddr p))
(define (multiplicand p) (caddr p))
|#
; b. The problem becomes substantially harder if we allow standard algebraic notation, 
; such as (x + 3 * (x + y + 2)), which drops unnecessary parentheses and assumes that multiplication is done before
; addition. Can you design appropriate predicates, selectors, and
; constructors for this notation such that our derivative program still works?

; I think the point of this problem is when we met the `*` operation, you can't just say it's a multiplier, it's maybe a sum.
; Also, when it's a sum, you can't just give its car as the addend

; if the exp has any '+, it's a sum.
(define (sum? x)
  (display x)
  (and (pair? x) 
       (or (eq? (cadr x) '+)
           (and (not (null? (cdddr x))) (sum? (cddr x)))
           )
       ))

(define (addend s)
  (let ((oper (car s))
        (opet (cadr s))
        (open (cddr s)))
  (if (eq? opet '+)
      oper
      (let ((ae (addend open)))
        (append (list oper opet)
                (if (pair? ae)
                    ae
                    (list ae)))))
  ))

(define (augend s)
   (let ((opet (cadr s))
         (open (cddr s)))
     (if (eq? opet '+)
         open
         (augend open))))

(augend '(a + b + c))
(augend '(a * b + c * d))

(define (product? x)
  (and (pair? x)
       (eq? (cadr x) '*)
       (or (null? (cdddr x))
           (not (sum? (cddr x))))))
(product? '(a * b + c))
(product? '(a * b * c))
(product? '(a * b))

(define (multiplier p) (car p))
(define (multiplicand p)
  (if (null? (cdddr p))
      (caddr p)
      (cddr p))
  )
(multiplier '(a * b * c))
(multiplicand '(a * b * c))
(multiplicand '(a * c))
(multiplicand '(a * (b + d)))
(product? '(a * (b + d)))
