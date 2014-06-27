#lang racket
#|
Exercise 4.47.  Louis Reasoner suggests that, since a verb phrase is either a verb or 
a verb phrase followed by a prepositional phrase, it would be much more straightforward to
 define the procedure parse-verb-phrase as follows (and similarly for noun phrases):

(define (parse-verb-phrase)
  (amb (parse-word verbs)
       (list 'verb-phrase
             (parse-verb-phrase)
             (parse-prepositional-phrase))))

Does this work? Does the program's behavior change if we interchange the order of expressions in the amb? 
|#

; Answer
#|
No. This will not work.
In the implementation of parse-verb-phrase, if we got a verb+prepositional, the first
branch will fail, and the 2nd will also fail, because after verb already poped in the 1st
branch, so there is only a prepositional left.

Changing the order will not help at this case.
|#
