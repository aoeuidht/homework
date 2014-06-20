#lang racket
#|
Exercise 4.36.  Exercise 3.69 discussed how to generate the stream of all
 Pythagorean triples, with no upper bound on the size of the integers to be
 searched. Explain why simply replacing an-integer-between by an-integer-starting-from
 in the procedure in exercise 4.35 is not an adequate way to generate arbitrary Pythagorean triples.
 Write a procedure that actually will accomplish this. (That is, write a procedure for which repeatedly
 typing try-again would in principle eventually generate all Pythagorean triples.) 
|#

;  Explain why simply replacing an-integer-between by an-integer-starting-from
; in the procedure in exercise 4.35 is not an adequate way to generate arbitrary Pythagorean triples.

; Answer
; Because it will try to travel all values of k in the last an-integer-starting-from after amb give the
; 1st and 2nd value for i, j

; to avoid this, we have to make the amb end at j and k, so let's just assume i is the biggest bound.
; and use the rule `a-b<c` in triple


(define (pythagorean-triple)
  (let ((i (an-integer-starting-from 5)))
    (let ((j (an-integer-between 4 i)))
      (let ((k (an-integer-between (- i j) i)))
        (require (= (+ (* i i) (* j j)) (* k k)))
        (list i j k)))))