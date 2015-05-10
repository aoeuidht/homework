#lang eopl
;;; exercise 2.22

#|
Using define-datatype, implement the stack data type of exercise 2.4.
|#
(require eopl/tests/private/utils)

(define-datatype s-list s-list?
  (an-s-list
   (sexps (list-of s-exp?))))

(define list-of
  (lambda (pred)
    (lambda (val)
      (or (null? val)
          (and (pair? val)
               (pred (car val))
               ((list-of pred) (cdr val)))))))

(define-datatype s-exp s-exp?
  (symbol-s-exp
   (sym symbol?))
  (s-list-s-exp
   (slst s-list?)))

(define-datatype stack stack?
  (empty-stack (es null?))
  (non-empty-stack (nones (lambda (s) (not (null? s))))))

(define (empty-stack? s)
  (cases stack s
         (empty-stack (es) #t)
         (else #f)))

(define (push val s)
  (cases stack s
         (empty-stack (es) (non-empty-stack (list val)))
         (non-empty-stack (nones) (non-empty-stack (cons val nones)))
         ))

(define (pop s)
  (cases stack s
         (non-empty-stack (nones) (non-empty-stack (cdr nones)))
         (else #f)
         ))

(define (top s)
  (cases stack s
         (non-empty-stack (nones) (car nones))
         (else #f)
         ))

(display (empty-stack? (empty-stack '())))

(display (push 5 (push 3 (empty-stack '()))))



(display (pop (push 5 (push 3 (empty-stack '())))))

(display (top (push 5 (push 3 (empty-stack '())))))
