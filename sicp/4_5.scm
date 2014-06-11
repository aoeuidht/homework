; Exercise 4.5.  Scheme allows an additional syntax for cond clauses,
; (<test> => <recipient>). If <test> evaluates to a true value, then <recipient> is evaluated.
; Its value must be a procedure of one argument; this procedure is then invoked on the
; value of the <test>, and the result is returned as the value of the cond expression. For example

; (cond ((assoc 'b '((a 1) (b 2))) => cadr)
;       (else false))

; returns 2. Modify the handling of cond so that it supports this extended syntax.  
(define (cond? exp) (tagged-list? exp 'cond))
(define (cond-clauses exp) (cdr exp))
(define (cond-else-clause? clause)
  (eq? (cond-predicate clause) 'else))
(define (cond-predicate clause) (car clause))
(define (cond-actions clause) (cdr clause))
(define (add-cond-clause? clause) (pair? (cdr clause)))
(define (cond->if exp)
  (expand-clauses (cond-clauses exp)))

(define (expand-clauses clauses)
  (if (null? clauses)
      'false                          ; no else clause
      (let ((first (car clauses))
            (rest (cdr clauses)))
      (if (add-cond-clause? first)
          (make-if (cond-predicate first)
                   (list (cddr first) (cond-predicate first)) ; I miss the leading `list' at first
                   (expand-clauses (rest)))
          (if (cond-else-clause? first)
              (if (null? rest)
                  (sequence->exp (cond-actions first))
                  (error "ELSE clause isn't last -- COND->IF"
                         clauses))
              (make-if (cond-predicate first)
                       (sequence->exp (cond-actions first))
                       (expand-clauses rest)))))))