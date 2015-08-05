#lang eopl

;;; We wrote: “If ty1 is an unknown type, then the no-occurrence invariant tells
;;; us that it is not bound in the substitution.” Explain in detail why this is so.


;;; Answer:
;;; there are 2 cases.

;;; scenario 1
;;; in substitution, t1 doesn't be bound at all, so it's totally ok.

;;; scenario 2
;;; there is a bound like (cons t1 ty1), ty1 is also a tvar-type, so
;;; it must be unbount. If not, there will be a bound like
;;; (cons ty1 blah-blah), which is conflict with the occurrence rule,
;;; because ty1 appears on both sides of the substitution.
