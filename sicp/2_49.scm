#lang racket
(define (frame-coord-map frame)
  (lambda (v)
    (add-vect
     (origin-frame frame)
     (add-vect (scale-vect (xcor-vect v)
                           (edge1-frame frame))
               (scale-vect (ycor-vect v)
                           (edge2-frame frame))))))

(define (segments->painter segment-list)
  (lambda (frame)
    (for-each
     (lambda (segment)
       (draw-line
        ((frame-coord-map frame) (start-segment segment))
        ((frame-coord-map frame) (end-segment segment))))
     segment-list)))

; Exercise 2.49. Use segments->painter to define the following primitive painters: 

(let ((tl (make-vector  0 1))
      (tr (make-vector 1 1))
      (bl (make-vector 0 0))
      (br (make-vector 1 0)))

  ; a. The painter that draws the outline of the designated frame.;

  (segments->painter (list (make-segment bl tl)
                           (make-segment tl tr)
                           (make-segment tr br)
                           (make-segment br bl)))
  ;  b. The painter that draws an ``X'' by connecting opposite corners of the frame.
  (segments-painter (list (make-segment tl br)
                          (make-segment bl tr)))
  ; c. The painter that draws a diamond shape by connecting the midpoints of the sides of the frame. 
  (segments-painter (list (make-segment (make-vector 0 0.5) (make-segment 0.5 1))
                          (make-segment (make-vector 0.5 1) (make-segment 1 0.5))
                          (make-segment (make-vector 1 0.5) (make-segment 0.5 0))
                          (make-segment (make-vector 0.5 0) (make-segment 0 0.5))))
  ; d. The wave painter.
  )
  