#lang racket

; Use this notation to write a procedure same-parity that takes one or more integers and returns a list of
; all the arguments that have the same even-odd parity as the first argument. For example,

(define (same-parity sample . rest)
  (define (sp-wrapper candidate seo rst)
    (if (null? candidate)
        rst
        (if (= seo
               (remainder (car candidate) 2))
            (sp-wrapper (cdr candidate) seo
                        (append rst (list (car candidate))))
            (sp-wrapper (cdr candidate) seo
                        rst)
            )))
  (define (sp-wrapper? cand seo rst)
    (car cand))
  (let ((sample-eo (remainder sample 2)))
    (cons sample (sp-wrapper rest sample-eo '()))
    ;rest
    ))

(same-parity 1 2 3 4 5 6 7)
