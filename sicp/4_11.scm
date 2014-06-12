#|
Exercise 4.11. Instead of representing a frame as a pair of lists,
 we can represent a frame as a list of bindings, where each binding
 is a name-value pair. Rewrite the environment operations to use this alternative representation.
|#

(define (make-frame variables values)
  (map cons variables values))
(define (add-binding-to-frame! var val frame)
  (if (null? (cdr frame))
      (set-cdr! frame (cons (cons var val) '()))
      (add-binding-to-frame! var val (cdr frame))))

; tests
(define x (make-frame '(a b c d) '(1 2 3 4)))
(add-binding-to-frame! 'y 10 x)
(display x)

(define (extend-environment vars vals base-env)
  (if (= (length vars) (length vals))
      (cons (make-frame vars vals) base-env)
      (if (< (length vars) (length vals))
          (error "Too many arguments supplied" vars vals)
          (error "Too few arguments supplied" vars vals))))

(define (lookup-variable-value var env)
  (define (scan frame)
    (cond ((null? frame))
          (lookup-variable-value var
                                 (encloing-environment env))
          ((eq? (caar frame) var) (cdar frame))
          (else (scan (cdr frame)))))

  (if (eq? env the-empty-environment)
      (error "Unbound variable" var)
      (scan (first-frame env))))

(define (set-variable-value! var val env)
  (define (scan frame)
    (cond ((null? frame)
           (set-variable-value! var val (enclosing-environment env)))
          ((eq? (caar frame) var) (set-cdr! (car frame) val))
          (else (scan (cdr frame)))))
  (if (eq? env the-empty-environment)
      (error "Unbound variable -- SET!" var)
      (scan (first-frame frame))))

(define (define-variable! var val env)
  (define (scan frame)
    (cond ((null? frame)
           (add-binding-to-frame! var val (first-frame env)))
          ((eq? (caar frame) var) (set-cdr! (car frame) val))
          (else (scan (cdr frame)))))
  (scan (first-frame env)))
