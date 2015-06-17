#lang eopl

(require "store.rkt")

(provide (all-defined-out))

;;;;;;;;;;;;;;;; mutable pairs ;;;;;;;;;;;;;;;;

;; model a mutable pair as two consecutive locations (left and
;; right), and represent it as a reference to the first.

;; mutpair? : SchemeVal -> Bool
;; Page: 129
;;
;; Not every reference is really a mutpair, but this test is good
;; enough, because in the implicit-refs language, you
;; can't get your hands on a reference otherwise.
(define mutpair?
  (lambda (v)
    (reference? v)))

;; make-pair : ExpVal * ExpVal -> MutPair
;; Page: 129
(define make-pair
  (lambda (val1 val2)
    (let ((ref1 (newref val1)))
      (let ((ref2 (newref val2)))
        ref1))))

;; left : MutPair -> ExpVal
;; Page: 129
(define left
  (lambda (p)
    (deref p)))

;; right : MutPair -> ExpVal
;; Page: 129
(define right
  (lambda (p)
    (deref (+ 1 p))))

;; setleft : MutPair * ExpVal -> Unspecified
;; Page: 129
(define setleft
  (lambda (p val)
    (setref! p val)))

;; setright : MutPair * Expval -> Unspecified
;; Page: 129
(define setright
  (lambda (p val)
    (setref! (+ 1 p) val)))

(define (arrval? v)
  (pair? v))

(define (my-range start end)
  (if (>= start end)
      '()
      (cons start (my-range (+ 1 start) end))
      )
  )

(define (arraylen arr)
  (car arr))

(define (arraydata arr)
  (cdr arr))

(define (array-idx-get arr idx)
  (if (< idx (car arr))
      (+ (car arr) idx)
      (eopl:error 'array-index-out-of-range "max-index is ~s, got ~s"
                  (car arr) idx)
      )
  )

(define (make-array arr-len init-val)
  (cons arr-len
        (car (map (lambda (idx) (newref init-val))
                  (my-range 0 arr-len)))))

(define (arrayref arr ref-idx)
  (deref (array-idx-get arr ref-idx))
  )

(define (arrayset arr set-idx val)
  (setref! (array-idx-get arr set-idx) val))
