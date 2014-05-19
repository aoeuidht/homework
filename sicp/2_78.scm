#lang racket
(define (attach-tag type-tag contents)
  (if (or (symbol? contents)
          (number? contents))
      contents
      (cons type-tag contents)))

(define (type-tag datum)
  (if (pair? datum)
      (car datum)
      (cond ((symbol? datum) 'symbol)
            ((number? datum) 'scheme-number)
            (else      (error "Bad tagged datum -- TYPE-TAG" datum)))))
(define (contents datum)
  (if (pair? datum)
      (cdr datum)
      (cond ((symbol? datum) datum)
            ((number? datum) datum)
            (else      (error "Bad tagged datum -- TYPE-TAG" datum)))))

; Exercise 2.78. The internal procedures in the scheme-number package are essentially nothing more
;than calls to the primitive procedures +, -, etc. It was not possible to use the primitives of the language
;directly because our type-tag system requires that each data object have a type attached to it. In fact,
;however, all Lisp implementations do have a type system, which they use internally. Primitive predicates
;such as symbol? and number? determine whether data objects have particular types. Modify the
;definitions of type-tag, contents, and attach-tag from section 2.4.2 so that our generic system
;takes advantage of Scheme's internal type system. That is to say, the system should work as before except
;that ordinary numbers should be represented simply as Scheme numbers rather than as pairs whose car is
;the symbol scheme-number.

