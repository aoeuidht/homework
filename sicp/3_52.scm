; Exercise 3.52.  Consider the sequence of expressions

(define sum 0)
(define (accum x)
  (set! sum (+ x sum))
  sum)
(define seq (stream-map accum (stream-enumerate-interval 1 20)))
(define y (stream-filter even? seq))
(define z (stream-filter (lambda (x) (= (remainder x 5) 0))
                         seq))
(stream-ref y 7)
(display-stream z)

; What is the value of sum after each of the above expressions is evaluated?
; What is the printed response to evaluating the stream-ref and display-stream expressions?
; Would these responses differ if we had implemented (delay <exp>) simply as (lambda () <exp>)
; without using the optimization provided by memo-proc ? Explain. 

; Answer
; let's do it in a stuipd way, list sum values
; 1  2  3  4  5   6   7   8   9   10   11   12   13   14   15   16   17   18   19   20
; 1  3  6  10 15  21  28  36  45  55   66   78   91   105  120  136  153  171  190  210  

; After
(define seq (stream-map accum (stream-enumerate-interval 1 20)))
; sum is 1

; after
(define y (stream-filter even? seq))
; sum is 3

; after
(define z (stream-filter (lambda (x) (= (remainder x 5) 0))
                         seq))
; sum is 6

; after
(stream-ref y 7)
; we should count 7 even numbers from 10 to 136,
; so the answer is 136.

(display-stream z)

; the stream is '(17 18 19 20)