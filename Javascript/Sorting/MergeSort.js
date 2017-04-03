function mergeSort(array) {
  if (array.length <= 1) {
    return array;
  }

  function merge(a, b) {
    let m = [];
    while (a.length > 0 && b.length > 0) {
      if (a[0] < b[0]) {
        m.push(a.shift());
      } else {
        m.push(b.shift());
      }
    }
    if (a.length >0 ) {
      m = m.concat(a);
    }
    if(b.length > 0) {
      m = m.concat(b);
    }
    return m;
  }

  return merge(mergeSort(array.slice(0, Math.floor(array.length / 2))), mergeSort(array.slice(Math.floor(array.length / 2))));
}

module.exports = {
  mergeSort,
};
