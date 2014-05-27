; Exercise 3.16. Ben Bitdiddle decides to write a procedure to count the number of pairs in any list structure.
; ``It's easy,'' he reasons. ``The number of pairs in any structure is the number in the car plus the number
; in the cdr plus one more to count the current pair.'' So Ben writes the following procedure:
(define (count-pairs x)
  (if (not (pair? x))
      0
      (+ (count-pairs (car x))
         (count-pairs (cdr x))
         1)))
; Show that this procedure is not correct. In particular,
; draw box-and-pointer diagrams representing list structures made up
; of exactly three pairs for which Ben's procedure would return 3; return 4; return 7; never return at all.

(let ((p1 (cons 1 '()))
      (p2 (cons 2 '()))
      (p3 (cons 3 '())))
  
  ; 3
  (set-cdr! p1 p2)
  (set-cdr! p2 p3)
  (display (count-pairs p1))
  (set-cdr! p1 p3)
  (set-car! p1 p2)
  (display (count-pairs p1))
  
  (set-car! p1 p2)
  (set-cdr! p1 p2)
  (set-car! p2 p3)
  (set-cdr! p2 p3)
  (display (count-pairs p1))
  
  (set-car! p2 p1) ; infinite loop here
)