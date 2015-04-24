#lang racket

#|
(swapper s1 s2 slist) returns a list the same as slist, but with all occurrences of s1 replaced by s2 and all occurrences of s2 replaced by s1.
  > (swapper ’a ’d ’(a b c d))
  (d b c a)
  > (swapper ’a ’d ’(a d () c d))
  (d a () c a)
  > (swapper ’x ’y ’((x) y (z (x))))
  ((y) x (z (y)))
|#

#|
swapper symbel X symbol X list --> List
|#

(define (swapper s1 s2 slist)
  (if (null? slist)
      '()
      (let ((cur (car slist)))
        (cons (if (pair? cur)
                  (swapper s1 s2 cur)
                  (cond ((eq? s1 cur) s2)
                        ((eq? s2 cur) s1)
                        (else cur)))
              (swapper s1 s2 (cdr slist))))))

(display (swapper 'a 'd '(a b c d)))
(newline)

(display (swapper 'a 'd '(a d () c d)))
(newline)

(display (swapper 'x 'y '((x) y (z (x)))))
(newline)
                    