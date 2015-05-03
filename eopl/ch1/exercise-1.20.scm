#lang racket

#|
(count-occurrences s slist) returns the number of occur- rences of s in slist.
> (count-occurrences ’x ’((f x) y (((x z) x))))
 3
> (count-occurrences ’x ’((f x) y (((x z) () x))))
 3
> (count-occurrences ’w ’((f x) y (((x z) x))))
 0
|#

#|
count-occurrences: Sym X List -> List
|#

(define (count-occurrences s slist)
  (if (null? slist)
      0
      (let ((cur (car slist)))
        (+ (if (pair? cur)
               (count-occurrences s cur)
               (if (eq? s cur)
                   1
                   0))
           (count-occurrences s (cdr slist))))))

(display (count-occurrences 'x '((f x) y (((x z) x)))))
(newline)

(display (count-occurrences 'x '((f x) y (((x z) () x)))))
(newline)

(display (count-occurrences 'w '((f x) y (((x z) x)))))