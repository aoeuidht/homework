#lang racket
#|
Exercise 5.4.  Specify register machines that implement each of the following procedures.
 For each machine, write a controller instruction sequence and
 draw a diagram showing the data paths.

a. Recursive exponentiation:

(define (expt b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))

b. Iterative exponentiation:

(define (expt b n)
  (define (expt-iter counter product)
    (if (= counter 0)
        product
        (expt-iter (- counter 1) (* b product))))
  (expt-iter n 1))

|#

; answer a

(controller
 (assign continue (label expt-done))
 expt-loop
   (test (op =) (reg n) (cont 0))
   (branch (label base-caseh))
   ;
   (save continue)
   (save n)
   (assign n (op -) (reg n) (cont 1))
   (assign continue (label after-expt))
   (goto (label expt-loop))
 after-expt
   (restore n)
   (restore continue)
   (assign val (op *) (reg b) (reg val))
   (goto (reg continue))
 base-case
   (assign val (const 1))
   (goto (reg continue))
 fact-done)


; answer b

(controller
 (assign continue (label iter-done))
 (goto (label iter-invoke))
 ; here we start the iter sub-process, which using register n and p
 ; to remember 2 paramters of procedure expt-iter
 iter-start
   (test (op =) (reg n) (const 0))
   (goto (label continue)
   (assign (reg p) (op *) (reg b) (reg p))
   (assign (reg n) (op -) (reg n) (const 1))
   (goto (label inter-start))
 ; call the iter with default parameter
 iter-invoke
   (assign p (const 1))
   ; after we init the arguments, goto the sub procedure
   (goto (label iter-start))
 iter-done)
  