#lang racket

#|
(sort/predicate pred loi)  returnsalistofelementssorted by the predicate.
|#

; sort/predicate: lambda X List -->  List
(define (sort/predicate pred loi)
  (s-wrapper pred loi '()))


; s-wrapper lambda X List X List --> List
(define (s-wrapper pred loi rst-lst)
  (if (null? loi)
      rst-lst
      (s-wrapper pred (cdr loi)
                 (insert-item pred (car loi) rst-lst))))


; insert-item lambda X Int X List --> List
(define (insert-item pred n loi)
    (if (null? loi)
      (cons n loi)
      (if (pred n (car loi))
          (cons n loi)
          (cons (car loi)
                (insert-item pred n (cdr loi)))
          )))

(sort/predicate < '(8 2 5 2 3))

(sort/predicate > '(8 2 5 2 3))