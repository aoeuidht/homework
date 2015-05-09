#lang racket

(define (action-fail action reason)
  (error action reason))

(define (number->bintree n) `((,n () ())
                              ()))

(define current-element caar)

(define (at-leaf? t) 
  (or (null? t)
      (null? (car t)))
  )

(define (at-root? t)
  (null? (cadr t)))

(define (move-to-left t)
  (if (at-leaf? t)
      (action-fail 'move-to-left 'met-leaf)
      (list (cadar t)
            (cons (car t) (cadr t)))))

(define (move-to-right t)
  (if (at-leaf? t)
      (action-fail 'move-to-right 'met-leaf)
      (list (caddar t)
            (cons (car t) (cadr t)))
      ))

(define (move-up t)
  (if (at-root? t)
      (action-fail 'move-up 'met-root)
      (list (cadr t) (cddr t))))

(define (insert-to-left n t)
  (list
   (list (current-element t)
         (if (at-leaf? (move-to-left t))
             (car (number->bintree n))
             (list n (car (move-to-left t)) '()))
         (car (move-to-right t)))
   (cadr t)))

(define (insert-to-right n t)
  (list
   (list (current-element t)
         (car (move-to-left t))
         (if (at-leaf? (move-to-right t))
             (car (number->bintree n))
             (list n '() (car (move-to-right t))))
        )
   (cadr t)))

(define t0 (number->bintree 13))
t0
(at-root? t0)
(insert-to-right 3 t0)
(insert-to-left 5 t0)
(move-up (move-to-left (insert-to-left 3 t0)))

(define t1 (insert-to-right
            14
            (insert-to-left
             12
             (number->bintree 13))))

t1
(at-root? t1)
(move-to-left t1)

(current-element (move-to-left t1))

(at-leaf? (move-to-right (move-to-left t1)))

(insert-to-left 15 t1)