function selectSort(array) {
  const count = array.length;
  let sortedArray = [];
  let plucked = [];
  for (let i = 0; i < count; i++) {
    let min = Infinity;
    for (let j = 0; min === Infinity; j++) {
      if (plucked.indexOf(j) === -1) {
        min = j;
      }
    }
    for (let j = min; j < count; j++) {
      if (array[j] < array[min] && plucked.indexOf(j) === -1) {
        min = j;
      }
    }
    sortedArray.push(array[min]);
    plucked.push(min);
  }
  return sortedArray;
}

module.exports = {
  selectSort
};
