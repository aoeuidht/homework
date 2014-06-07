; Exercise 3.58.  Give an interpretation of the stream computed by the following procedure:

(define (expand num den radix)
  (cons-stream
   (quotient (* num radix) den)
   (expand (remainder (* num radix) den) den radix)))

; (Quotient is a primitive that returns the integer quotient of two integers.)
; What are the successive elements produced by (expand 1 7 10) ? What is produced by (expand 3 8 10) ? 

; Answer
; the expand procedure expand the `num/den based radix' to rational number
; so (expand 1 7 10) is 142857142... which is (1/7)
; and (expand 3 8 10) is 375000... which is exactly (3/8)
