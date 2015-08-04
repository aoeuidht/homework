#lang eopl

;;; Implement an alternate representation in which extend-subst is
;;; implemented as

(define extend-subst
  (lambda (subst tvar ty)
    (cons (cons tvar ty) subst)))

;;; and the extra work is shifted to apply-subst-to-type.

(define apply-subst-to-type
  (lambda (ty subst)
    (cases type ty
           (int-type () (int-type))
           (bool-type () (bool-type))
           (proc-type (t1 t2)
                      (proc-type
                       (apply-subst-to-type t1 subst) (apply-subst-to-type t2 subst)))
           (tvar-type (sn)
                      (let ((tmp (assoc ty subst)))
                        (if tmp
                            ;; since the cdr may be a tvar-type, we call it
                            ;; recursively
                            (let ((rst (apply-subst-to-type (cdr tmp))))
                              (set-cdr! tmp rst)
                              rst)
                            ;; if we find the type, we set it back
                            ty))))))
