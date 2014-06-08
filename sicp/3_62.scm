; Exercise 3.62. Use the results of exercises 3.60 and 3.61 to define a procedure
; div-series that divides two power series. Div-series should work for any two series, 
; provided that the denominator series begins with a nonzero constant term. (If the 
; denominator has a zero constant term, then div-series should signal an error.) 
; Show how to use div-series together with the result of exercise 3.59 to generate the power series for tangent.

; Answer
; if we want to calc a / b, just expand it to a * (1 / b)

(define (div-series s0 s1)
  (if (= (stream-car s1) 0)
      (error "cant div stream whoso constant equals zero")
      (let ((s1-c1 (scale-stream s1 (/ 1.0 (stream-car s1)))))
        (scale-stream (mul-stream s0 (invert-unit-series s1-c1))
                      (stream-car s1)))))