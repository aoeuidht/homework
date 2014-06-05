; Exercise 3.24. In the table implementations above, the keys are tested for equality using equal? (called by assoc).
; This is not always the appropriate test. For instance, we might have a table with numeric keys
; in which we don't need an exact match to the number we're looking up,
; but only a number within some tolerance of it. Design a table constructor make-table
; that takes as an argument a same-key? procedure that will be used to test ``equality'' of keys.
; Make-table should return a dispatch procedure that can be used to access appropriate lookup
; and insert! procedures for a local table.



(define (make-table same-key?)
  (let ((local-table (list '*table*)))
    (define (lookup key)
      (let ((record (assoc key (cdr local-able))))
        (if record
            (cdr record)
            false)))
    (define (assoc key records)
      (cond ((null? records) false)
            ((same-key? key (caar records)) (car records))
            (else (assoc key (cdr records)))))
    
    (define (insert! key value)
      (let ((record (assoc key (cdr local-table))))
        (if record
            (set-cdr! record value)
            (set-cdr! local-table
                      (cons (cons key value) (cdr local-table)))))
      'ok)
    (define (dispatch m)
      (cond ((eq? m 'lookup-proc) lookup)
            ((eq? m 'insert-proc!) insert!)
            (else (error "Unknown operation -- TABLE" m))))
    dispatch))
