; Exercise 3.63.  Louis Reasoner asks why the sqrt-stream procedure was not written in the 
; following more straightforward way, without the local variable guesses:

(define (sqrt-stream x)
  (cons-stream 1.0
               (stream-map (lambda (guess)
                             (sqrt-improve guess x))
                           (sqrt-stream x))))

; Alyssa P. Hacker replies that this version of the procedure is considerably less
; efficient because it performs redundant computation. Explain Alyssa's answer. 
; Would the two versions still differ in efficiency if our implementation of delay used only
; (lambda () <exp>) without using the optimization provided by memo-proc (section 3.5.1)? 

; Answer
; the orginal 

(define (sqrt-stream x)
  (define guesses
    (cons-stream 1.0
                 (stream-map (lambda (guess)
                               (sqrt-improve guess x))
                             guesses)))
  guesses)

; Let's see how the sqrt-stream works while its running
; the procedure returns a cons at first invoke, a number and a promise, expand which 
; we can get (improve 1) and (improve #promise), and so on.

; so let's paint it out

; 1 #promise
;   (improve 1) (improve #promise)
;                        (improve 1) (improve #promise)
;                                             ......

; then you see that, when we ref the nth item of the result,
; it will try to improve the (n-1)th item.

; at the first implementation, the nth item and the n-1 th item are in diffrent
; environment, so the optmize to delay will never, so it will have to calc (n+1)*n/2 times
; instead of 1, so its less efficint than the 2nd implementation.

; if we imply delay to (lambda () <exp>), they will both be slow.



