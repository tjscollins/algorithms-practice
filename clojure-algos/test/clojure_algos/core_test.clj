(ns clojure-algos.core-test
  (:require [clojure.test :refer :all]
            [clojure-algos.core :refer :all]
            [clojure-algos.sorting :refer :all]))

(deftest select-sort-test
  (testing "Selection sort"
    (let [arr [5 -4 3 -2 1 0 -1 2 -3 4 -5]]
      (is (=
            (sort arr)
            (select-sort arr))))

    (let [arr [1]]
      (is (=
            (sort arr)
            (select-sort arr))))
            
    (let [arr [10 10 10]]
      (is (=
            (sort arr)
            (select-sort arr))))
  ))
