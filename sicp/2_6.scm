#lang racket
; Exercise 2.6. In case representing pairs as procedures wasn't mind-boggling enough, consider that,
; in a language that can manipulate procedures, we can get by without numbers
; (at least insofar as nonnegative integers are concerned) by implementing 0 and the operation of adding 1 as
(define zero (lambda (f) (lambda (x) x)))
(define (add-1 n)
  (lambda (f) (lambda (x) (f ((n f) x)))))
; This representation is known as Church numerals, after its inventor,
; Alonzo Church, the logician who invented the lambda calculus.

; Define one and two directly (not in terms of zero and add-1).
; (Hint: Use substitution to evaluate (add-1 zero)). 
; Give a direct definition of the addition procedure + (not in terms of repeated application of add-1).

; Answer
; seems that zero is return a function which
; -- takes a procedure as argument, and
; -- return a procedure, that will output f(x) 0 times with input x
; so `one` should be return f(x) 
(define one (lambda (f) (lambda (x) (f x))))
(define two (lambda (f) (lambda (x) ( f (f x)))))
(define three (lambda (f) (lambda (x) (f (f (f x))))))

; testing
(define (test-func x)
  (+ x 3))

((zero test-func) 4)
((one test-func) 4)
((two test-func) 4)
((three test-func) 4)

; try add-1
(((add-1 one) test-func) 4)

; now we can apply the procedure +
(define (f+ a n)
  (lambda (f)
    (lambda (x)
      ((a f) ((n f) x)))))

(((f+ two two) test-func) 4)