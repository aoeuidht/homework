#lang racket
; Exercise 2.11. In passing, Ben also cryptically comments: ``By testing the signs of the endpoints of the intervals,
; it is possible to break mul-interval into nine cases,
; only one of which requires more than two multiplications.'' 
; Rewrite this procedure using Ben's suggestion.

; Answer:
; Here I will list the nine scenarios (asume x has bigger width than y):
; x           |__________________________|
; y |______|

; x           |__________________________|
; y    |______|

; x           |__________________________|
; y       |______|

; x           |__________________________|
; y           |______|

; x           |__________________________|
; y                |______|

; x           |__________________________|
; y                               |______|

; x           |__________________________|
; y                                  |______|

; x           |__________________________|
; y                                      |______|

; x           |__________________________|
; y                                            |______|

; And only the following scenario needs more than 2 multiplication operation
; x           |__________________________|
; y                |______|