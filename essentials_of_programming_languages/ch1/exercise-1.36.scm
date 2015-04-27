#lang racket

#|
Writeaproceduregsuchthatnumber-elementsfrompage23 could be defined as
(define number-elements
  (lambda (lst)
    (if (null? lst) ’()
        (g (list 0 (car lst)) (number-elements (cdr lst))))))
|#

(define (g node lst)
  (cons node
        (map (lambda (n)
               (cons (+ (car n) 1)
                     (cdr n)))
             lst)
        ))

(define number-elements
  (lambda (lst)
    (if (null? lst) '()
        (g (list 0 (car lst))
           (number-elements (cdr lst))))))


(number-elements '(10 9 8 7 6 5 4 3 2 1))