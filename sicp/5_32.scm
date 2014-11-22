#lang racket
#|
Exercise 5.32.  Using the preserving mechanism, the compiler will avoid saving and restoring
 env around the evaluation of the operator of a combination in the case where the operator
 is a symbol. We could also build such optimizations into the evaluator.
 Indeed, the explicit-control evaluator of section 5.4 already
 performs a similar optimization, by treating combinations with no operands as a special case.

a. Extend the explicit-control evaluator to recognize as a separate class of expressions
 combinations whose operator is a symbol, and to take advantage of this fact in evaluating such expressions.

b. Alyssa P. Hacker suggests that by extending the evaluator to recognize more and more
 special cases we could incorporate all the compiler's optimizations, and that this
 would eliminate the advantage of compilation altogether. What do you think of this idea? 

|#

#|
the original ev-appl-operand-loop
ev-appl-operand-loop
  (save argl)
  (assign exp (op first-operand) (reg unev))
  (test (op last-operand?) (reg unev))
  (branch (label ev-appl-last-arg))
  (save env)
  (save unev)
  (assign continue (label ev-appl-accumulate-arg))
  (goto (label eval-dispatch))

ev-appl-accumulate-arg
  (restore unev)
  (restore env)
  (restore argl)
  (assign argl (op adjoin-arg) (reg val) (reg argl))
  (assign unev (op rest-operands) (reg unev))
  (goto (label ev-appl-operand-loop))

ev-appl-last-arg
  (assign continue (label ev-appl-accum-last-arg))
  (goto (label eval-dispatch))
ev-appl-accum-last-arg
  (restore argl)
  (assign argl (op adjoin-arg) (reg val) (reg argl))
  (restore proc)
  (goto (label apply-dispatch))

|#


#|
change it to:
ev-appl-operand-loop
  (save argl)
  (assign exp (op first-operand) (reg unev))
  (test (op last-operand?) (reg unev))
  (branch (label ev-appl-last-arg))
  (test (op symbol?) (reg exp))
  (branch (label ev-appl-arg-symbol)
  (save env)
  (save unev)
  (assign continue (label ev-appl-accumulate-arg))
  (goto (label eval-dispatch))
ev-appl-arg-symbol
  (assign argl (op adjoin-arg) (reg exp) (reg argl))
  (goto (label ev-appl-operand-loop))

ev-appl-accumulate-arg
  (restore unev)
  (restore env)
  (restore argl)

ev-appl-acc-symbol
  (assign argl (op adjoin-arg) (reg val) (reg argl))
  (assign unev (op rest-operands) (reg unev))
  (goto (label ev-appl-operand-loop))

ev-appl-last-arg
  (test (op symbol?) (reg exp))
  (branch (label ev-appl-last-arg-symbol))
  (assign continue (label ev-appl-accum-last-arg))
  (goto (label eval-dispatch))
ev-appl-last-arg-symbol
  (assign argl (op adjoin-arg) (reg exp) (reg argl))
  (restore proc)
  (goto (label apply-dispatch))
ev-appl-accum-last-arg
  (restore argl)
  (assign argl (op adjoin-arg) (reg val) (reg argl))
  (restore proc)
  (goto (label apply-dispatch))

|#