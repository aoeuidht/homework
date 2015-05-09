#lang racket

(define (action-fail action reason)
  (error action reason))

(define (number->bintree n) `(,n () ()))

(define current-element car)

(define at-leaf? null?)

(define (move-to-left t)
  (if (at-leaf? t)
      (action-fail 'move-to-left 'met-leaf)
      (cadr t)))

(define (move-to-right t)
  (if (at-leaf? t)
      (action-fail 'move-to-right 'met-leaf)
      (caddr t)))

(define (insert-to-left n t)
  (list (current-element t)
        (if (at-leaf? (move-to-left t))
            (number->bintree n)
            (list n (move-to-left t) '()))
        (move-to-right t)))

(define (insert-to-right n t)
  (list (current-element t)
        (move-to-left t)
        (if (at-leaf? (move-to-right t))
            (number->bintree n)
            (list n '() (move-to-right t)))
        ))

(number->bintree 13)
(define t1 (insert-to-right
            14
            (insert-to-left
             12
             (number->bintree 13))))

t1

(move-to-left t1)

(current-element (move-to-left t1))

(at-leaf? (move-to-right (move-to-left t1)))

(insert-to-left 15 t1)