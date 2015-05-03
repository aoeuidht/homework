#lang racket
#|
Write a procedure path that takes an integer n and a binary 
search tree bst (page 10) that contains the integer n, and 
returns a list of lefts and rights showing how to find the node containing n. 
If n is found at the root, it returns the empty list.
|#

; path Int X BST -> List(of directions) | #f
(define (path n root)
  (cond
    ((null? root) #f)
    ((= n (car root)) '())
    (else (let ((lrst (path n (cadr root))))
            (if (list? lrst)
                (cons 'left lrst)
                (let ((rrst (path n (caddr root))))
                  (if (list? rrst)
                      (cons 'right rrst)
                      #f)))))))

(path 17 '(14 (7 () (12 () ()))
              (26 (20 (17 () ())
                      ())
                  (31 () ()))))
