#lang racket
; Exercise 2.66. Implement the lookup procedure for the case where the set of records is structured
; as a binary tree, ordered by the numerical values of the keys.
(define (lookup given-key set-tree)
  (if (null? set-tree)
      false
      (let ((ck (key (entry set-tree))))
        (cond ((= ck given-key) (value (entry set-tree)))
              ((> ck given-key) (lookup given-key (left-branch set-tree)))
              (else (lookup given-key (right-branch set-tree)))))))
        
  