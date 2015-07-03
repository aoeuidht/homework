#lang eopl

(require "queues.rkt")
(require "data-structures.rkt")       ; for continuation?
(require "lang.rkt")                  ; for expval?

(provide
 initialize-scheduler!
 set-final-answer!

 time-expired?
 decrement-timer!

 place-on-ready-queue!
 run-next-thread

 get-time-remaining
 restore-time-remaining!

 ;; pcb releated
 get-current-pcb
 generate-pcb!
 )

;;;;;;;;;;;;;;;; the state ;;;;;;;;;;;;;;;;

;; components of the scheduler state:

(define the-ready-queue   'uninitialized)
(define the-final-answer  'uninitialized)

(define the-max-time-slice    'uninitialized)
(define the-time-remaining    'uninitialized)

;; initialize-scheduler! : Int -> Unspecified
(define initialize-scheduler!
  (lambda (ticks)
    (set! the-ready-queue (empty-queue))
    (set! the-final-answer 'uninitialized)
    (set! the-max-time-slice ticks)
    (set! the-time-remaining the-max-time-slice)
    ))

;;;;;;;;;;;;;;;; the final answer ;;;;;;;;;;;;;;;;

;; place-on-ready-queue! : Thread -> Unspecified
;; Page: 184
(define place-on-ready-queue!
  (lambda (th . pcb)
    (set! the-ready-queue
          (enqueue the-ready-queue
                   (cons th (if (null? pcb)
                                (get-current-pcb)
                                (generate-pcb!)))))))

;; run-next-thread : () -> FinalAnswer
;; Page: 184
(define run-next-thread
  (lambda ()
    (if (empty? the-ready-queue)
        the-final-answer
        (dequeue the-ready-queue
                 (lambda (first-ready-thread other-ready-threads)
                   (set! the-ready-queue other-ready-threads)
                   (set! the-time-remaining the-max-time-slice)
                   (set-current-pcb! (cdr first-ready-thread))
                   (eopl:printf "switch-to-theread ~s~%"
                                (cdr first-ready-thread))
                   ((car first-ready-thread))
                   )))))

;; set-final-answer! : ExpVal -> Unspecified
;; Page: 184
(define set-final-answer!
  (lambda (val)
    (set! the-final-answer val)))

;; time-expired? : () -> Bool
;; Page: 184
(define time-expired?
  (lambda ()
    (zero? the-time-remaining)))

;; decrement-timer! : () -> Unspecified
;; Page: 184
(define decrement-timer!
  (lambda ()
    (set! the-time-remaining (- the-time-remaining 1))))


;;; add the yield releated operations

(define (get-time-remaining)
  the-time-remaining)

(define (restore-time-remaining! tr)
  (set! the-time-remaining tr))


;;; the pcb of current running process

;;; a process-control-bolck is a list,
;;; with current tid(therad-id), pid(parent-thread-id)
;;; all the threads are forked by tid 0
(define current-pcb (list 1 0))
(define next-pid 1)

(define (get-next-pid!)
  (set! next-pid (+ next-pid 1))
  next-pid)

(define (get-current-pcb) current-pcb)

(define (set-current-pcb! pcb)
  (set! current-pcb pcb))

(define (generate-pcb!)
  (list (get-next-pid!) (car current-pcb)))
