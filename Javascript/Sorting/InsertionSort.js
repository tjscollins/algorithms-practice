function insertionSort(array) {
  let sortedArray = [...array];
  for (let a = 1; a<sortedArray.length; ++a) {
    for (let i = a-1; i >= 0; --i) {
      if (sortedArray[i] > sortedArray[i+1]) {
        [sortedArray[i], sortedArray[i+1]] = [sortedArray[i+1], sortedArray[i]];
      }
    }
  }
  return sortedArray;
}

module.exports = {
  insertionSort
};
