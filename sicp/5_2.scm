#lang racket
#|
Exercise 5.2. Use the register-machine language to describe the iterative factorial machine of exercise 5.1.
|#

(controller
 (assign c (const 1))
 (assign p (const 1))
 test-n
 (test (op >) (reg c) (reg n))
 (branch (label fac-done))
 (assign p (op *) (reg p) (reg c))
 (assign c (op +) (reg c) (const 1))
 (goto (label test-n))
 fac-done)