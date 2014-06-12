#| Exercise 4.6. Let expressions are derived expressions, because
(let ((<var1> <exp1>) ... (<varn> <expn>)) <body>)
is equivalent to
((lambda (<var1> ... <varn>) <body>)
<exp1> <expn>)
Implement a syntactic transformation let->combination that reduces evaluating
let expressions to evaluating combinations of the type shown above, 
and add the appropriate clause to eval to handle let expressions.
|#

(define (let? exp) (tagged-list? exp 'let))
(define (let-params exp) (cadr exp))
(define (let-body exp) (cddr exp))

(define (let-combination exp)
  (list (make-lambda (map car (let-params exp))
                     (let-body exp))
        (map cdr (let-params exp))))

(define (make-lambda parameters body)
  (cons 'lambda (cons parameters body)))


; this is the test for exercise 4.7
(let-combination '(let* ((x 3)
                           (y (+ x 2))
                           (z (+ x y 5)))
                      (* x z)))

