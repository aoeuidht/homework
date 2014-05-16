#lang racket
; Exercise 2.71. Suppose we have a Huffman tree for an alphabet of n symbols, and that the relative frequencies of the symbols
; are 1, 2, 4, ..., 2n-1. Sketch the tree for n=5; for n=10. In such a tree (for general n)
; how may bits are required to encode the most frequent symbol? the least frequent symbol?

; Answer
; if we have a list with ferquence 1, 2, 4, 8
; as the procedure in 2.69, two smallest leaf merge to one tree, 
; so it would be (((1 2) 4) 8)
; so with n-nodes list, the most frequent symbol take 1 bit,  the least  frequent symbol use n-1 bits