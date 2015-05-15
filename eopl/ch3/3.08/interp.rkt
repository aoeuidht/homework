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

      (equal?-exp (exp1 exp2)
               (arith-compare-value-of = exp1 exp2 env))
      (greater?-exp (exp1 exp2)
               (arith-compare-value-of > exp1 exp2 env))
      (less?-exp (exp1 exp2)
               (arith-compare-value-of < exp1 exp2 env))
      
      )))


