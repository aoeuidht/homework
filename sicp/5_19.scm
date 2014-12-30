#lang r5rs

#|
Exercise 5.19.  Alyssa P. Hacker wants a breakpoint feature in the simulator to help
 her debug her machine designs. You have been hired to install this feature for her.
 She wants to be able to specify a place in the controller sequence where the
 simulator will stop and allow her to examine the state of the machine.
 You are to implement a procedure

(set-breakpoint <machine> <label> <n>)

that sets a breakpoint just before the nth instruction after the given label. For example,

(set-breakpoint gcd-machine 'test-b 4)

installs a breakpoint in gcd-machine just before the assignment to register a.
 When the simulator reaches the breakpoint it should print the label and the
 offset of the breakpoint and stop executing instructions.
 Alyssa can then use get-register-contents and set-register-contents!
 to manipulate the state of the simulated machine.
 She should then be able to continue execution by saying

(proceed-machine <machine>)

She should also be able to remove a specific breakpoint by means of

(cancel-breakpoint <machine> <label> <n>)

or to remove all breakpoints by means of

(cancel-all-breakpoints <machine>)
|#

(define (error reason . args)
      (display "Error: ")
      (display reason)
      (for-each (lambda (arg) 
                  (display " ")
		  (write arg))
		args)
      (newline)
      (scheme-report-environment -1))
(define (tagged-list? exp tag)
  (if (pair? exp)
      (eq? (car exp) tag)
      #false))

(define (make-machine register-names ops controller-text)
  (let ((machine (make-new-machine)))
    (for-each (lambda (register-name)
                ((machine 'allocate-register) register-name))
              register-names)
    ((machine 'install-operations) ops)    
    ((machine 'install-instruction-sequence)
     (assemble controller-text machine))
    machine))

(define (make-register name)
  (let ((contents '*unassigned*))
    (define (dispatch message)
      (cond ((eq? message 'get) contents)
            ((eq? message 'set)
             (lambda (value) (set! contents value)))
            (else
             (error "Unknown request -- REGISTER" message))))
    dispatch))

(define (get-contents register)
  (register 'get))

(define (set-contents! register value)
  ((register 'set) value))

; -----------
(define (make-stack)
  (let ((s '())
        (number-pushes 0)
        (max-depth 0)
        (current-depth 0))
    (define (push x)
      (set! s (cons x s))
      (set! number-pushes (+ 1 number-pushes))
      (set! current-depth (+ 1 current-depth))
      (set! max-depth (max current-depth max-depth)))
    (define (pop)
      (if (null? s)
          (error "Empty stack -- POP")
          (let ((top (car s)))
            (set! s (cdr s))
            (set! current-depth (- current-depth 1))
            top)))    
    (define (initialize)
      (set! s '())
      (set! number-pushes 0)
      (set! max-depth 0)
      (set! current-depth 0)
      'done-reg-initialize)
    (define (print-statistics)
      (newline)
      (display (list 'total-pushes  '= number-pushes
                     'maximum-depth '= max-depth)))
    (define (dispatch message)
      (cond ((eq? message 'push) push)
            ((eq? message 'pop) (pop))
            ((eq? message 'initialize) (initialize))
            ((eq? message 'print-statistics)
             (print-statistics))
            (else
             (error "Unknown request -- STACK" message))))
    dispatch))
(define (pop stack)
  (stack 'pop))

(define (push stack value)
  ((stack 'push) value))
;-----------
(define (make-new-machine)
  (let ((pc (make-register 'pc))
        (flag (make-register 'flag))
        (stack (make-stack))
        (the-instruction-sequence '())
        (inst-counting 0)
        (inst-trace #f))
    (define (print-inst-counting)
      (display (list 'instruction-counting '= inst-counting)))
    (let ((the-ops
           (list (list 'initialize-stack
                       (lambda () (stack 'initialize)))
                 (list 'print-stack-statistics
                       (lambda () (stack 'print-statistics)))
                 (list 'initialize-inst-counting
                       (lambda () (set! inst-counting 0)))
                 (list 'print-inst-counting
                       (lambda () (print-inst-counting)))
                 ))
          (register-table
           (list (list 'pc pc) (list 'flag flag))))

      (define (trace-on)
        (set! inst-trace #t))
      (define (trace-off)
        (set! inst-trace #f))
      (define (allocate-register name)
        (if (assoc name register-table)
            (error "Multiply defined register: " name)
            (set! register-table
                  (cons (list name (make-register name))
                        register-table)))
        'register-allocated)
      (define (lookup-register name)
        (let ((val (assoc name register-table)))
          (if val
              (cadr val)
              (error "Unknown register:" name))))
      (define (execute)
        (let ((insts (get-contents pc)))
          (if (null? insts)
              'done
              (begin
                (if inst-trace
                    (begin
                      ;(display (cadaar insts))(display (car (cddaar insts)))
                      (display (caaar insts))
                      (newline)
                      'pass)
                    'pass)
                ; check the break point
                (if (caddr (cdaar insts))
                    (begin 
                           (display 'got-bp)(newline)
                           (display 'label----)(display (cadr (caar insts)))(newline)
                           (display 'inst----)(display (car (caar insts)))(newline)
                           (display 'offset----)(display (caddr (caar insts)))(newline)
                           )
                    (begin 
                      (set! inst-counting (+ inst-counting 1))
                      ((instruction-execution-proc (car insts)))
                      (execute)))))))
      (define (dispatch message)
        (cond ((eq? message 'start)
               (set-contents! pc the-instruction-sequence)
               (execute))
              ((eq? message 'get-insts) the-instruction-sequence)
              ((eq? message 'install-instruction-sequence)
               (lambda (seq) (set! the-instruction-sequence seq)))
              ((eq? message 'allocate-register) allocate-register)
              ((eq? message 'get-register) lookup-register)
              ((eq? message 'install-operations)
               (lambda (ops) (set! the-ops (append the-ops ops))))
              ((eq? message 'stack) stack)
              ((eq? message 'trace-on) (trace-on))
              ((eq? message 'trace-off) (trace-off))
              ((eq? message 'operations) the-ops)
              ((eq? message 'print-inst-counting) (print-inst-counting))
              (else (error "Unknown request -- MACHINE" message))))
      dispatch)))

;------------
(define (start machine)
  (machine 'start))
(define (get-register-contents machine register-name)
  (get-contents (get-register machine register-name)))
(define (set-register-contents! machine register-name value)
  (set-contents! (get-register machine register-name) value)
  'done)
(define (get-register machine reg-name)
  ((machine 'get-register) reg-name))

(define (set-breakpoint machine label-name offset)
  (define (set-bp-wrapper insts label-name offset)
    (if (null? insts)
        #f
        (let ((inst (caar insts)))
          (if (and (eq? label-name (cadr inst))
                   (= offset (caddr inst)))
              (set-car! (cdddr inst) #t)
              (set-bp-wrapper (cdr insts) label-name offset)))))
  (let ((insts (machine 'get-insts)))
    (set-bp-wrapper insts label-name offset)
    )
  )

(define (cancel-breakpoint machine label-name offset)
  (define (cancel-bp-wrapper insts label-name offset)
    (if (null? insts)
        #f
        (let ((inst (caar insts)))
          (if (and (eq? label-name (cadr inst))
                   (= offset (caddr inst)))
              (set-car! (cdddr inst) #f)
              (cancel-bp-wrapper (cdr insts) label-name offset)))))
  (let ((insts (machine 'get-insts)))
    (cancel-bp-wrapper insts label-name offset)
  ))

;-------------
(define (assemble controller-text machine)
  (extract-labels controller-text
    (lambda (insts labels)
      (update-insts! insts labels machine)
      insts)))
(define (extract-labels text receive)
  (if (null? text)
      (receive '() '())
      (extract-labels (cdr text)
       (lambda (insts labels)
         ;(display (cons 'inst insts))(newline)(display labels)(newline)
         (let ((next-inst (car text))
               (label-inst-count 1))
           (if (symbol? next-inst)
               (begin
                 (set! label-inst-count 1)
                 (for-each (lambda (inst)
                             (if (null? (cadar inst))
                                 (begin
                                   (set-car! (cdar inst) next-inst)
                                   (set-car! (cddar inst) label-inst-count)
                                   (set! label-inst-count (+ label-inst-count 1))
                                   )
                                 'done)
                             )
                           insts)
                 ;(display insts)
                 (newline)
                 (receive insts
                          (cons (make-label-entry next-inst
                                                  insts)
                                labels)))
               (receive (cons (make-instruction next-inst)
                              insts)
                        labels)))))))
(define (update-insts! insts labels machine)
  (let ((pc (get-register machine 'pc))
        (flag (get-register machine 'flag))
        (stack (machine 'stack))
        (ops (machine 'operations)))
    (for-each
     (lambda (inst)
       (set-instruction-execution-proc! 
        inst
        (make-execution-procedure
         (instruction-text inst) labels machine
         pc flag stack ops)))
     insts)))
(define (make-instruction text)
  ; make car a (text, label, index, breakpoint list)
  (cons (list text '() 0 #f) '()))
(define (instruction-text inst)
  (caar inst))
(define (instruction-execution-proc inst)
  (cdr inst))
(define (set-instruction-execution-proc! inst proc)
  (set-cdr! inst proc))

(define (make-label-entry label-name insts)
  (cons label-name insts))
(define (lookup-label labels label-name)
  (let ((val (assoc label-name labels)))
    (if val
        (cdr val)
        (error "Undefined label -- ASSEMBLE" label-name))))

;---------------
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
        (else (error "Unknown instruction type -- ASSEMBLE"
                     inst))))
(define (make-assign inst machine labels operations pc)
  (let ((target
         (get-register machine (assign-reg-name inst)))
        (value-exp (assign-value-exp inst)))
    (let ((value-proc
           (if (operation-exp? value-exp)
               (make-operation-exp
                value-exp machine labels operations)
               (make-primitive-exp
                (car value-exp) machine labels))))
      (lambda ()                ; execution procedure for assign
        (set-contents! target (value-proc))
        (advance-pc pc)))))

(define (assign-reg-name assign-instruction)
  (cadr assign-instruction))
(define (assign-value-exp assign-instruction)
  (cddr assign-instruction))
(define (advance-pc pc)
  (set-contents! pc (cdr (get-contents pc))))
(define (make-test inst machine labels operations flag pc)
  (let ((condition (test-condition inst)))
    (if (operation-exp? condition)
        (let ((condition-proc
               (make-operation-exp
                condition machine labels operations)))
          (lambda ()
            (set-contents! flag (condition-proc))
            (advance-pc pc)))
        (error "Bad TEST instruction -- ASSEMBLE" inst))))
(define (test-condition test-instruction)
  (cdr test-instruction))
(define (make-branch inst machine labels flag pc)
  (let ((dest (branch-dest inst)))
    (if (label-exp? dest)
        (let ((insts
               (lookup-label labels (label-exp-label dest))))
          (lambda ()
            (if (get-contents flag)
                (set-contents! pc insts)
                (advance-pc pc))))
        (error "Bad BRANCH instruction -- ASSEMBLE" inst))))
(define (branch-dest branch-instruction)
  (cadr branch-instruction))
(define (make-goto inst machine labels pc)
  (let ((dest (goto-dest inst)))
    (cond ((label-exp? dest)
           (let ((insts
                  (lookup-label labels
                                (label-exp-label dest))))
             (lambda () (set-contents! pc insts))))
          ((register-exp? dest)
           (let ((reg
                  (get-register machine
                                (register-exp-reg dest))))
             (lambda ()
               (set-contents! pc (get-contents reg)))))
          (else (error "Bad GOTO instruction -- ASSEMBLE"
                       inst)))))
(define (goto-dest goto-instruction)
  (cadr goto-instruction))

(define (make-save inst machine stack pc)
  (let ((reg (get-register machine
                           (stack-inst-reg-name inst))))
    (lambda ()
      (push stack (get-contents reg))
      (advance-pc pc))))
(define (make-restore inst machine stack pc)
  (let ((reg (get-register machine
                           (stack-inst-reg-name inst))))
    (lambda ()
      (set-contents! reg (pop stack))    
      (advance-pc pc))))
(define (stack-inst-reg-name stack-instruction)
  (cadr stack-instruction))

(define (make-perform inst machine labels operations pc)
  (let ((action (perform-action inst)))
    (if (operation-exp? action)
        (let ((action-proc
               (make-operation-exp
                action machine labels operations)))
          (lambda ()
            (action-proc)
            (advance-pc pc)))
        (error "Bad PERFORM instruction -- ASSEMBLE" inst))))
(define (perform-action inst) (cdr inst))

; -----------
(define (make-primitive-exp exp machine labels)
  (cond ((constant-exp? exp)
         (let ((c (constant-exp-value exp)))
           (lambda () c)))
        ((label-exp? exp)
         (let ((insts
                (lookup-label labels
                              (label-exp-label exp))))
           (lambda () insts)))
        ((register-exp? exp)
         (let ((r (get-register machine
                                (register-exp-reg exp))))
           (lambda () (get-contents r))))
        (else
         (error "Unknown expression type -- ASSEMBLE" exp))))
(define (register-exp? exp) (tagged-list? exp 'reg))
(define (register-exp-reg exp) (cadr exp))
(define (constant-exp? exp) (tagged-list? exp 'const))
(define (constant-exp-value exp) (cadr exp))
(define (label-exp? exp) (tagged-list? exp 'label))
(define (label-exp-label exp) (cadr exp))


(define (make-operation-exp exp machine labels operations)
  (let ((op (lookup-prim (operation-exp-op exp) operations))
        (aprocs
         (map (lambda (e)
                (make-primitive-exp e machine labels))
              (operation-exp-operands exp))))
    (lambda ()
      (apply op (map (lambda (p) (p)) aprocs)))))

(define (operation-exp? exp)
  (and (pair? exp) (tagged-list? (car exp) 'op)))
(define (operation-exp-op operation-exp)
  (cadr (car operation-exp)))
(define (operation-exp-operands operation-exp)
  (cdr operation-exp))

(define (lookup-prim symbol operations)
  (let ((val (assoc symbol operations)))
    (if val
        (cadr val)
        (error "Unknown operation -- ASSEMBLE" symbol))))

(define gcd-machine
  (make-machine
   '(continue n val)
   (list (list 'rem remainder) (list '= =) (list '- -) (list '< <) (list '+ +) (list '* *))
   '(controller
   (assign continue (label fact-done))     ; set up final return address
 fact-loop
   (test (op =) (reg n) (const 1))
   (branch (label base-case))
   ;; Set up for the recursive call by saving n and continue.
   ;; Set up continue so that the computation will continue
   ;; at after-fact when the subroutine returns.
   (save continue)
   (save n)
   (assign n (op -) (reg n) (const 1))
   (assign continue (label after-fact))
   (goto (label fact-loop))
 after-fact
   (restore n)
   (restore continue)
   (assign val (op *) (reg n) (reg val))   ; val now contains n(n - 1)!
   (goto (reg continue))                   ; return to caller
 base-case
   (assign val (const 1))                  ; base case: 1! = 1
   (goto (reg continue))                   ; return to caller
 fact-done)))

(set-register-contents! gcd-machine 'continue 0)
(set-register-contents! gcd-machine 'val 0)
(set-register-contents! gcd-machine 'n 10)
(display (start gcd-machine))
(display (get-register-contents gcd-machine 'val))
((gcd-machine 'stack) 'print-statistics)
((gcd-machine 'stack) 'initialize)
(set-register-contents! gcd-machine 'continue 0)
(set-register-contents! gcd-machine 'val 0)
(set-register-contents! gcd-machine 'n 10)
;(gcd-machine 'trace-on)
(display (start gcd-machine))
(display (get-register-contents gcd-machine 'val))
((gcd-machine 'stack) 'print-statistics)

(define (run-and-stat n machine)
  ((machine 'stack) 'initialize)
  (set-register-contents! machine 'continue 0)
  (set-register-contents! machine 'val 0)
  (set-register-contents! machine 'n n)
  (set-breakpoint gcd-machine 'after-fact 3)
  (start machine)
  (display (get-register-contents machine 'val))
  ((machine 'stack) 'print-statistics)
  ;(machine 'print-inst-counting)
  (newline))

(define range
  (lambda (n . m)
    (let
      ((n (if (null? m) 0 n)) (m (if (null? m) n (car m))))
      (cond
    ((= n m) (list n))
    (else (cons n (range ((if (< n m) + -) n 1) m)))))))

(map (lambda (n) (run-and-stat n gcd-machine))
     (range 1 10))

(set-breakpoint gcd-machine 'after-fact 3)
;(cancel-breakpoint gcd-machine 'after-fact 3)