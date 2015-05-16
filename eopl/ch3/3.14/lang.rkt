#lang eopl

;; grammar for the LET language  

(provide (all-defined-out))

;;;;;;;;;;;;;;;; grammatical specification ;;;;;;;;;;;;;;;;

(define the-lexical-spec
  '((whitespace (whitespace) skip)
    (comment ("%" (arbno (not #\newline))) skip)
    (identifier
     (letter (arbno (or letter digit "_" "-" "?" "+" "*" "/")))
     symbol)
    (number (digit (arbno digit)) number)
    (number ("-" digit (arbno digit)) number)
    (unary-bool-op ((or "zero?" "null?")) string)
    (binary-bool-op ((or "equal?" "greater?"
                         "less?")) string)
    ))

(define the-grammar
  '((program (expression) a-program)
    
    (expression (number) const-exp)
    (expression
     ("-" "(" expression "," expression ")")
     diff-exp)
    
    (bool-exp
     (unary-bool-op "(" expression ")") unary-bool-exp)
    (bool-exp
     (binary-bool-op "(" expression "," expression ")") binary-bool-exp)
    
    (expression
     ("if" bool-exp "then" expression "else" expression)
     if-exp)
    
    (expression (identifier) var-exp)
    (expression (bool-exp) b-exp)
    
    (expression
     ("let" identifier "=" expression "in" expression)
     let-exp)   

    ;; add the minos operator
    (expression
     ("minus" "(" expression ")")
     minus-exp)

    ;; add addition
    (expression
     ("+" "(" expression "," expression ")")
     add-exp)

    ;; add multiplication
    (expression
     ("*" "(" expression "," expression ")")
     mul-exp)

    ;; add quotient
    (expression
     ("/" "(" expression "," expression ")")
     div-exp)

    ;; list related expression here
    (expression
     ("cons" "(" expression "," expression ")")
     cons-exp)
    (expression
     ("car" "(" expression ")")
     car-exp)
    (expression
     ("cdr" "(" expression ")")
     cdr-exp)
    (expression
     ("emptylist")
     empty-list-exp)

    ;; the 'list keyword
    (expression
     ("list" "(" (separated-list expression ",") ")")
     list-exp)

    (expression
     ("cond"
      (arbno bool-exp "==>" expression)
      "end")
     cond-exp)
    ))

;;;;;;;;;;;;;;;; sllgen boilerplate ;;;;;;;;;;;;;;;;

(sllgen:make-define-datatypes the-lexical-spec the-grammar)

(define show-the-datatypes
  (lambda () (sllgen:list-define-datatypes the-lexical-spec the-grammar)))

(define scan&parse
  (sllgen:make-string-parser the-lexical-spec the-grammar))

(define just-scan
  (sllgen:make-string-scanner the-lexical-spec the-grammar))


