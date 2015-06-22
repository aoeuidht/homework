#lang eopl

;; interpreter for the LETREC language.  The \commentboxes are the
;; latex code for inserting the rules into the code in the book.
;; These are too complicated to put here, see the text, sorry.

(require "lang.rkt")
(require "data-structures.rkt")
(require "environments.rkt")
(require (only-in racket pretty-print))
(provide value-of-program )

;;;;;;;;;;;;;;;; the interpreter ;;;;;;;;;;;;;;;;
;;; the trampoline
(define (trampoline bounce)
  (if (expval? bounce)
      bounce
      (trampoline (bounce))))

;; value-of-program : Program -> ExpVal
(define value-of-program
  (lambda (pgm)
    (cases
     program pgm
     (a-program
      (exp1)
      (trampoline
       (value-of/k exp1 (init-env) (end-cont)))))))

(define (value-of/k exp env cont)
  (cases
   expression exp
   (const-exp (num) (apply-cont cont (num-val num)))
   (var-exp (var) (apply-cont cont (apply-env env var)))
   (proc-exp (var body)
             (apply-cont cont
                         (proc-val (procedure var body env))))
   (letrec-exp (p-name b-var p-body letrec-body)
               (value-of/k letrec-body
                           (extend-env-rec p-name b-var p-body env)
                           cont))

   (zero?-exp (exp1)
              (value-of/k exp1 env
                          (zero1-cont cont)))

   (let-exp (var exp1 body)
            (value-of/k exp1 env
                        (let-exp-cont var body env cont)))
   (if-exp (exp1 exp2 exp3)
           (value-of/k exp1 env
                       (if-test-cont exp2 exp3 env cont)))

   (diff-exp (exp1 exp2)
             (value-of/k exp1 env
                         (diff1-cont exp2 env cont)))
   (call-exp (rator rand)
             (value-of/k rator env
                         (rator-cont rand env cont))
             )

   ;;
   (empty-list-exp () (apply-cont cont (list-val '())))
   (car-exp (exp1)
            (value-of/k exp1 env
                        (car-cont cont)))

   (cdr-exp (exp1)
            (value-of/k exp1 env (cdr-cont cont)))

   (list-exp (exp1)
             (if (null? exp1)
                 (apply-cont cont (list-val '()))
                 (value-of/k (list-exp (cdr exp1)) env
                             (list-cdr-cont (car exp1) env cont))))

   (begin-exp (exps)
              (value-of/k (car exps) env
                          (begin-cont (cdr exps) env cont)
                          ))
   ))

;;; -------- the continution part --------
;;; apply
(define (apply-cont cont val)
  (cases continution cont
         (end-cont ()
                   (begin
                     (eopl:printf "End-of-computation.~%")
                     val))
         (zero1-cont (cont)
                     (apply-cont
                      cont
                      (bool-val
                       (zero? (expval->num val)))))
         (let-exp-cont (var body env cont)
                       (value-of/k body
                                   (extend-env var val env)
                                   cont))
         (if-test-cont (exp2 exp3 env cont)
                       (if (expval->bool val)
                           (value-of/k exp2 env cont)
                           (value-of/k exp3 env cont)))
         (diff1-cont (exp2 env cont)
                     (value-of/k exp2 env
                                 (diff2-cont val cont)))

         (diff2-cont (val1 cont)
                     (let ((num1 (expval->num val1))
                           (num2 (expval->num val)))
                       (apply-cont cont (num-val (- num1 num2)))))

         (rator-cont (rand env cont)
                     (value-of/k rand env
                                 (rand-cont val cont)))

         (rand-cont (rator cont)
                    (lambda ()
                      (apply-procedure/k (expval->proc rator) val cont)))

         (list-cdr-cont
          (exp env cont)
          (value-of/k exp env
                      (list-car-cont val cont)))
         (list-car-cont (cdr-val cont)
                        (apply-cont cont
                                    (list-val
                                     (cons val (expval->list cdr-val)))))
         (cdr-cont (cont)
                   (apply-cont cont (list-val (cdr (expval->list val)))))
         (car-cont (cont)
                   (apply-cont cont (car (expval->list val))))

         ;; begin-cont
         (begin-cont (exps env cont)
                     (if (null? exps)
                         (apply-cont cont val)
                         (value-of/k (begin-exp exps) env cont)))
         ))

(define (apply-procedure/k rator rand cont)
  ;(lambda ())
  (cases proc rator
         (procedure (var body saved-env)
                    (value-of/k body
                                (extend-env var rand saved-env)
                                cont))))
