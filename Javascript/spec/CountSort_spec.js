const {countSort} = require('../Sorting/CountSort');
const df = require('deep-freeze-strict');

describe('CountSort:', () => {
  it('should sort an array of integers numerically if also given the total range of integers', () => {
    // Use of deep-freeze requires functional sort w/o side-effects
    for (let i = 0; i < 50; ++i) {
      const RANGE = 1000;
      let array1 = []
      for (let i = 0; i < 1000; ++i) {
        array1.push(Math.floor((Math.random()- 0.5)*RANGE));
      }
      expect(countSort(df([...array1]), [-RANGE, RANGE])).toEqual(array1.sort((a, b) => a-b));
    }
    const array2 = [];
    const array3 = [1];
    const array4 = [-100, -100];

    expect(countSort(df([...array2]), [-100, 100])).toEqual(array2.sort((a, b) => a-b));
    expect(countSort(df([...array3]), [-100, 100])).toEqual(array3.sort((a, b) => a-b));
    expect(countSort(df([...array4]), [-100, 100])).toEqual(array4.sort((a, b) => a-b));
  });
})
