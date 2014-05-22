#lang racket
; Exercise 2.84. Using the raise operation of exercise 2.83, modify the apply-generic procedure so that
; it coerces its arguments to have the same type by the method of successive raising, as discussed in this
; section. You will need to devise a way to test which of two types is higher in the tower. 
; Do this in a manner that is ``compatible'' with the rest of the system and will not lead to problems 
; in adding new levels to the tower.

; Answer
; while checking the types, just do it recursivly

(define (r-raise arg target-type)
  (let ((arg-raise (raise arg)))
    (cond ((nil? arg-raise) '())
          ((eq? (tag-type arg-raise) target-type) arg-raise)
          (else (r-raise arg-raise target-type)))))

(define (apply-generic op . args)
  (let ((type-tags (map type-tag args)))
    (let ((proc (get op type-tags)))
      (if proc
          (apply proc (map contents args))
          (if (= (length args) 2)
              (let ((type1 (car type-tags))
                    (type2 (cadr type-tags))
                    (a1 (car args))
                    (a2 (cadr args)))
                (let ((t1->t2 (r-raise type1 (tag-type type2)))
                      (t2->t1 (r-raise type2 (tag-type type1))))
                  (cond (t1->t2
                         (apply-generic op t1->t2 a2))
                        (t2->t1
                         (apply-generic op a1 t2->t1))
                        (else
                         (error "No method for these types"
                                (list op type-tags))))))
              (error "No method for these types"
                     (list op type-tags)))))))

