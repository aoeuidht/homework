#lang eopl

(require "lang.rkt")
(require "data-structures.rkt")
(require "environments.rkt")
(require (only-in racket pretty-print))

(provide value-of-program value-of/k)
(provide trace-apply-procedure)

(define trace-apply-procedure (make-parameter #t))

;;;;;;;;;;;;;;;; continuations ;;;;;;;;;;;;;;;;


(define-datatype continuation continuation?
  (end-cont)                          ; []
  (diff1-cont                       ; cont[(- [] (value-of e2 env))]
   (exp2 expression?)
   (env environment?)
   (cont continuation?))
  (diff2-cont                         ; cont[(- val1 [])]
   (val1 expval?)
   (cont continuation?))
  (unop-arg-cont
   (unop unary-op?)
   (cont continuation?))
  (if-test-cont
   (exp2 expression?)
   (exp3 expression?)
   (env environment?)
   (cont continuation?))
  (rator-cont            ; cont[(apply-proc [] (value-of rand env))]
   (rand expression?)
   (env environment?)
   (cont continuation?))
  (rand-cont                          ; cont[(apply-proc val1 [])]
   (val1 expval?)
   (cont continuation?))
  (try-cont
   (var symbol?)
   (handler-exp expression?)
   (env environment?)
   (cont continuation?)
   (exception-cont continuation?)
   )
  (raise1-cont
   (saved-cont continuation?))
  )

;;;;;;;;;;;;;;;; the interpreter ;;;;;;;;;;;;;;;;

;; value-of-program : Program -> ExpVal
(define value-of-program
  (lambda (pgm)
    (cases program pgm
           (a-program (body)
                      (value-of/k body (init-env) (end-cont) (end-cont))))))

;; value-of/k : Exp * Env * Cont -> FinalAnswer
;; Page: 173
(define value-of/k
  (lambda (exp env cont exception-cont)
    (cases expression exp

           (const-exp (num) (apply-cont cont (num-val num) exception-cont))

           (const-list-exp (nums)
                           (apply-cont cont
                                       (list-val (map num-val nums))
                                       exception-cont))

           (var-exp (var) (apply-cont cont (apply-env env var) exception-cont))

           (diff-exp (exp1 exp2)
                     (value-of/k exp1 env
                                 (diff1-cont exp2 env cont)
                                 exception-cont))

           (unop-exp (unop exp1)
                     (value-of/k exp1 env
                                 (unop-arg-cont unop cont)
                                 exception-cont))

           (if-exp (exp1 exp2 exp3)
                   (value-of/k exp1 env
                               (if-test-cont exp2 exp3 env cont)
                               exception-cont))

           (proc-exp (var body)
                     (apply-cont cont
                                 (proc-val
                                  (procedure var body env))
                                 exception-cont))

           (call-exp (rator rand)
                     (value-of/k rator env
                                 (rator-cont rand env cont)
                                 exception-cont))

           ;; make let a macro, because I'm too lazy to add the extra
           ;; continuation
           (let-exp (var exp1 body)
                    (value-of/k
                     (call-exp (proc-exp var body) exp1)
                     env
                     cont
                     exception-cont))

           (letrec-exp (p-name b-var p-body letrec-body)
                       (value-of/k
                        letrec-body
                        (extend-env-rec p-name b-var p-body env)
                        cont
                        exception-cont))

           (try-exp (exp1 var handler-exp)
                    (value-of/k exp1 env
                                (try-cont var handler-exp env cont exception-cont)
                                (try-cont var handler-exp env cont exception-cont)))

           (raise-exp (exp1)
                      (value-of/k exp1 env
                                  (raise1-cont cont)
                                  exception-cont)))))

;; apply-cont : continuation * expval -> final-expval

(define apply-cont
  (lambda (cont val exception-cont)
    (cases continuation cont
           (end-cont () val)
           (diff1-cont (exp2 saved-env saved-cont)
                       (value-of/k exp2 saved-env (diff2-cont val saved-cont) exception-cont))
           (diff2-cont (val1 saved-cont)
                       (let ((n1 (expval->num val1))
                             (n2 (expval->num val)))
                         (apply-cont saved-cont
                                     (num-val (- n1 n2))
                                     exception-cont)))
           (unop-arg-cont (unop cont)
                          (apply-cont cont
                                      (apply-unop unop val)
                                      exception-cont))
           (if-test-cont (exp2 exp3 env cont)
                         (if (expval->bool val)
                             (value-of/k exp2 env cont exception-cont)
                             (value-of/k exp3 env cont exception-cont)))
           (rator-cont (rand saved-env saved-cont)
                       (value-of/k rand saved-env
                                   (rand-cont val saved-cont)
                                   exception-cont))
           (rand-cont (val1 saved-cont)
                      (let ((proc (expval->proc val1)))
                        (apply-procedure proc val saved-cont exception-cont)))
           ;; the body of the try finished normally-- don't evaluate the handler
           (try-cont (var handler-exp saved-env saved-cont exception-cont)
                     (apply-cont saved-cont val exception-cont))
           ;; val is the value of the argument to raise
           (raise1-cont (saved-cont)
                        ;; we put the short argument first to make the trace more readable.
                        (cases continuation exception-cont
                               (try-cont (var handler-exp saved-env
                                              saved-cont exception-cont)
                                        (value-of/k handler-exp
                                                    (extend-env var val saved-env)
                                                    saved-cont exception-cont))
                              (else (eopl:error 'apply-handler "uncaught exception!")))
                        )
           )))

;; apply-procedure : procedure * expval * cont -> final-expval

(define apply-procedure
  (lambda (proc1 arg cont exception-cont)
    (cases proc proc1
           (procedure (var body saved-env)
                      (value-of/k body
                                  (extend-env var arg saved-env)
                                  cont exception-cont)))))


(define apply-unop
  (lambda (unop val)
    (cases unary-op unop
           (null?-unop ()
                       (bool-val
                        (null? (expval->list val))))
           (car-unop ()
                     (car (expval->list val)))
           (cdr-unop ()
                     (list-val (cdr (expval->list val))))
           (zero?-unop ()
                       (bool-val
                        (zero? (expval->num val)))))))


;; to get the detailed trace:
;; (trace value-of/k apply-cont apply-handler)
