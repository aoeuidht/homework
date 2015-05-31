#lang eopl

;; interpreter for the EXPLICIT-REFS language

(require "lang.rkt")
(require "data-structures.rkt")
(require "environments.rkt")
(require "store.rkt")

(require (only-in racket pretty-print))

(provide value-of-program value-of instrument-let instrument-newref)

;;;;;;;;;;;;;;;; switches for instrument-let ;;;;;;;;;;;;;;;;

(define instrument-let (make-parameter #f))

;; say (instrument-let #t) to turn instrumentation on.
;;     (instrument-let #f) to turn it off again.

;;;;;;;;;;;;;;;; the interpreter ;;;;;;;;;;;;;;;;

;; value-of-program : Program -> ExpVal
;; Page: 110
(define value-of-program
  (lambda (pgm)
    (initialize-store!)               ; new for explicit refs.
    (cases program pgm
           (a-program (exp1)
                      (cases answer
                             (value-of exp1 (init-env) (get-store))
                             (an-answer (val new-store)
                                        val))))))

;; value-of : Exp * Env -> ExpVal
;; Page: 113
(define value-of
  (lambda (exp env store)
    (cases expression exp

      ;;\commentbox{ (value-of (const-exp \n{}) \r) = \n{}}
      (const-exp (num)
                 (an-answer (num-val num) store))

      ;;\commentbox{ (value-of (var-exp \x{}) \r) = (apply-env \r \x{})}
      (var-exp (var)
               (an-answer
                (apply-env env var)
                store))

      ;;\commentbox{\diffspec}
      (diff-exp
       (exp1 exp2)
       (cases answer (value-of exp1 env store)
              (an-answer
               (val1 new-store)
               (cases answer (value-of exp2 env new-store)
                      (an-answer
                       (val2 new-store2)
                       (let ((num1 (expval->num val1))
                             (num2 (expval->num val2)))
                         (an-answer
                          (num-val (- num1 num2))
                          new-store2)
                         )
                       ))))
       )

      ;;\commentbox{\zerotestspec}
      (zero?-exp
       (exp1)
       (cases answer (value-of exp1 env store)
              (an-answer (val1 new-store)
                         (if (zero? (expval->num val1))
                             (an-answer (bool-val #t) new-store)
                             (an-answer (bool-val #f) new-store)))))

      ;;\commentbox{\ma{\theifspec}}
      (if-exp (exp1 exp2 exp3)
              (cases answer (value-of exp1 env store)
                     (an-answer (val1 new-store)
                                (if (expval->bool val1)
                                    (value-of exp2 env new-store)
                                    (value-of exp3 env new-store)))))

      ;;\commentbox{\ma{\theletspecsplit}}
      (let-exp (var exp1 body)
               (cases answer (value-of exp1 env store)
                      (an-answer (val1 new-store)
                                 (value-of body
                                             (extend-env var val1 env)
                                             new-store)
                                  )))


      (proc-exp (var body)
                (an-answer (proc-val (procedure var body env)) store))

      (call-exp (rator rand)
                (cases answer (value-of rator env store)
                       (an-answer (rator-val new-store)
                                  (cases answer (value-of rand env new-store)
                                         (an-answer (rand-val new-store2)
                                                    (apply-procedure
                                                     (expval->proc rator-val)
                                                     rand-val
                                                     new-store2
                                                     )
                                                    ))))
)

      (letrec-exp (p-names b-vars p-bodies letrec-body)
                  (value-of letrec-body
                            (extend-env-rec* p-names b-vars p-bodies env)
                            store))

      (begin-exp (exp1 exps)
                 (letrec
                     ((value-of-begins
                       (lambda (e1 es store)
                         (cases answer (value-of e1 env store)
                                (an-answer (v1 new-store)
                                           (if (null? es)
                                               (an-answer v1 new-store)
                                               (value-of-begins (car es)
                                                                (cdr es)
                                                                new-store)
                                               ))))))
                   (value-of-begins exp1 exps store)))

      (newref-exp
       (exp1)
       (cases answer (value-of exp1 env store)
              (an-answer (v1 new-store)
                         (an-answer (ref-val (newref v1)) new-store)
                         )))

      (deref-exp
       (exp1)
       (cases answer (value-of exp1 env store)
              (an-answer (v1 new-store)
                       (let ((ref1 (expval->ref v1)))
                         (an-answer (deref ref1) new-store)))))

      (setref-exp
       (exp1 exp2)
       (cases answer (value-of exp1 env store)
              (an-answer (v1 new-store)
                         (cases answer (value-of exp2 env new-store)
                                (an-answer (v2 new-store2)
                                           (an-answer
                                            (begin
                                              (setref! (expval->ref v1) v2)
                                              (num-val 23))
                                            new-store)
                                           )))))
      )))

;; apply-procedure : Proc * ExpVal -> ExpVal
;;
;; uninstrumented version
;;   (define apply-procedure
;;    (lambda (proc1 arg)
;;      (cases proc proc1
;;        (procedure (bvar body saved-env)
;;          (value-of body (extend-env bvar arg saved-env))))))

;; instrumented version
(define apply-procedure
  (lambda (proc1 arg store)
    (cases proc proc1
      (procedure (var body saved-env)
                 (let ((r arg))
                   (let ((new-env (extend-env var r saved-env)))
                     (when (instrument-let)
                       (eopl:printf
                        "entering body of proc ~s with env =~%"
                        var)
                       (pretty-print (env->list new-env))
                       (eopl:printf "store =~%")
                       (pretty-print (store->readable (get-store-as-list)))
                       (eopl:printf "~%"))
                     (value-of body new-env store)))))))


;; store->readable : Listof(List(Ref,Expval))
;;                    -> Listof(List(Ref,Something-Readable))
(define store->readable
  (lambda (l)
    (map
     (lambda (p)
       (cons
        (car p)
        (expval->printable (cadr p))))
     l)))
