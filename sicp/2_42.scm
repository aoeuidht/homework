#lang racket

; 8-queens problem. We can formulate this approach recursively:
; Assume that we have already generated the sequence of all possible ways to place k - 1 queens
; in the first k - 1 columns of the board. board. For each of these ways, generate an extended set of positions by
; placing a queen in each row of the kth column.
; Now filter these, keeping only the positions for which the queen in the kth column is safe with respect to the other queens.
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

(define (flatmap proc seq)
  (accumulate append '() (map proc seq)))

(define (safe? k positions)
  (define (safe-wrapper n cands)
    (if (= n k)
        (cons (+ (car cands) 1)
              (- (car cands) 1))
        (let ((r (safe-wrapper (+ n 1)
                               (cdr cands)))
              (c1 (car cands)))
          (if (null? r)
              r
              (if (or (= c1 (car r))
                      (= c1 (cdr r))
                      (= (* c1 2) (+ (car r) (cdr r))))
                  '()
                  (cons (+ 1 (car r))
                        (- 1 (cdr r))))))))
  (let ((r0 (pair? (safe-wrapper 1 positions))))
    (dispaly k positions r0)
    r0)
  )

(define empty-board '())
(define (adjoin-position new-row k rest-of-queens)
  (append rest-of-queens (list new-row)))
(define (enumerate-interval start bs)
  (range start (+ bs 1)))

(define (queens board-size)
  (define (queen-cols k)
    (if (= k 0)
        (list empty-board)
        (filter
         (lambda (positions) (safe? k positions))
         (flatmap
          (lambda (rest-of-queens)
            (map (lambda (new-row)
                   (adjoin-position new-row k rest-of-queens))
                 (enumerate-interval 1 board-size)))
          (queen-cols (- k 1))))))
  (queen-cols board-size))

(queens 5)