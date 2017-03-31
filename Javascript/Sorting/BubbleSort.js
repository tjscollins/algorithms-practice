function bubbleSort(array) {
  let arr = [...array];
  for (let i =0; i< arr.length; ++i){
    for (let j = 0; j< arr.length; ++j) {
      if (arr[j] < arr[j-1]) {
        [arr[j-1], arr[j]] = [arr[j], arr[j-1]]
      }
    }
  }
  return arr;
}

module.exports = {
  bubbleSort
}
