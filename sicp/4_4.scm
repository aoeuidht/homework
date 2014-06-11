; Exercise 4.4.  Recall the definitions of the special forms and and or from chapter 1:

;    and: The expressions are evaluated from left to right. If any expression
; evaluates to false, false is returned; any remaining expressions are not evaluated.
; If all the expressions evaluate to true values, the value of the last expression is
; returned. If there are no expressions then true is returned.

;    or: The expressions are evaluated from left to right. If any expression evaluates
; to a true value, that value is returned; any remaining expressions are not evaluated.
; If all expressions evaluate to false, or if there are no expressions, then false is returned. 

; Install and and or as new special forms for the evaluator by defining appropriate syntax
; procedures and evaluation procedures eval-and and eval-or. Alternatively, show how to 
; implement and and or as derived expressions. 

; Answer

; the special form way:
(define (eval exp env)
  (cond ((self-evaluating? exp) exp)
        ((variable? exp) (lookup-variable-value exp env))
        ((quoted? exp) (text-of-quotation exp))
        ((assignment? exp) (eval-assignment exp env))
        ((definition? exp) (eval-definition exp env))
        ((if? exp) (eval-if exp env))
        ((lambda? exp)
         (make-procedure (lambda-parameters exp)
                         (lambda-body exp)
                         env))
        ((begin? exp) 
         (eval-sequence (begin-actions exp) env))
        ((cond? exp) (eval (cond->if exp) env))
        ((and? exp) (eval-and exp env))
        ((or? exp) (eval-or exp env))
        ((application? exp)
         (apply (eval (operator exp) env)
                (list-of-values (operands exp) env)))
        (else
         (error "Unknown expression type -- EVAL" exp))))

(define (and? exp) (tagged-list? exp 'and))
(define (and-pred exp) (cdr exp))
(define (eval-and exp env)
  (define (eval-and-preds preds env)
    (let ((fst-pred (eval (first-exp preds) env)))
      (if (last-exp? preds)
        fst-pred
        (if (true? fst-pred)
            (eval-and-preds (rest-exp preds) env)
            #f))))
  (eval-and-preds (cdr exp) env))

(define (or? exp) (tagged-list? exp 'or))
(define (eval-or exp env)
  (define (eval-or-preds preds env)
    (let ((fst-pred (eval (first-exp preds) env)))
      (if (last-exp? preds)
          fst-pred
          (if (true? fst-pred)
              #t
              (eval-and-preds (rest-exp preds) env)))))
  (eval-or-preds (cdr-exp) env))

; the derived way

(define (and? exp) (tagged-list? exp 'and))
(define (and-preds exp) (cdr exp))
(define (and->if exp)
  (expand-and (and-preds exp)))

(define (expand-and predicates)
  (if (null? predicates)
      #t
      (let ((f (car predicates))
            (r (cdr predicates)))
        (make-if f (expand-and r) #f))))
  

(define (or? exp) (tagged-list? exp 'or))
(define (or-preds exp) (cdr exp))
(define (or->if exp)
  (expand-or (or-preds exp)))

(define (expand-or predicates)
  (if (null? predicates)
      #f
      (let ((f (car predicates))
            (r (cdr predicates)))
        (make-if f #t (expand-and r)))))