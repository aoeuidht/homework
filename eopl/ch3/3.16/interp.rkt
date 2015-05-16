#lang eopl

;; interpreter for the LET language.  The \commentboxes are the
;; latex code for inserting the rules into the code in the book.
;; These are too complicated to put here, see the text, sorry.

(require "lang.rkt")
(require "data-structures.rkt")
(require "environments.rkt")

(provide value-of-program value-of)

;;;;;;;;;;;;;;;; the interpreter ;;;;;;;;;;;;;;;;

;; value-of-program : Program -> ExpVal
;; Page: 71
(define value-of-program 
  (lambda (pgm)
    (cases program pgm
      (a-program (exp1)
                 (value-of exp1 (init-env))))))

(define (arith-value-of op operator-exp operand-exp env)
  (let ((val1 (value-of operator-exp env))
        (val2 (value-of operand-exp env)))
    (let ((num1 (expval->num val1))
          (num2 (expval->num val2)))
      (num-val (op num1 num2)))))

(define (arith-compare-value-of op operator-exp operand-exp env)
  (let ((val1 (value-of operator-exp env))
        (val2 (value-of operand-exp env)))
    (let ((num1 (expval->num val1))
          (num2 (expval->num val2)))
      (bool-val (op num1 num2)))))

;; value-of : Exp * Env -> ExpVal
;; Page: 71
(define (value-of-bool-exp exp env)
  (cases bool-exp exp
         (unary-bool-exp
          (op exp1)
          (let ((val1 (value-of exp1 env)))
            (bool-val
             (cond
              [(equal? op "zero?") (= 0 (expval->num val1))]
              [(equal? op "null?") (null? (expval->list val1))]
              [else (eopl:error 'invalid-unary-bool-exp-op op)]))))
         (binary-bool-exp
          (op exp1 exp2)
          (let ((val1 (value-of exp1 env))
                (val2 (value-of exp2 env)))
            (bool-val
             ((cond
                [(equal? op "equal?") =]
                [(equal? op "greater?") >]
                [(equal? op "less?") <]
                [else (eopl:error 'invalid-banary-bool-exp-op op)])
              (expval->num val1)
              (expval->num val2)
              ))))))

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
      
      ;;\commentbox{\ma{\theifspec}}
      (if-exp (exp1 exp2 exp3)
              (let ((val1 (value-of-bool-exp exp1 env)))
                (if (expval->bool val1)
                    (value-of exp2 env)
                    (value-of exp3 env))))

      (b-exp (exp1)
             (value-of-bool-exp exp1 env))

      ;;\commentbox{\ma{\theletspecsplit}}
      (let-exp (vars exps body)       
               (let ((vals (map (lambda (exp1) (value-of exp1 env))
                                exps)))
                 (value-of body
                           (batch-extend-env vars vals env))))
      
      ;; Add the minus operator
      (minus-exp (exp1)
                 (let ((val1 (value-of exp1 env)))
                   (num-val (- 0 (expval->num val1)))))

      (add-exp (exp1 exp2)
               (arith-value-of + exp1 exp2 env))
      
      (mul-exp (exp1 exp2)
               (arith-value-of * exp1 exp2 env))
      
      (div-exp (exp1 exp2)
               (arith-value-of / exp1 exp2 env))

      ;; the list related
      (empty-list-exp () (list-val '()))
      
      (cons-exp (exp1 exp2)
                (list-val
                 (cons (value-of exp1 env)
                       (expval->list (value-of exp2 env)))))

      (car-exp (exp1)
               (car (expval->list (value-of exp1 env))))
      (cdr-exp (exp1)
               (list-val  (cdr (expval->list (value-of exp1 env)))))

      ;; the list expression
      (list-exp (exp1)
                (if (null? exp1)
                    (list-val '())
                    (list-val
                      (cons (value-of (car exp1) env)
                            (expval->list
                             (value-of (list-exp (cdr exp1))
                                       env)))))
                )
      ;; cond expression
      (cond-exp (exp1 exp2)
                (if (null? exp1)
                    (eopl:error 'cond-exp-fail "no-cond-satisfied")
                    (if (expval->bool (value-of-bool-exp (car exp1) env))
                        (value-of (car exp2) env)
                        (value-of (cond-exp (cdr exp1) (cdr exp2)) env)
                        )
                    ))
      )))


