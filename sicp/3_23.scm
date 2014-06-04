; Exercise 3.23. A deque (``double-ended queue'') is a sequence in which items can be
; inserted and deleted at either the front or the rear. Operations on deques are the
; constructor make-deque, the predicate empty-deque?, selectors front-deque and rear-deque,
; and mutators front-insert- deque!, rear-insert-deque!, front-delete-deque!, and
; rear-delete-deque!. Show how to represent deques using pairs, and give implementations
; of the operations.23 All operations should be accomplished in theta(1) steps.

; Answer
; make each item in the list linke this
;  value | ---> prev_item|next_item
(define (make-dqueue) (cons '() '()))
(define (empty-dqueue? q) (null? (car q)))

(define (front-dqueue dq) (caar dq))
(define (front-insert-dqueue! dq item)
  (let ((new-item (cons item (cons '() '()))))
    (if (empty-dqueue? dq)
        (begin (set-car! dq new-item)
               (set-cdr! dq new-item))
        (begin (set-car! (cdar dq) new-item)  ; point old head to new
               (set-cdr! (cdr new-item) (car dq))
               (set-car! dq new-item))
          )))

(define (print-dqueue dq)
  (define (pnt-dq q)
    (display (car q))
    (display '->)
    (display #\space)
    (if (null? (cddr q))
        (display #\newline)
        (pnt-dq (cddr q))))
  (if (empty-dqueue? dq)
      (begin (display 'blank-dqueue)  
             (display #\space))
      (pnt-dq (car dq))))

(define (rear-insert-dqueue! dq item)
  (let ((new-item (cons item (cons '() '()))))
    (if (empty-dqueue? dq)
        (begin (set-car! dq new-item)
               (set-cdr! dq new-item))
        (begin (set-cdr! (cddr dq) new-item)  ; point old rear to new
               (set-car! (cdr new-item) (cdr dq))
               (set-cdr! dq new-item))
          )))

(define (rear-dqueue dq)
  (if (null? dq)
      (display 'blank-dqueue)
      (cadr dq)))

(define (front-delete-dqueue! dq)
  (if (empty-dqueue? dq)
      (error 'cant-delete-blank-queue)
      (let ((new-front (cddar dq)))
        (set-car! (cdr new-front) '())
        (set-car! dq new-front)
        (cond ((empty-dqueue? dq) (set-cdr! dq '()))))))

(define (rear-delete-dqueue! dq)
  (if (empty-dqueue? dq)
      (error 'cant-delete-blank-queue)
      (let ((new-rear (caddr dq)))
        (set-cdr! (cdr new-rear) '())
        (set-cdr! dq new-rear)
        (cond ((null? (cdr dq)) (set-car! dq '()))))))
  

(define dq (make-dqueue))
(empty-dqueue? dq)
(front-insert-dqueue! dq 1)
(front-dqueue dq)
(print-dqueue dq)
(front-insert-dqueue! dq 2)
(print-dqueue dq)
(rear-insert-dqueue! dq 3)
(print-dqueue dq)
(rear-dqueue dq)
(front-delete-dqueue! dq)
(print-dqueue dq)
(rear-delete-dqueue! dq)
(print-dqueue dq)