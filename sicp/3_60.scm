; Exercise 3.60. With power series represented as streams of coefficients as in exercise 3.59,
; adding series is implemented by add-streams. Complete the definition
; of the following procedure for multiplying series:
; (define (mul-series s1 s2)
;   (cons-stream <??> (add-streams <??> <??>)))

; Answer
; the key point of this problem is, we have to add all the values with sawe power together
; so let's take 2 streams
; a0 a1 a2 a3 a4 a5
; b0 b1 b2 b3 b4 b5
; multiply them, we can expand it to
; a0 * (b0 b1 b2 b3 b4) + (a1 a2 a3 a4) * (b0 b1 b2 b3 b4)
; the first part a0 * b..., we got a stream whose 1st item has power 0,
; but the 2nd part, whose 1st item has power 1, can't be added to the first part directly,
; so we have to expand the first part to
; a0 * b0 + a0 * (b1 b2 b3 b4)


(define (mul-series s1 s2)
   (cons-stream (* (stream-car s1) (stream-car s2)
                   (add-streams (scrale-stream (stream-cdr s2) (stream-car s1))
                                (mul-series (stream-cdr s1)
                                            (stream-cdr s2))
                                )))