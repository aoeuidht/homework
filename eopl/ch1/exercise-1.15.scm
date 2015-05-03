#lang racket
; (duple n x) returns a list containing n copies of x
; > (duple 2 3)
; (3, 3)
; (duple 4 '(ha ha))
; ((ha ha) (ha ha) (ha ha) (ha ha))
; (duple 0 '(blah))
; ()

; duple: Int X List --> List
; usage: (duple 2 3)
;        = (3, 3)

(define (duple n x)
  (if (= n 0)
      '()
      (cons x (duple (- n 1)
                     x))))

(display
 (duple 2 3))

(display (duple 4 '(ha ha)))

(display (duple 0 '(blah)))