#lang eopl
(require racket/pretty)

;; builds environment interface, using data structures defined in
;; data-structures.scm. 

(require "data-structures.rkt")

(provide init-env empty-env extend-env apply-env batch-extend-env batch-extend-env-rec)

;;;;;;;;;;;;;;;; initial environment ;;;;;;;;;;;;;;;;

;; init-env : () -> Env
;; usage: (init-env) = [i=1, v=5, x=10]
;; (init-env) builds an environment in which i is bound to the
;; expressed value 1, v is bound to the expressed value 5, and x is
;; bound to the expressed value 10.
;; Page: 69

(define init-env 
  (lambda ()
    (extend-env 
     'i (num-val 1)
     (extend-env
      'v (num-val 5)
      (extend-env
       'x (num-val 10)
       (empty-env))))))

;;;;;;;;;;;;;;;; environment constructors and observers ;;;;;;;;;;;;;;;;

;; Page: 86
(define apply-env
  (lambda (env search-sym)
    (cases environment env
      (empty-env ()
                 (eopl:error 'apply-env "No binding for ~s" search-sym))
      (extend-env (var val saved-env)
                  (if (eqv? search-sym var)
                      val
                      (apply-env saved-env search-sym)))
      (extend-env-rec (proc-list saved-env)
                      (let ((proc-info (search-proc-list search-sym
                                                         proc-list
                                                         env)))
                        (if proc-info
                            proc-info
                            (apply-env saved-env search-sym)
                            )
                        ))
      )))

(define (search-proc-list search-sym proc-list env)

  (if (null? proc-list)
      #f
      (cases proc-info (car proc-list)
             (a-proc (id bvars body)
                     (if (eq? id search-sym)
                         (proc-val (procedure bvars body env))
                         (search-proc-list search-sym (cdr proc-list) env)
                         )
                     )
             (else #f))
      )
  )

(define (batch-extend-env syms vals old-env)
  (if (null? syms)
      old-env
      (batch-extend-env
       (cdr syms) (cdr vals)
       (extend-env (car syms) (car vals)
                   old-env))))

(define (batch-extend-env-rec p-names b-vars-list p-body-list env)
  (let ((proc-list (map (lambda (id bvars body) (a-proc id bvars body))
                        p-names b-vars-list p-body-list)))
    (extend-env-rec proc-list env)
    ))
