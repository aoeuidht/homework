#lang r5rs

; 5.38 a
(define (spread-arguments op1 op2)
  (let ((code1 (compile op1 'arg1 'next))
        (code2 (compile op2 'arg2 'next)))
    (list code1 code2)))


                                        ;5.38 b
(define (compile-open-code exp target linkage)
  (let ((after-call (make-label 'after-call))
        )
    (let ((compiled-linkage
           (if (eq? linkage 'next) after-call linkage))
          (argls (spread-arguments (cadr exp) (caddr exp)))
          )
      (append-instruction-sequences
       (end-with-linkage
        compiled-linkage
        (append-instruction-sequences
         (car argls)
         (preserving '(arg1)
                     (cadr argls)
                     (make-instruction-sequence '(arg1 arg2)
                                                (list target)
                                                `((assign ,target
                                                          (op ,(car exp))
                                                          (reg arg1)
                                                          (reg arg2)))))))
              after-call))))


                                        ; 5.38 d
(define (expand-big-open-code exp)
  (let ((operator (car exp))
        (oper-1st (cadr exp))
        (oper-2nd (caddr exp)))
    (if (> (length exp) 3)
        (list operator (list operator oper-1st oper-2nd)
              (cdddr exp))
                exp)))

(define (compile-open-code exp target linkage)
  (if (> (length exp) 3)
      (compile-open-code (expand-big-open-code exp) target linkage)
      (let ((after-call (make-label 'after-call))
            )
        (let ((compiled-linkage
               (if (eq? linkage 'next) after-call linkage))
              (argls (spread-arguments (cadr exp) (caddr exp)))
              )
          (append-instruction-sequences
           (end-with-linkage
            compiled-linkage
            (append-instruction-sequences
             (car argls)
             (preserving '(arg1)
                         (cadr argls)
                         (make-instruction-sequence '(arg1 arg2)
                                                    (list target)
                                                    `((assign ,target
                                                              (op ,(car exp))
                                                              (reg arg1)
                                                              (reg arg2)))))))
           after-call)))))
