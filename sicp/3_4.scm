#lang racket
; Exercise 3.4. Modify the make-account procedure of exercise 3.3 by adding another local state variable so that,
; if an account is accessed more than seven consecutive times with an incorrect password,
; it invokes the procedure call-the-cops.

(define (make-account balance pwd)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (let ((err-cnt 0))
    (define (dispatch pwd-input m)
      ; add the universal password check before dispatch
      (if (eq? pwd pwd-input)
          (cond ((eq? m 'withdraw) withdraw)
                ((eq? m 'deposit) deposit)
                (else (error "Unknown request -- MAKE-ACCOUNT"
                             m)))
          (if (> err-cnt 7)
              (error "call the cops")
              (begin (set! err-cnt (+ err-cnt 1))
                     (lambda (a) (display "pwd incorrect")))
              )))
    dispatch))

(define acc (make-account 100 'secret-password))
((acc 'secret-password 'withdraw) 40)
((acc 'secret-password 'withdraw) 40)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)
((acc 'some-other-password 'deposit) 50)