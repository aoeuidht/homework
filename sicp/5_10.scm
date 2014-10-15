#lang racket
#|
Exercise 5.10.  Design a new syntax for register-machine instructions and modify the simulator to
use your new syntax. Can you implement your new syntax without changing any part of the
simulator except the syntax procedures in this section? 
|#

; Answer

#|
I want to add a ``JE`` to this register machine, like
(JE (const|register foo) (label label-name))

if exp equals zero, it will jump to the target label
|#

(define (make-je inst machine labels operations pc)
  (let ((value-exp (je-value-exp inst))
        (dest (je-dest inst)))
    (let ((value-proc
           (if (operation-exp? value-exp)
               (make-operation-exp
                value-exp machine labels operations)
               (make-primitive-exp
                (car value-exp) machine labels))))
      (lambda ()
        (if (= 0 (value-proc))
            (set-contents! pc (lookup-label labels (label-exp-label dest)))
            (advance-pc pc)))
      )
    )
  )

(define (js-dest je-instruction)
  (caddr je-instruction))

(define (je-value-exp je-instruction)
  (cadr je-instruction))

