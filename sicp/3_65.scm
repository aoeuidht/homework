; Exercise 3.65.  Use the series

; to compute three sequences of approximations to the natural logarithm of 2,
; in the same way we did above for . How rapidly do these sequences converge? 

(define (ln2-summands n coe)
  (cons-stream (/ coe n)
               (ln2-summands (+ n 1) (* coe -1))))

(define ln2 (ln2-summands 1 1))