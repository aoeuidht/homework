#lang eopl
(require racket/pretty)
(require eopl/tests/private/utils)

(require "data-structures.rkt")  ; for expval constructors
(require "lang.rkt")             ; for scan&parse
(require "interp.rkt")           ; for value-of-program

;; run : String -> ExpVal
(define run
  (lambda (string)
    (value-of-program (scan&parse string))))

(define equal-answer?
  (lambda (ans correct-ans)
    (equal? ans (sloppy->expval correct-ans))))

(define sloppy->expval 
  (lambda (sloppy-val)
    (cond
      ((number? sloppy-val) (num-val sloppy-val))
      ((boolean? sloppy-val) (bool-val sloppy-val))
      (else
       (eopl:error 'sloppy->expval 
                   "Can't convert sloppy value to expval: ~s"
                   sloppy-val)))))

(define-syntax-rule (check-run (name str res) ...)
  (begin
    (cond [(eqv? 'res 'error)
           (check-exn always? (lambda () (run str)))]
          [else
           (check equal-answer? (run str) 'res (symbol->string 'name))])
    ...))

;;;;;;;;;;;;;;;; tests ;;;;;;;;;;;;;;;;

(display (run "
let a = 3
in let p = proc (x) -(x,a) 
in let a=5
in -(a,(p 2))
"))


(display (run "
let a = 3
      in let p = proc (z) a
         in let f = proc (a) (p 0)
            in let a = 5
in (f a)
"))

(pretty-print (scan&parse "
let a = 3
      in let p = proc (z) a
         in let f = proc (a) (p 0)
            in let a = 5
in (f a)
"))

(pretty-print (scan&parse "8"))
