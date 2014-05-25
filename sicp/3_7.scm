#lang racket
; Exercise 3.7. Consider the bank account objects created by make-account,
; with the password modification described in exercise 3.3.
; Suppose that our banking system requires the ability to make joint accounts.
; Define a procedure make-joint that accomplishes this. Make-joint should take three
; arguments. The first is a password-protected account. The second argument must match
; the password with which the account was defined in order for the make-joint operation to proceed.
; The third argument is a new password. Make-joint is to create an additional access to
; the original account using the new password. For example,
; if peter-acc is a bank account with password open-sesame, then
; (define paul-acc
;   (make-joint peter-acc 'open-sesame 'rosebud))

(define (make-account balance pwd)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (define (dispatch pwd-input m)
    ; add the universal password check before dispatch
    (if (eq? pwd pwd-input)
        (cond ((eq? m 'withdraw) withdraw)
              ((eq? m 'deposit) deposit)
              (else (error "Unknown request -- MAKE-ACCOUNT"
                           m)))
        (error "Incorrect pasword")))
  dispatch)

(define (make-joint acc ori-pwd new-pwd)
  ((acc ori-pwd 'withdraw) 0)
  (define (dispatch pwd-input m)
    (if (eq? new-pwd pwd-input)
        (acc ori-pwd m)
        (error "incorrect password")))
  dispatch)

(define acc (make-account 100 'secret-password))
((acc 'secret-password 'withdraw) 40)
((acc 'secret-password 'withdraw) 40)
; ((acc 'some-other-password 'deposit) 50)

(define acc1 (make-account 100 'secret-password))

(define jacc (make-joint acc1 'secret-password 'jpassword))
((jacc 'jpassword 'withdraw) 40)
((jacc 'jpassword 'withdraw) 40)
((jacc 'jpassword 'deposit) 50)
(define invalid-acc (make-joint acc1 'wrong-password 'jpassword))