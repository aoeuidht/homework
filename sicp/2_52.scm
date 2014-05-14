#lang racket
; Exercise 2.52. Make changes to the square limit of wave shown in figure 2.9 by working
; at each of the levels described above. In particular:

; b. Change the pattern constructed by corner-split (for example, by using only one copy of the up-
; split and right-split images instead of two).

(define (corner-split painter n)
  (if (= n 0)
      painter
      (let ((up (up-split painter (- n 1)))
            (right (rotate270 (up-split (rotate90 painter) (- n 1)))))
        (let ((top-left (beside up up))
              (bottom-right (below right right))
              (corner (corner-split painter (- n 1))))
          (beside (below painter top-left)
                  (below bottom-right corner))))))

; c. Modify the version of square-limit that uses square-of-four so as to assemble the corners in a
; different pattern. (For example, you might make the big Mr. Rogers look outward from each corner of the square.)
(define (square-limit painter n)
  (let ((quarter (corner-split painter n)))
    (let ((half (beside (flip-horiz quarter) quarter)))
      (below (flip-vert half) half))))

(define (square-of-four tl tr bl br)
  (lambda (painter)
    (let ((top (beside (tl painter) (tr painter)))
          (bottom (beside (bl painter) (br painter))))
      (below bottom top))))

(define (square-limit painter n)
  (let ((quarter (corner-split painter n)))
    ((square-of-four (rotate90 quarter)
                    quarter
                    (rotate180 quarter)
                    (rotate270 quarter)))
    painter))