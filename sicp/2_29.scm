#lang racket
; Exercise 2.29. A binary mobile consists of two branches, a left branch and a right branch. Each branch is a
; rod of a certain length, from which hangs either a weight or another binary mobile. We can represent a
; binary mobile using compound data by constructing it from two branches (for example, using list):
(define (make-mobile left right)
  (list left right))
; A branch is constructed from a length (which must be a number) together with a structure, which
; may be either a number (representing a simple weight) or another mobile:
(define (make-branch length structure)
  (list length structure))
; a. Write the corresponding selectors left-branch and right-branch, which return the branches of a
; mobile, and branch-length and branch-structure, which return the components of a branch.
(define (left-branch mobile)
  (car mobile))
(define (right-branch mobile)
  (car (cdr mobile)))
(define (branch-len branch) (car branch))
(define (branch-str branch) (car (cdr branch)))

; b. Using your selectors, define a procedure total-weight that returns the total weight of a mobile.
; Answer:
; first we have to write a helper method
(define (mobile? tgt) (and (pair? tgt)
                           (pair? (car tgt))))
(define (total-weight tgt)
  (if (mobile? tgt)
      (+ (total-weight (left-branch tgt))
         (total-weight (right-branch tgt)))
      (if (pair? tgt)
          (total-weight (branch-str tgt))
          tgt)
      ))

; copy the tests

  
 (define level-1-mobile (make-mobile (make-branch 2 1) 
                                     (make-branch 1 2))) 
 (define level-2-mobile (make-mobile (make-branch 3 level-1-mobile) 
                                     (make-branch 9 1))) 
 (define level-3-mobile (make-mobile (make-branch 4 level-2-mobile) 
                                     (make-branch 8 2))) 
  
 (total-weight level-1-mobile) 
 (total-weight level-2-mobile) 
 (total-weight level-3-mobile)
; c. A mobile is said to be balanced if the torque applied by its top-left branch is equal to that applied by its
; top-right branch (that is, if the length of the left rod multiplied by the weight hanging from that rod is equal
; to the corresponding product for the right side) and if each of the submobiles hanging off its branches is
; balanced. Design a predicate that tests whether a binary mobile is balanced.

; d. Suppose we change the representation of mobiles so that the constructors are
;(define (make-mobile left right)

;(cons left right))
;(define (make-branch length structure)
;(cons length structure))
; How much do you need to change your programs to convert to the new representation?