#lang racket
#|

1. Showthateverynumberhasinfinitelymanyrepresentationsinthissystem.


; generate another tree with same value, then we can call it recursively, we can get
; infinite representations of the same number,
(define (generate-tree root)
  (diff root (diff (one) (one))))

|#

#|
2. implementation the procedures
|#

(define (zero)
  '(one one))

(define (calc-val root)
  (if (symbol? root)
      1
      (- (calc-val (car root))
         (calc-val (cadr root)))))

(define (is-zero? root)
  (if (symbol? root)
      #f
      (= (calc-val (car root))
         (calc-val (cadr root)))))

(define (successor root)
  (list root
        (list zero 'one)))

(define (successor root)
  '(root 'one))