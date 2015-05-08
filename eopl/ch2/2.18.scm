#lang racket

(define (number->sequence n)
  (list n '() '()))

(define current-element car)
(define left-list cadr)
(define right-list caddr)

(define (at-left-end? s)
  (null? (cadr s)))

(define (at-right-end? s)
  (null? (caddr s)))

(define (action-fail action reason)
  (error action reason))

(define (move-to-left s)
  (if (at-left-end? s)
      (action-fail 'move-to-left 'meet-left-end)
      (list (car (left-list s))
            (cdr (left-list s))
            (cons (current-element s) (right-list s)))))

(define (move-to-right s)
  (if (at-right-end? s)
      (action-fail 'move-to-right 'meet-right-end)
      (list (car (right-list s))
            (cons (current-element s) (left-list s))
            (cdr (right-list s)))))

(define (insert-to-left n s)
  (list (current-element s)
        (cons n (left-list s))
        (right-list s)))

(define (insert-to-right n s)
  (list (current-element s)
        (left-list s)
        (cons n (right-list s))))
      
(number->sequence 7)
(current-element '(6 (5 4 3 2 1) (7 8 9)))
(move-to-left '(6 (5 4 3 2 1) (7 8 9)))
(move-to-right '(6 (5 4 3 2 1) (7 8 9)))
(insert-to-left 13 '(6 (5 4 3 2 1) (7 8 9)))
(insert-to-right 13 '(6 (5 4 3 2 1) (7 8 9)))