#lang racket
#|
registersz:
continue -> where to go
tree -> the tree
result -> the final result
tmp-rst -> the tmp for recursion call
|#


; a
(controller
 (assign continue 'cl-done)
 (assign result (const 0))
 (assign tmp-rst (cont 0))
 count-leaves
 (test (op pair?) (reg tree))
 (goto (label 'left-tree))
 
 blank-tree
 (test (op null?) (reg tree))
 (assign result (const 0))
 (assign result (const 1))
 (goto (reg continue))
 
 left-tree
 (save continue)
 (save tree)
 (save result)
 ;;;;;
 (assign tree (op car) (reg tree))
 (assign result (const 0))
 (assign continue 'left-done)
 (goto (label 'count-leaves))
 left-done
 (assign tmp-rst (reg result))
 (restore result)
 (restore tree)
 (assign result (op '+) (reg result) (reg tmp-rst))
 
 right-tree
 (save result)
 (assign tree (op cdr) (reg tree))
 (assign result (const 0))
 (assign continue 'right-done)
 (goto (label 'count-leaves))
 right-done
 (assign tmp-rst (reg result))
 (restore result)
 (assign result (op '+) (reg result) (reg tmp-rst))
 
 (restore continue)
 (goto (reg continue))
 cl-done)

;b

(controller
 (assign continue (label 'cl-done))
 (assign result (const 0))
 count-iter
 (test (op pair?) (reg tree))
 (goto (label 'sub-tree-car))
 
 no-sub-tree
 (test (op null?) (reg tree))
 (assign result (const 0))
 (assign result (const 1))
 (goto (reg continue))
 
 sub-tree-car
 (save continue)
 (save result)
 (save tree)
 (assign tree (op car) (reg tree))
 (assign continue (label 'sub-tree-cdr))
 (goto (label 'count-iter))
 
 sub-tree-cdr
 (restore tree)
 (restore tmp-rst)
 (assign result (op '+) (reg result) (reg tmp-rst))
 (assign continue (label 'count-iter-done))
 (assign tree (op cdr) (reg tree))
 (save result)
 (goto (label 'count-iter))
 count-iter-done
 (restore tmp-rst)
 (assign result (op '+) (reg result) (reg tmp-rst))
 (restore continue)
 (goto (reg continue))
 cl-done)