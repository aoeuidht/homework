#lang racket
; Exercise 2.22. Louis Reasoner tries to rewrite the first square-list procedure of exercise 2.21 so that
; it evolves an iterative process:
(define (square-list-e items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (cons (square (car things))
                    answer))))
  (iter items '()))
;Unfortunately, defining square-list this way produces the answer list in the reverse order of the one
; a desired. Why?

; Answer
; the problem is at these lines:
;               (cons (square (car things))
;                     answer))))
; in the iter, `answer` is the result of the previously handled list, here cons put it back,
; so we got a reverse list

; Louis then tries to fix his bug by interchanging the arguments to cons:
(define (square-list-ee items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (cons answer
              (square (car things))))))
  (iter items '()))

; This doesn't work either. Explain.

; Answer:
; the error is what we should got is
; (answer_0, answer_1, ..., answer_n, (car things))
; but we got
; (answer, (car things))

; if you want the correct answer, use the `extend` method before (since there is no permitive `append` operation in scheme)
(define (square x) (* x x))
(define (square-list items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (append answer (list (square (car things)))))))
  (iter items '()))

(square-list (list 1 2 3 4))
