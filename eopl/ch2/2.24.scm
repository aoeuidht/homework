#lang eopl
;;; exercise 2.23

#|
Implement a bintree-to-list procedure for binary trees, so that (bintree-to-list (interior-node ’a (leaf-node 3) (leaf-node 4))) returns the list
 (interior-node
    a
    (leaf-node 3)
    (leaf-node 4))
|#
(require eopl/tests/private/utils)

(define-datatype s-list s-list?
  (an-s-list
   (sexps (list-of s-exp?))))

(define list-of
  (lambda (pred)
    (lambda (val)
      (or (null? val)
          (and (pair? val)
               (pred (car val))
               ((list-of pred) (cdr val)))))))

(define-datatype s-exp s-exp?
  (symbol-s-exp
   (sym symbol?))
  (s-list-s-exp
   (slst s-list?)))

(define identifier?
  (lambda (id-name)
    (and (symbol? id-name)
         (not (eq? id-name 'labmda)))))

(define-datatype bintree bintree?
  (leaf-node
   (num integer?))
  (interior-node
   (key symbol?)
   (left bintree?)
   (right bintree?)))

(define (bintree-to-list bt)
  (cases bintree bt
         (leaf-node (n) (list 'leaf-node n))
         (interior-node
          (key left right)
          (list 'interior-node key
                (bintree-to-list left)
                (bintree-to-list right)))
         ))

(display (bintree-to-list (interior-node 'a (leaf-node 3) (leaf-node 4))))
