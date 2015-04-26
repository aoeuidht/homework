#lang racket

#|
(sort loi) returns a list of the elements of loi in ascending order.
|#

; sort List --> List

(define (sort loi)
  (sort-wrapper loi '()))

; sort-wrapper List X List --> List
(define (sort-wrapper loi rst-lst)
  (if (null? loi)
      rst-lst
      (sort-wrapper (cdr loi)
                    (insert-item (car loi) rst-lst))))

; insert-item Int X List --> List
(define (insert-item n loi)
  (if (null? loi)
      (cons n loi)
      (if (> n (car loi))
          (cons (car loi)
                (insert-item n (cdr loi)))
          (cons n loi))))

(display (sort '(1 3 6 2 3 6 2)))