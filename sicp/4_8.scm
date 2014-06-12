#|
Exercise 4.8. ``Named let'' is a variant of let that has the form
(let <var> <bindings> <body>)

The <bindings> and <body> are just as in ordinary let, except that <var> 
is bound within <body> to a procedure whose body is <body> and whose parameter
s are the variables in the <bindings>. Thus, one can
repeatedly execute the <body> by invoking the procedure named <var>. 
For example, the iterative Fibonacci procedure (section 1.2.2) can be 
rewritten using named let as follows:
(define (fib n)
  (let fib-iter ((a 1)
                 (b 0)
                 (count n))
    (if (= count 0)
        b
        (fib-iter (+ a b) a (- count 1)))))
Modify let->combination of exercise 4.6 to also support named let.
|#

(define (let? exp) (tagged-list? exp 'let))

(define (let-params exp) (cadr exp))
(define (let-body exp) (cddr exp))
  
(define (named-let? exp) (symbol? (cadr exp)))
(define (named-let-name exp) (cadr exp))
(define (named-let-params exp) (caddr exp))
(define (named-let-body exp) (cadddr exp))

(define (let-combination exp)
  (if (named-let? exp)
      (sequence->exp (list (list 'define 
                                 (cons (named-let-name exp)
                                       (map car (named-let-params exp)))
                                 (named-let-body exp))
                           (cons (named-let-name exp)
                                 (map cadr (named-let-params exp)))))
      (cons (make-lambda (map car (let-params exp))
                         (let-body exp))
            (map cadr (let-params exp)))))

(define (make-lambda parameters body)
  (cons 'lambda (cons parameters body)))

(define (begin? exp) (tagged-list? exp 'begin))
(define (begin-actions exp) (cdr exp))
(define (last-exp? seq) (null? (cdr seq)))
(define (first-exp seq) (car seq))
(define (rest-exps seq) (cdr seq))
(define (sequence->exp seq)
  (cond ((null? seq) seq)
        ((last-exp? seq) (first-exp seq))
        (else (make-begin seq))))
(define (make-begin seq) (cons 'begin seq))

(let-combination '(let fib-iter ((a 1)
                                 (b 0)
                                 (count n))
                    (if (= count 0)
                        b
                        (fib-iter (+ a b) a (- count 1)))))

; then we got
(begin 
  (define (fib-iter a b count)
    (if (= count 0)
        b
        (fib-iter (+ a b) a (- count 1))))
  (fib-iter 1 0 n))