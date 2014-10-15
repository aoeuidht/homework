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


(define (make-execution-procedure inst labels machine
                                  pc flag stack ops)
  (cond ((eq? (car inst) 'assign)
         (make-assign inst machine labels ops pc))
        ((eq? (car inst) 'test)
         (make-test inst machine labels ops flag pc))
        ((eq? (car inst) 'branch)
         (make-branch inst machine labels flag pc))
        ((eq? (car inst) 'goto)
         (make-goto inst machine labels pc))
        ((eq? (car inst) 'save)
         (make-save inst machine stack pc))
        ((eq? (car inst) 'restore)
         (make-restore inst machine stack pc))
        ((eq? (car inst) 'perform)
         (make-perform inst machine labels ops pc))
(define (make-execution-procedure inst labels machine
                                  pc flag stack ops)
  (cond ((eq? (car inst) 'assign)
         (make-assign inst machine labels ops pc))
        ((eq? (car inst) 'test)
         (make-test inst machine labels ops flag pc))
        ((eq? (car inst) 'branch)
         (make-branch inst machine labels flag pc))
        ((eq? (car inst) 'goto)
         (make-goto inst machine labels pc))
        ((eq? (car inst) 'save)
         (make-save inst machine stack pc))
        ((eq? (car inst) 'restore)
         (make-restore inst machine stack pc))
        ((eq? (car inst) 'perform)
         (make-perform inst machine labels ops pc))
        ((eq? (car inst) 'je)
         (make-je inst machine labels ops pc))
        (else (error "Unknown instruction type -- ASSEMBLE"
                     inst))))

