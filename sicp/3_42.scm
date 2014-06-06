; Exercise 3.42.  Ben Bitdiddle suggests that it's a waste of time to create a new serialized
;procedure in response to every withdraw and deposit message. He says that make-account could be
; changed so that the calls to protected are done outside the dispatch procedure. 
; That is, an account would return the same serialized procedure
; (which was created at the same time as the account) each time it is
; asked for a withdrawal procedure.

(define (make-account balance)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (let ((protected (make-serializer)))
    (let ((protected-withdraw (protected withdraw))
          (protected-deposit (protected deposit)))
      (define (dispatch m)
        (cond ((eq? m 'withdraw) protected-withdraw)
              ((eq? m 'deposit) protected-deposit)
              ((eq? m 'balance) balance)
              (else (error "Unknown request -- MAKE-ACCOUNT"
                           m))))
      dispatch)))

; Is this a safe change to make? In particular, is there any difference in what 
; concurrency is allowed by these two versions of make-account ? 

; Answer
; Let's see how `serializer` introduced:
; `` A serializer takes a procedure as argument and returns a serialized procedure that behaves
; like the original procedure. All calls to a given serializer return serialized procedures in the same set.''

; Notice the 'return serialized procedures',
; after the 1st time called, the new implement will have no procedures to return.