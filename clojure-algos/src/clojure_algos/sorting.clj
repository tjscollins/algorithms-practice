(ns clojure-algos.sorting
  (:gen-class))

(defn select-sort
  [vec]
  (loop [sorted [] unsorted vec]
    (if (not (= 0 (count unsorted)))
      (recur
        (conj sorted (apply min unsorted))
        (filter #(not (= (apply min unsorted) %)) unsorted))
      (lazy-seq sorted))))
