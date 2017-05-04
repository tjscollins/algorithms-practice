
function countSort(arr, range) {
  let [min, max] = range;
  let count = [];

  for(let i = 0; i < arr.length; ++i) {
    if (count[arr[i]]) {
      count[arr[i]]++;
    } else {
      count[arr[i]] = 1;
    }
  }

  let result = [];
  for (let j = min; j <= max; j++) {
    if(count[j]) {
      for (let k = count[j]; k > 0; --k) {
        result.push(j);
      }
    }
  }
  return result;
}

module.exports = {
  countSort,
};
