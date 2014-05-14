#lang racket
; Exercise 2.51. Define the below operation for painters. Below takes two painters as arguments.
; The resulting painter, given a frame, draws with the first painter in the bottom of the frame
; and with the second painter in the top. Define below in two different ways
; -- first by writing a procedure that is analogous to the beside procedure given above,
; and again in terms of beside and suitable rotation operations (from exercise 2.50).

(define (beside painter1 painter2)
  (let ((split-point (make-vect 0.5 0.0)))
    (let ((paint-left
           (transform-painter painter1
                              (make-vect 0.0 0.0)
                              split-point
                              (make-vect 0.0 1.0)))
          (paint-right
           (transform-painter painter2
                              split-point
                              (make-vect 1.0 0.0)
                              (make-vect 0.5 1.0))))
      (lambda (frame)
        (paint-left frame)
        (paint-right frame)))))

; so the below is 
(define (below painter1 painter2)
  (let ((split-point (make-vert 0.0 0.5)))
    (let ((paint-bottom
           (tarnsform-painter painter1
                              (make-vert 0.0 0.0)
                              (make-vert 0.0 1.0)
                              split-point))
          (paint-up
           (transform-painter pointer2
                              split-point
                              (make-vert 0.0 1.0)
                              (make-vert 1.0 0.0))))
      (lambda (frame)
        (paint-bottom frame)
        (paint-up frame)))))

; the beside and rotate solution
(define (below p-down p-up)
  (let ((p-left (rotate90 p-up))
        (p-right (rotate90 p-down)))
    (rotate270 (beside p-left p-right))))