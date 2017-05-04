(ns clojure-algos.sorting
  (:gen-class))

(defn select-sort
  "Implementation of selection sort.  Currently clobbers duplicates and effectively returns a sorted set due to the use of the filter function.  Not sure how to fix this."
  [vec]
  (loop [sorted [] unsorted vec]
    (if (not (= 0 (count unsorted)))
      (recur
        (conj sorted (apply min unsorted))
        (filter #(not (= (apply min unsorted) %)) unsorted))
      (lazy-seq sorted))))
