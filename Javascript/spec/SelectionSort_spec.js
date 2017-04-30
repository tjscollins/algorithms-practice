const {selectSort} = require('../Sorting/SelectionSort');
const df = require('deep-freeze-strict');

describe('SelectionSort:', () => {
  it('should sort arrays numerically', () => {
    // Use of deep-freeze requires functional sort w/o side-effects
    const array1 = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 15, 13, 11, 14, 12];
    const array2 = [100, -100, 2, 3, 4, -10, -9, -8, 7, 6, -5, 4, -4, 3, -2, 1, 0];
    const array3 = [200, 2, -2, 3, 4, 400, -300, 100, 5, 7, 6, -8, -10, 9];
    const array4 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const array5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10];
    expect(selectSort(df(Object.assign([], array1)))).toEqual(array1.sort((a, b) => a-b));
    expect(selectSort(df(Object.assign([], array2)))).toEqual(array2.sort((a, b) => a-b));
    expect(selectSort(df(Object.assign([], array3)))).toEqual(array3.sort((a, b) => a-b));
    expect(selectSort(df(Object.assign([], array4)))).toEqual(array4.sort((a, b) => a-b));
    expect(selectSort(df(Object.assign([], array5)))).toEqual(array5.sort((a, b) => a-b));

  });
})
