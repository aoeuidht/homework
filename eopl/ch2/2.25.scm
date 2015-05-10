#lang eopl
;;; exercise 2.25

#|
Use cases to write max-interior, which takes a binary tree of
 integers (as in the preceding exercise) with at least one
 interior node and returns the symbol associated with an
 interior node with a maximal leaf sum.
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


(define (find-max a b c)
  (let ((r (if b (if (> (cdr a) (cdr b)) a b) a)))
    (if c (if (> (cdr r) (cdr c)) r c) r)))

(define (max-interior-wrapper bt)
  ;; return ((current-key . current-sum) . (max-key . max-sum))
  (cases bintree bt
         (leaf-node (num) (cons (cons 'leaf num) #f))
         (interior-node
          (key left right)
          (let ((lr (max-interior-wrapper left))
                (rr (max-interior-wrapper right)))
            (let ((cinfo 
                   (cons key (+ (cdar lr)
                                (cdar rr)))))
              (cons cinfo 
                    (find-max cinfo (cdr lr) (cdr rr)))
              )))))

(define (max-interior bt)
  (let ((rst (max-interior-wrapper bt)))
    ((if (cdr rst)
         cadr caar) rst)))

(define tree-1
  (interior-node 'foo (leaf-node 2) (leaf-node 3)))
(define tree-2
  (interior-node 'bar (leaf-node -1) tree-1))
(define tree-3
  (interior-node 'baz tree-2 (leaf-node 1)))

(display (max-interior tree-2))

(display (max-interior tree-3))

