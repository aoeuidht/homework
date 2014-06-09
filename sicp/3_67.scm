; Exercise 3.67. Modify the pairs procedure so that (pairs integers integers) will
; produce the stream of all pairs of integers (i,j) (without the condition i < j).
; Hint: You will need to mix in an additional stream.

; Answer
; we split the streams into 4 parts

(define (interleave s1 s2 s3)
  (if (stream-null? s1)
      (interleave s2 s3 s1)
      (cons-stream (stream-car s1)
                   (interleave s2 s3 (stream-cdr s1)))))

(define (pairs s t)
  (cons-stream
   (list (stream-car s) (stream-car t))
   (interleave
    (stream-map (lambda (x) (list (stream-car s) x))
                (stream-cdr t))
    (pairs (stream-cdr s) (stream-cdr t))
    (stream-map (lambda (x) (list x (stream-car t)))
                (stream-cdr s)))))