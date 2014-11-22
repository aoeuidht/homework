#lang racket
#|
Exercise 5.31.  In evaluating a procedure application, the explicit-control evaluator always saves and restores the env
 register around the evaluation of the operator, saves and restores env around the evaluation of each
 operand (except the final one), saves and restores argl around the evaluation of each operand,
 and saves and restores proc around the evaluation of the operand sequence.
 For each of the following combinations, say which of these save and restore
 operations are superfluous and thus could be eliminated by the compiler's preserving mechanism:

(f 'x 'y)

((f) 'x 'y)

(f (g 'x) y)

(f (g 'x) 'y)


; answer

Here is how ev-application works:
ev-appl-did-operator
  (restore unev)                  ; the operands
  (restore env)
  (assign argl (op empty-arglist))
  (assign proc (reg val))         ; the operator
  (test (op no-operands?) (reg unev))
  (branch (label apply-dispatch))
  (save proc)


env holds the environment, proc holds operands, so(I got some hint from http://community.schemewiki.org/?sicp-ex-5.31)

(f 'x 'y)  needs to save nothing, becaule all operands are quoted, so env doesn't change and no other proc necessary

((f) 'x 'y)  all operands are quoted, so env needn't; 

(f (g 'x) y) the 1st operand is a compound-procedure, so saving for proc, argl are needed; also env, because we have to read y from env

(f (g 'x) 'y) the 1st operand is a compound-procedure, so saving for proc, argl are needed; env is not, because y is quoted
|#