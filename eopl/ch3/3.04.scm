#lang eopl

#|
Write out the derivation of figure 3.4 as a derivation tree in the style of the one on page 5.
|#

#|
(value-of << x >> rho) = (num-val 33) (value-of << 11 >> rho) = (num-val 11)
---------------------------------------------------------------------------
(value-of << zero?(-(33, 22)) >> rho)) = (bool-val #f)
---------------------------------------------------------------------------
(value-of <<if #f then -(y, 2) else -(y, 4)>> rho) = (value-of << -(y, 4) >> rho)
---------------------------------------------------------------------------
(value-of << y >> rho) = (num-val 22) (value-of << 4 >> rho) = (num-val 4)
---------------------------------------------------------------------------
(value-of << -(22, 4) >> rho) = (num-val 18)
|#
