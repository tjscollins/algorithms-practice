(ns clojure-algos.core-test
  (:require [clojure.test :refer :all]
            [clojure-algos.core :refer :all]
            [clojure-algos.sorting :refer :all]))

(deftest select-sort-test
  (testing "Selection sort"
    (is (=
          (sort [5 1 4 2 3])
          (select-sort [5 1 4 2 3])))))
