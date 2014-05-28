; Exercise 3.17. Devise a correct version of the count-pairs procedure of exercise 3.16 that returns the
; number of distinct pairs in any structure. (Hint: Traverse the structure, maintaining an auxiliary data
; structure that is used to keep track of which pairs have already been counted.)

(define (his-chk one all)
  (cond ((null? all) #f)
        ((eq? one (car all)) #t)
        (else (his-chk one (cdr all)))))

(define his '())

(define (count-pairs x)
  (cond ((not (pair? x)) 0)
        ((his-chk x his) 0)
        (else (begin (set! his (cons x his))
                     (+ (count-pairs (car x))
                        (count-pairs (cdr x))
                        1)))))


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

