; Exercise 3.69. Write a procedure triples that takes three infinite streams, S, T, and U, 
; and produces the stream of triples (Si,Tj,Uk) such that i < j < k. Use triples to
; generate the stream of all Pythagorean triples of positive integers, i.e.,
; the triples (i,j,k) such that i < j and i2 + j2 = k2.

(define (triples s1 s2 s3)
  (cons-stream (list (map stream-car (list s1 s2 s3)))
               (itterleave (stream-map (lambda (x) (list (stream-car s1) (car x) (cdr x)))
                                       (pairs s2 s3))
                           (triples (map stream-cdr (list s1 s2 s3))))))