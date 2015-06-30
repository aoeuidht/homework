#lang eopl

(require "lang.rkt")
(require "data-structures.rkt")
(require "environments.rkt")

(provide value-of-program value-of/k)
(provide trace-apply-procedure)

(define trace-apply-procedure (make-parameter #f))

;;;;;;;;;;;;;;;; the interpreter ;;;;;;;;;;;;;;;;

;; value-of-program : Program -> ExpVal
(define value-of-program
  (lambda (pgm)
    (cases program pgm
           (a-program (body)
                      (value-of/k body (init-env) (end-cont))))))

;; value-of/k : Exp * Env * Cont -> FinalAnswer
;; Page: 173
(define value-of/k
  (lambda (exp env cont)
    (cases expression exp

           (const-exp (num) (apply-cont cont (num-val num)))

           (const-list-exp (nums)
                           (apply-cont cont
                                       (list-val (map num-val nums))))

           (var-exp (var) (apply-cont cont (apply-env env var)))

           (diff-exp (exp1 exp2)
                     (value-of/k exp1 env
                                 (diff1-cont exp2 env cont)))

           (unop-exp (unop exp1)
                     (value-of/k exp1 env
                                 (unop-arg-cont unop cont)))

           (if-exp (exp1 exp2 exp3)
                   (value-of/k exp1 env
                               (if-test-cont exp2 exp3 env cont)))

           (proc-exp (var body)
                     (apply-cont cont
                                 (proc-val
                                  (procedure var body env))))

           (call-exp (rator rand)
                     (value-of/k rator env
                                 (rator-cont rand env cont)))

           ;; make let a macro, because I'm too lazy to add the extra
           ;; continuation
           (let-exp (var exp1 body)
                    (value-of/k
                     (call-exp (proc-exp var body) exp1)
                     env
                     cont))

           (letrec-exp (p-name b-var p-body letrec-body)
                       (value-of/k
                        letrec-body
                        (extend-env-rec p-name b-var p-body env)
                        cont))

           (try-exp (exp1 var handler-exp)
                    (value-of/k exp1 env
                                (try-cont var handler-exp env cont)))

           (raise-exp (exp1)
                      (value-of/k exp1 env
                                  (raise1-cont cont))))))

;; apply-cont : continuation * expval -> final-expval



(define (end-cont)
  (make-cont
   (lambda (val) val)
   (lambda (val) (eopl:error 'apply-handler "uncaught exception!"))
   ))

(define (diff-cont exp2 saved-env saved-cont)
  (make-cont
   (lambda (val)
     (value-of/k exp2 saved-env (diff2-cont val saved-cont)))
   (lambda (val) (apply-handler val saved-cont))))

(define (diff2-cont val1 saved-cont)
  (make-cont
   (lambda (val)
     (let ((n1 (expval->num val1))
           (n2 (expval->num val)))
       (apply-cont saved-cont
                   (num-val (- n1 n2)))))
   (lambda (val)
     (apply-handler val saved-cont))))

(define (unop-arg-cont unop cont)
  (make-cont
   (lambda (val)
     (apply-cont cont
                 (apply-unop unop val)))
   (lambda (val)
     (apply-handler val cont)))
  )

(define (if-test-cont exp2 exp3 env cont)
  (make-cont

   (lambda (val)
     (if (expval->bool val)
         (value-of/k exp2 env cont)
         (value-of/k exp3 env cont)))
   (lambda (val) (apply-handler val cont))))

(define (rator-cont rand saved-env saved-cont)
  (make-cont
   (lambda (val)
     (value-of/k rand saved-env
                 (rand-cont val saved-cont)))
   (lambda (val) (apply-handler val saved-cont))))

(define (rand-cont val1 saved-cont)
  (make-cont
   (lambda (val)
     (let ((proc (expval->proc val1)))
       (apply-procedure proc val saved-cont)))
   (lambda (val) (apply-handler val saved-cont))))

(define (try-cont var handler-exp saved-env saved-cont)
  (make-cont
   (lambda (val) (apply-cont saved-cont val))
   (lambda (val)
     (value-of/k handler-exp
                 (extend-env var val saved-env)
                 saved-cont))
   ))

(define (diff1-cont exp2 saved-env saved-cont)
  (make-cont
   (lambda (val)
     (value-of/k exp2 saved-env (diff2-cont val saved-cont)))
   (lambda (val) (apply-handler val saved-cont)))
  )

(define (raise1-cont saved-cont)
  (make-cont
   (lambda (val) (apply-handler val saved-cont))
   (lambda (val) (apply-handler val saved-cont))
   )
  )

(define (make-cont apply-hand exception-hand)
  (lambda (fake  val)
    ((if fake apply-hand exception-hand) val)))

(define (apply-cont cont val)
  (cont #t val))

;; apply-handler : ExpVal * Cont -> FinalAnswer
(define (apply-handler val cont)
  (cont #f val))


;; apply-procedure : procedure * expval * cont -> final-expval

(define apply-procedure
  (lambda (proc1 arg cont)
    (cases proc proc1
           (procedure (var body saved-env)
                      (value-of/k body
                                  (extend-env var arg saved-env)
                                  cont)))))


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
