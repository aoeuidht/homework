; Exercise 3.25. Generalizing one- and two-dimensional tables, show how to implement
; a table in which values are stored under an arbitrary number of keys and different
; values may be stored under different numbers of keys. The lookup and insert! 
; procedures should take as input a list of keys used to access the table.

(define (make-table)
  (let ((local-table (list '*table*)))
    (define (lookup key)
      (let ((record (assoc key (cdr local-able))))
        (if record
            (cdr record)
            false)))
    (define (assoc key records)
      (cond ((null? records) #f)
            ((equal? key (caar records)) (car records))
            (else (assoc key (cdr records)))))
    (define (r-lookup keys)
      (let ((r (assoc (car keys) (cdr local-table))))
        (if r
            (cond ((null? (cdr keys)) (cdr r))
                  (else (((cdr r) 'r-lookup) (cdr keys))))
            #f)))
    
    (define (r-insert! keys value)
      (if (null? (cdr keys))
          (insert! (car keys) value)
          (let ((record (assoc (car keys) (cdr local-table))))
            (if record
                (((cdr record) 'r-insert!) (cdr keys) value)
                ; if no record available, create new table, then insert
                (let ((tb (make-table)))
                  ((tb 'r-insert!) (cdr keys) value) ; insert to new table
                  (insert! (car keys) tb))))))
    
    (define (insert! key value)
      (let ((record (assoc key (cdr local-table))))
        (if record
            (set-cdr! record value)
            (set-cdr! local-table
                      (cons (cons key value) (cdr local-table)))))
      'ok)
    (define (pnt-table) local-table)
    (define (dispatch m)
      (cond ((eq? m 'lookup-proc) lookup)
            ((eq? m 'insert-proc!) insert!)
            ((eq? m 'r-insert!) r-insert!)
            ((eq? m 'r-lookup) r-lookup)
            ((eq? m 'pnt) pnt-table)
            (else (error "Unknown operation -- TABLE" m))))
    dispatch))


(define t (make-table))
((t 'r-insert!) '(1 2 3 4 5) 10)
((t 'pnt))
((t 'r-lookup) '(1 2 3 4 5))
((t 'r-lookup) '(1 2 3 4))
((t 'r-lookup) '(1 2 3 4 6))