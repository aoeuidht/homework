#lang eopl

;; data structures for letrec-lang.

(require "lang.rkt")                  ; for expression?

(provide (all-defined-out))           ; too many things to list

;;;;;;;;;;;;;;;; expressed values ;;;;;;;;;;;;;;;;

;;; an expressed value is either a number, a boolean or a procval.

(define-datatype expval expval?
  (num-val
   (value number?))
  (bool-val
   (boolean boolean?))
  (proc-val
   (proc proc?))
  (list-val
   (list (list-of expval?)))
  )

;;; extractors:

;; expval->num : ExpVal -> Int
(define expval->num
  (lambda (v)
    (cases expval v
      (num-val (num) num)
      (else (expval-extractor-error 'num v)))))

;; expval->bool : ExpVal -> Bool
(define expval->bool
  (lambda (v)
    (cases expval v
      (bool-val (bool) bool)
      (else (expval-extractor-error 'bool v)))))

;; expval->proc : ExpVal -> Proc
(define expval->proc
  (lambda (v)
    (cases expval v
      (proc-val (proc) proc)
      (else (expval-extractor-error 'proc v)))))

(define (expval->list lst)
  (cases expval lst
         (list-val (list) list)
         (else (expval-extractor-error 'list lst))))


(define expval-extractor-error
  (lambda (variant value)
    (eopl:error 'expval-extractors "Looking for a ~s, found ~s"
                variant value)))

;;;;;;;;;;;;;;;; procedures ;;;;;;;;;;;;;;;;

;; proc? : SchemeVal -> Bool
;; procedure : Var * Exp * Env -> Proc
(define-datatype proc proc?
  (procedure
   (bvar symbol?)
   (body expression?)
   (env environment?)))

;; Page: 86
(define-datatype environment environment?
  (empty-env)
  (extend-env
   (bvar symbol?)
   (bval expval?)
   (saved-env environment?))
  (extend-env-rec
   (id symbol?)
   (bvar symbol?)
   (body expression?)
   (saved-env environment?)))

;;; the continution data-type
(define-datatype continution continution?
  (end-cont)
  (zero1-cont
   (cont continution?))
  (let-exp-cont
   (var symbol?)
   (body expression?)
   (env environment?)
   (cont continution?))
  (if-test-cont
   (exp2 expression?)
   (exp3 expression?)
   (env environment?)
   (cont continution?))
  (diff1-cont
   (exp2 expression?)
   (env environment?)
   (cont continution?))
  (diff2-cont
   (val1 expval?)
   (cont continution?))
  (rator-cont
   (rand expression?)
   (env environment?)
   (cont continution?))
  (rand-cont
   (rator expval?)
   (cont continution?))
  (list-cdr-cont
   (exp expression?)
   (env environment?)
   (cont continution?))
  (list-car-cont
   (val expval?)
   (cont continution?))
  (car-cont
   (cont continution?))
  (cdr-cont
   (cont continution?))
  )
