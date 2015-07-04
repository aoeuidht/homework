#lang eopl

(require "cps-out-lang.rkt")
(require "data-structures.rkt")       ; this includes environments

(provide value-of-program value-of/k)

;;; define the registers

(define r/exp 'undefined)
(define r/env 'undefined)
(define r/cont 'undefined)
(define r/proc 'undefined)

;;;;;;;;;;;;;;;; the interpreter ;;;;;;;;;;;;;;;;

;; value-of-program : Program -> ExpVal

(define value-of-program
  (lambda (pgm)
    (cases cps-out-program pgm
           (cps-a-program (exp1)
                          (set! r/exp exp1)
                          (set! r/env (init-env))
                          (set! r/cont (end-cont))
                          (value-of/k)))))

(define value-of-simple-exp
  (lambda ()
    (cases simple-expression r/exp
           (cps-const-exp (num) (num-val num))
           (cps-var-exp (var)
                        (apply-env r/env var))

           (cps-diff-exp (exp1 exp2)
                         (set! r/exp exp1)
                         (let ((val1
                                (expval->num
                                 (value-of-simple-exp)))
                               (val2
                                (begin (set! r/exp exp2)
                                       (expval->num
                                        (value-of-simple-exp)))))
                           (num-val
                            (- val1 val2))))

           (cps-zero?-exp (exp1)
                          (set! r/exp exp1)
                          (bool-val
                           (zero?
                            (expval->num
                             (value-of-simple-exp)))))

           (cps-sum-exp (exps)
                        (let ((nums (map
                                     (lambda (exp)
                                       (set! r/exp exp)
                                       (expval->num
                                        (value-of-simple-exp)))
                                     exps)))
                          (num-val
                           (let sum-loop ((nums nums))
                             (if (null? nums) 0
                                 (+ (car nums) (sum-loop (cdr nums))))))))

           (cps-proc-exp (vars body)
                         (proc-val
                          (procedure vars body r/env)))

           )))

;; value-of/k : TfExp * Env * Cont -> FinalAnswer
;; Page: 209
(define value-of/k
  (lambda ()
    (cases tfexp r/exp
           (simple-exp->exp (simple)
                            (set! r/exp simple)
                            (apply-cont r/cont
                                        (value-of-simple-exp)))
           (cps-let-exp (var rhs body)
                        (set! r/exp rhs)
                        (let ((val (value-of-simple-exp)))
                          (set! r/env (extend-env* (list var) (list val) r/env))
                          (set! r/exp body)
                          (value-of/k)))

           (cps-letrec-exp (p-names b-varss p-bodies letrec-body)
                           (set! r/env (extend-env-rec**
                                        p-names
                                        b-varss p-bodies r/env))
                           (set! r/exp letrec-body)
                           (value-of/k))

           (cps-if-exp (simple1 body1 body2)
                       (set! r/exp simple1)
                       (if (expval->bool (value-of-simple-exp))
                           (set! r/exp body1)
                           (set! r/exp body2))
                       (value-of/k))

           (cps-call-exp (rator rands)
                         (set! r/exp rator)
                         (let ((rator-proc
                                (expval->proc
                                 (value-of-simple-exp)))
                               (rand-vals
                                (map
                                 (lambda (simple)
                                   (set! r/exp simple)
                                   (value-of-simple-exp))
                                 rands)))
                           (set! r/proc rator-proc)
                           (apply-procedure/k rand-vals))))))

;; apply-cont : Cont * ExpVal -> Final-ExpVal
;; there's only one continuation, and it only gets invoked once, at
;; the end of the computation.
(define apply-cont
  (lambda (cont val)
    (cases continuation cont
           (end-cont () val))))

;; apply-procedure/k : Proc * ExpVal * Cont -> ExpVal
;; Page: 209
(define apply-procedure/k
  (lambda (args)
    (cases proc r/proc
           (procedure (vars body saved-env)
                      (set! r/exp body)
                      (set! r/env (extend-env* vars args saved-env))
                      (value-of/k)))))

'(define apply-procedure/k
   (lambda (proc1 args cont)
     (cases proc proc1
            (procedure (vars body saved-env)
                       (set! r/exp body)
                       (set! r/env saved-env)
                       (set! r/cont cont)
                       (value-of/k)))))

;; trace has to be in the module where the procedure is defined.
;; (trace value-of/k apply-cont)
