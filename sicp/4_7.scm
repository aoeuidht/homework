#| Exercise 4.7. Let* is similar to let, except that the bindings of the let variables
 are performed sequentially from left to right, and each binding is made in an environment
 in which all of the preceding bindings are visible. For example
(let* ((x 3)
       (y (+ x 2))
       (z (+ x y 5)))
  (* x z))
returns 39. Explain how a let* expression can be rewritten as a set of nested let expressions,
 and write a procedure let*->nested-lets that performs this transformation.
 If we have already implemented let (exercise 4.6) and we want to extend the evaluator
 to handle let*, is it sufficient to add a clause to eval whose action is
(eval (let*->nested-lets exp) env)
or must we explicitly expand let* in terms of non-derived expressions?
|#

(define (let*->nested-lets exp)
  (define (let*->nested-lets-wrapper variables body)
    (list 'let (list (car variables))
          (if (null? (cdr variables))
              body
              (let*->nested-lets-wrapper (cdr variables) body))))
  (let*->nested-lets-wrapper (cadr exp) (caddr exp)))

(let*->nested-lets '(let* ((x 3)
                           (y (+ x 2))
                           (z (+ x y 5)))
                      (* x z)))


; let's expand the let* using lambda
(let-combination '(let* ((x 3)
                           (y (+ x 2))
                           (z (+ x y 5)))
                      (* x z)))

; then we got ((lambda (x y z) (* x z)) (3) ((+ x 2)) ((+ x y 5)))
((lambda (x y z)
   (* x z))
 (3)
 (+ x 2))
 (+ x y 5)))

; while eval calculating the parameters, it can't find the defination of x and y,
; then there will be panic.