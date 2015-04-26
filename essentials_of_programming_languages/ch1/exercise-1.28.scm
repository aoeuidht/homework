#lang racket

#|
(merge loi1 loi2) where loi1 and loi2 arelistsofintegers that
 are sorted in ascending order, returns a sorted
 list of all the integers in loi1 and loi2.
|#

; merge List X List --> List


(define (merge loi1 loi2)
  (cond ((null? loi1) loi2)
        ((null? loi2) loi1)
        (else (let ((c1 (car loi1))
                    (c2 (car loi2)))
                (if (> c1 c2)
                    (cons c2 (merge loi1 (cdr loi2)))
                    (cons c1 (merge (cdr loi1) loi2)))))))

(display (merge '(1 4) '(1 2 8)))