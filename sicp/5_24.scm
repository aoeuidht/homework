#lang racket
#|
Exercise 5.24.  Implement cond as a new basic special form without reducing it to if.
 You will have to construct a loop that tests the predicates of successive cond clauses
 until you find one that is true, and then use ev-sequence to evaluate the actions of the clause. 
|#

ev-cond
(save continue)
(assign unev (op cond-body) (reg exp))

ev-loop
(test (op blank-cond-body) (reg unev))
(goto (label ev-done))
(assign exp (op cond-first-clause) (reg unev))
(save exp)
(assign exp (op cond-clause-predicate) (reg exp))
(assign continue (label cond-pred-chked))
(goto (label ev-dispatch))

cond-pred-chked
(save exp)
(test (op true?) (reg val))
(goto (label cond-pred-true))
(assign unev (op cond-rest-clause) (reg unev))
(goto (label ev-loop))

cond-pred-true
(assign continue (label ev-loop))
(goto (label ev-sequence))

ev-done
(restore continue)
(goto (reg continue))