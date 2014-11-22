#|
Exercise 5.23. Extend the evaluator to handle derived expressions such as cond, let, and so on
(section 4.1.2). You may ``cheat'' and assume that the syntax transformers such as cond->if are
available as machine operations.28
|#

ev-cond
(save exp)
(save continue)
(assign continue (label ev-cond-if-done))
(assign exp (op cond->if) exp)
(goto (label eval-dispatch))
ev-cond-if-done
(assign val (const 'ok))
(restore exp)
(restore continue)

ev-let
(save env)
(save unev)
(assign unev (op copy-env))
(assign env unev)
(save argl)
(assign argl (op let-vars) (reg exp))
(save continue)
(save exp)

(assign continue (label ev-let-var-done))
ev-let-vars
(test (op blank-let-vars?) (reg argl))
(goto (label ev-let-body))
(assign exp (op first-var) (reg argl))
(assign unev (op var-name) (reg exp))
(assign exp (op var-exp) (reg exp))
(goto (label eval-dispatch))
ev-let-var-done
(assign env (op extend-environment)
              (reg unev) (reg val) (reg env))
(assign argl (op rest-vars) argl)
(goto (label ev-let-vars))
ev-let-body
(restore exp)
(assign argl (op let-body) (reg exp))
ev-let-body-loop
(test (op blank-let-body?) (reg argl))
(goto (label ev-let-body-done))
(assign exp (op first-body) (reg argl))
(assign continue ev-let-body-loop)
(goto (label eval-dispatch))
ev-let-body-done
(restore continue)
(restore argl)
(restore unev)
(restore env)
(goto (reg continue))
