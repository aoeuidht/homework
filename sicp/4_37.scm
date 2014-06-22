#lang r5rs
#|
Exercise 4.37.  Ben Bitdiddle claims that the following method for generating
 Pythagorean triples is more efficient than the one in exercise 4.35. Is he 
correct? (Hint: Consider the number of possibilities that must be explored.)

(define (a-pythagorean-triple-between low high)
  (let ((i (an-integer-between low high))
        (hsq (* high high)))
    (let ((j (an-integer-between i high)))
      (let ((ksq (+ (* i i) (* j j))))
        (require (>= hsq ksq))
        (let ((k (sqrt ksq)))
          (require (integer? k))
          (list i j k))))))
|#

; I think he is right. Since it sqrt is a log-n algorithm, 
; but the k check is a n algorithm.