#lang racket
#|
Exercise 5.8.  The following register-machine code is ambiguous, because the label here is defined more than once:

start
  (goto (label here))
here
  (assign a (const 3))
  (goto (label there))
here
  (assign a (const 4))
  (goto (label there))
there

With the simulator as written, what will the contents of register a be when control reaches there? Modify the extract-labels procedure so that the assembler will signal an error if the same label name is used to indicate two different locations. 
|#

; Answer
#| 
first, let's see how the label handling part in  extract-lables works
(if (symbol? next-inst)
    (receive insts
             (cons (make-label-entry next-inst
                                     insts)
                   labels))
    (receive (cons (make-instruction next-inst)
                   insts)
             labels))

so the 
(cons (make-label-entry next-inst
                        insts)
      labels)
part doesn't check if the labels in unique before add a labels to the labels list

so we have to check weather the new labe already exists
|#

(define (label-exists? label labels)
  (if (null? labels)
      #f
      (if (= label (caar labels))
          #t
          (label-exists? label (cdr labels)))))

(define (extract-labels text receive)
  (if (null? text)
      (receive '() '())
      (extract-labels (cdr text)
       (lambda (insts labels)
         (let ((next-inst (car text)))
           (if (symbol? next-inst)
               (if (label-exists? next-inst labels)
                   (error 'label-exists)
                   (receive insts
                            (cons (make-label-entry next-inst
                                                    insts)
                                  labels)))
               (receive (cons (make-instruction next-inst)
                              insts)
                        labels)))))))
