#lang eopl

;; interpreter for the LETREC language.  The \commentboxes are the
;; latex code for inserting the rules into the code in the book.
;; These are too complicated to put here, see the text, sorry.

(require "lang.rkt")
(require "data-structures.rkt")
(require "environments.rkt")

(provide value-of-program value-of)

;;;;;;;;;;;;;;;; the interpreter ;;;;;;;;;;;;;;;;

;; value-of-program : Program -> ExpVal
(define value-of-program
  (lambda (pgm)
    (cases
     program pgm
     (a-program
      (exp1)
      (value-of/k exp1 (init-env) (end-cont))))))

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
   ))

;; value-of : Exp * Env -> ExpVal
;; Page: 83
(define value-of
  (lambda (exp env)
    (cases expression exp

      ;;\commentbox{ (value-of (const-exp \n{}) \r) = \n{}}
      (const-exp (num) (num-val num))

      ;;\commentbox{ (value-of (var-exp \x{}) \r) = (apply-env \r \x{})}
      (var-exp (var) (apply-env env var))

      ;;\commentbox{\diffspec}
      (diff-exp (exp1 exp2)
                (let ((val1 (value-of exp1 env))
                      (val2 (value-of exp2 env)))
                  (let ((num1 (expval->num val1))
                        (num2 (expval->num val2)))
                    (num-val
                     (- num1 num2)))))

      ;;\commentbox{\zerotestspec}
      (zero?-exp (exp1)
                 (let ((val1 (value-of exp1 env)))
                   (let ((num1 (expval->num val1)))
                     (if (zero? num1)
                         (bool-val #t)
                         (bool-val #f)))))

      ;;\commentbox{\ma{\theifspec}}
      (if-exp (exp1 exp2 exp3)
              (let ((val1 (value-of exp1 env)))
                (if (expval->bool val1)
                    (value-of exp2 env)
                    (value-of exp3 env))))

      ;;\commentbox{\ma{\theletspecsplit}}
      (let-exp (var exp1 body)
               (let ((val1 (value-of exp1 env)))
                 (value-of body
                           (extend-env var val1 env))))

      (proc-exp (var body)
                (proc-val (procedure var body env)))

      (call-exp (rator rand)
                (let ((proc (expval->proc (value-of rator env)))
                      (arg (value-of rand env)))
                  (apply-procedure proc arg)))

      (letrec-exp (p-name b-var p-body letrec-body)
                  (value-of letrec-body
                            (extend-env-rec p-name b-var p-body env)))

      )))

;; apply-procedure : Proc * ExpVal -> ExpVal

(define apply-procedure
  (lambda (proc1 arg)
    (cases proc proc1
      (procedure (var body saved-env)
                 (value-of body (extend-env var arg saved-env))))))

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
                    (apply-procedure/k (expval->proc rator) val cont))

         ))

(define (apply-procedure/k rator rand cont)
  (cases proc rator
         (procedure (var body saved-env)
                    (value-of/k body
                                (extend-env var rand saved-env)
                                cont)))
  )
