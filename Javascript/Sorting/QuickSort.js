function quickSort(array) {
  if(array.length <= 1) {
    return array;
  }

  let piv = Math.floor(Math.random()*array.length);
  let [L, M, R] = [[], [], []];
  array.forEach((value) => {
    if(value < array[piv]) {
      L.push(value);
    } else if (value > array[piv]) {
      R.push(value);
    } else {
      M.push(value);
    };
  });

  return quickSort(L).concat(M.concat(quickSort(R)));
}

module.exports = {
  quickSort
};
