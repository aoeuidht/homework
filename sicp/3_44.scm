; Exercise 3.44.  Consider the problem of transferring an amount from one account to another. 
; Ben Bitdiddle claims that this can be accomplished with the following procedure, 
; even if there are multiple people concurrently transferring money among multiple accounts, 
; using any account mechanism that serializes deposit and withdrawal transactions, 
; for example, the version of make-account in the text above.

(define (transfer from-account to-account amount)
  ((from-account 'withdraw) amount)
  ((to-account 'deposit) amount))

; Louis Reasoner claims that there is a problem here, and that we need to use a more sophisticated method,
; such as the one required for dealing with the exchange problem. 
; Is Louis right? If not, what is the essential difference between the transfer 
; problem and the exchange problem? (You should assume that the balance in from-account is at least amount.) 

; Answer
; Louis is wrong. Because in the exchange problem, some mid-state are saved out of the
; inner serializer in the account itself, and the mid-state may be modified by other
; therad. In the transfer, no info is saved out of the serializer, so this procudure works.