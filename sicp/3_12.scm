; Exercise 3.12. The following procedure for appending lists was introduced in section 2.2.1:
(define (last-pair x)
  (if (null? (cdr x))
      x
      (last-pair (cdr x))))



(define (append! x y)
  (set-cdr! (last-pair x) y)
  x)

(define x (list 'a 'b))
(define y (list 'c 'd))
(define z (append x y))

(cdr x) ; (b)

(define w (append! x y))
(cdr x) ; (b c d)