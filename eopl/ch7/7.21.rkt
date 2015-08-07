#lang eopl


;;; We said the substitution is like a store. Implement the unifier,
;;; using the representation of substitutions from exercise 7.17,
;;; and keeping the substi-tution in a global Scheme variable,
;;; as we did in figures 4.1 and 4.2.

(define the-sub '())

(define extend-subst
  (lambda (subst tvar ty)
    (cons (cons tvar ty) subst)))

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
                            (apply-subst-to-type (cdr tmp))
                            ty))))))


(define (unifier ty1 ty2 exp)
  (let ((ty1 (apply-subst-to-type ty1 the-sub))
        (ty2 (apply-subst-to-type ty2 the-sub)))
    (cond ((equal? ty1 ty2) the-sub)
          ((tvar-type? ty1)
           (if (no-occurrence? ty1 ty2)
               ((begin
                  (set! the-sub
                        (extend-subst the-sub ty1 ty2)))
                the-sub)
               (report-no-occurrence-violation ty1 ty2 )))
          ((tvar-type2? ty2)
           (if (no-occurrence? ty2 ty1)
               ((begin
                  (set! the-sub
                        (extend-subst the-sub ty2 ty1)))
                the-sub)
               (report-no-occurrence-violation ty1 ty2 )))
          ((and (proc-type? ty1)
                (proc-type? ty2))
           (let ((subst (unifier (proc-type->arg-type ty1)
                                 (proc-type->arg-type ty2)
                                 exp)))
             (let ((subst (unifier (proc-type->arg-type ty1)
                                   (proc-type->arg-type ty2)
                                   exp)))
               the-sub)))
          (else (report-no-occurrence-violation ty1 ty2 exp)))))
