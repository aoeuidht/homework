; 3.59

; a)
(define (integrate-series s)
  (stream-map /
              s
              integres))

; b)
(define cosine-series
  (cons-stream 1
               (stream-map (lambda (x) (* -1 x))
                           (integrate-series sine-series))))

(define sine-series
  (cons-stream 0
               (integrate-series cosine-series)))