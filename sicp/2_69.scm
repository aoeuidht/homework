#lang racket
(define (make-leaf symbol weight)
  (list 'leaf symbol weight))
(define (leaf? object)
  (eq? (car object) 'leaf))
(define (symbol-leaf x) (cadr x))
(define (weight-leaf x) (caddr x))

(define (make-code-tree left right)
  (list left
        right
        (append (symbols left) (symbols right))
        (+ (weight left) (weight right))))

(define (left-branch tree) (car tree))
(define (right-branch tree) (cadr tree))
(define (symbols tree)
  (if (leaf? tree)
      (list (symbol-leaf tree))
      (caddr tree)))
(define (weight tree)
  (if (leaf? tree)
      (weight-leaf tree)
      (cadddr tree)))

(define (decode bits tree)
  (define (decode-1 bits current-branch)
    (if (null? bits)
        '()
        (let ((next-branch
               (choose-branch (car bits) current-branch)))
          (if (leaf? next-branch)
              (cons (symbol-leaf next-branch)
                    (decode-1 (cdr bits) tree))
              (decode-1 (cdr bits) next-branch)))))
  (decode-1 bits tree))
(define (choose-branch bit branch)
  (cond ((= bit 0) (left-branch branch))
        ((= bit 1) (right-branch branch))
        (else (error "bad bit -- CHOOSE-BRANCH" bit))))

(define (adjoin-set x set)
  (cond ((null? set) (list x))
        ((< (weight x) (weight (car set))) (cons x set))
        (else (cons (car set)
                    (adjoin-set x (cdr set))))))

(define (make-leaf-set pairs)
  (if (null? pairs)
      '()
      (let ((pair (car pairs)))
        (adjoin-set (make-leaf (car pair)
                               (cadr pair)) ; frequency
                    (make-leaf-set (cdr pairs))))))

(define (msg-in-tree msg tree)
  (cond ((null? tree) #f)
        ((leaf? tree) (eq? (symbol-leaf tree) msg))
        (else (memq msg (symbols tree)))))
(define (encode-symbol msg tree)
  (define (encode-symbol1 prefix msg tree)
    (cond ((null? tree) (error "bad tree -- maybe invalid message"))
          ((eq? #f (msg-in-tree msg tree)) #f)
          ((leaf? tree) prefix)
          ((msg-in-tree msg (left-branch tree)) (encode-symbol1 (append prefix '(0)) msg (left-branch tree)))
          (else (encode-symbol1 (append prefix '(1)) msg (right-branch tree)))))
  (encode-symbol1 '() msg tree))

(define (encode message tree)
  (if (null? message)
      '()
      (append (encode-symbol (car message) tree)
              (encode (cdr message) tree))))

; Encode-symbol is a procedure, which you must write, that returns the list of bits that encodes a given symbol
; according to a given tree. You should design encode-symbol so that it signals an error
; if the symbol is not in the tree at all.
; Test your procedure by encoding the result you obtained in exercise 2.67 with the sample tree
; and seeing whether it is the same as the original sample message.

(define sample-tree
  (make-code-tree (make-leaf 'A 4)
                  (make-code-tree
                   (make-leaf 'B 2)
                   (make-code-tree (make-leaf 'D 1)
                                   (make-leaf 'C 1)))))
(define sample-message '(0 1 1 0 0 1 0 1 0 1 1 1 0))
(encode-symbol 'A sample-tree)
(encode-symbol 'B sample-tree)
(encode-symbol 'C sample-tree)
(encode-symbol 'D sample-tree)

(encode '(A D A B B C A) sample-tree)

(encode (decode sample-message sample-tree) sample-tree)

; Exercise 2.69. The following procedure takes as its argument a list of symbol-frequency pairs
; (where no symbol appears in more than one pair) and generates a Huffman encoding tree according to the Huffman algorithm.
;(define (generate-huffman-tree pairs)
;  (successive-merge (make-leaf-set pairs)))

; Make-leaf-set is the procedure given above that transforms the list of pairs 
; into an ordered set of leaves. Successive-merge is the procedure you must write, 
; using make-code-tree to successively
; merge the smallest-weight elements of the set until there is only one element left, 
; which is the desired Huffman tree. (This procedure is slightly tricky, but not really complicated. 
; If you find yourself designing a complex procedure, then you are almost certainly doing something wrong. 
; You can take significant advantage of the fact that we are using an ordered set representation.)


; Answer
; To make a huffman tree, you should merge 2 smallest weight leafs/trees into a new tree
; so to build a huffman tree, we have to do 2 steps recursivly:
; 1. the first 2 leafs/trees to one
; 2. sort the nodes by weight

; step 1. write a producer get the weight of leof/tree
(define (weight-of-node node)
  (cond ((leaf? node) (weight-leaf node))
        (else (weight node))))

; step 2. insert a node to the order list
(define (adjoin-node x nodes)
  (cond ((null? nodes) (list x))
        ((< (weight-of-node x) (weight-of-node (car nodes))) (cons x nodes))
        (else (cons (car nodes)
                    (adjoin-node x (cdr nodes))))))

; step 3. done!
(define (successive-merge nodes)
  (if (null? (cdr nodes))
      (car nodes) ; only one node left, return it
      (successive-merge (adjoin-node (make-code-tree (car nodes)
                                                     (cadr nodes))
                                     (cddr nodes)))))

(define (generate-huffman-tree pairs)
  (successive-merge (make-leaf-set pairs)))

(define htree (generate-huffman-tree '((A 4) (C 1) (B 2) (D 1))))
(encode '(A D A B B C A) sample-tree)
(encode '(A D A B B C A) htree)

(encode (decode sample-message sample-tree) sample-tree)
(encode (decode sample-message htree) htree)