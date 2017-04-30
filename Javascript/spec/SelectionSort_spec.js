const {selectSort} = require('../Sorting/SelectionSort');
const df = require('deep-freeze-strict');

describe('SelectionSort:', () => {
  it('should sort arrays numerically', () => {
    const array1 = [0,9,8,7,6,5,4,3,2,1];
    const array2 = [100, -100, 2, 3, 4, -10, -9, -8, 7, 6, -5, 4, -4, 3, -2, 1, 0];
    const array3 = [200, 2, -2, 3, 4, 400, -300, 100, 5, 7, 6, -8, -10, 9];
    // selectSort(df(array1))
    expect(selectSort(df(Object.assign([], array1)))).toEqual(array1.sort((a, b) => a-b));
    expect(selectSort(df(Object.assign([], array2)))).toEqual(array2.sort((a, b) => a-b));
    expect(selectSort(df(Object.assign([], array3)))).toEqual(array3.sort((a, b) => a-b));
  });
})
