;  Exercise 3.53.  Without running the program, describe the elements of the stream defined by

(define s (cons-stream 1 (add-streams s s)))

; Answer

; the 2nd elment of stream doubled the 1st elment of the stream, so
; this stream generate numbers like
; 1 2 4 8 ... (pow 2 n)