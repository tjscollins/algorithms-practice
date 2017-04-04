const Heap = require('../Data Structures/Heap');

describe('Heap class: ', () => {
  it('should return a new Heap object', () => {
    let heap = new Heap();
    expect(heap._data).toBeDefined();
    expect(heap.top).toBeDefined();
    expect(heap.insert).toBeDefined()
    expect(heap.extract).toBeDefined();
    expect(heap.replaceTop).toBeDefined();
  });

  it('should keep largest element at the top of a max heap', () => {
    let heap = new Heap();
    heap
      .insert(1)
      .insert(2)
      .insert(3)
      .insert(4);
    expect(heap._data[0]).toBe(4);
    heap
      .insert(5)
      .insert(6)
      .insert(7);
    expect(heap._data[0]).toBe(7);
  });

  it('should keep smallest element at the top of a min heap', () => {
    let heap = new Heap([], 'min');
    heap
      .insert(1)
      .insert(2)
      .insert(3)
      .insert(4);
    expect(heap._data[0]).toBe(1);
    heap
      .insert(-1)
      .insert(-2)
      .insert(-3);
    expect(heap._data[0]).toBe(-3);
  });

  it('should create a heap of the correct type from an array', () => {
    let heap = new Heap([1,2,3,4,5,6,7,8]);
    expect(heap._data[0]).toBe(8);
    heap = new Heap([-1,-2,-3,0,9,8,7,6,5,4,3,2,1], 'min');
    expect(heap._data[0]).toBe(-3);
  });

  it('should extract the top of the heap and then fix the heap', () => {
    let heap = new Heap([0,-2,-3,-1,-4,-5,-6,9,8,7,6,5,4,3,2,1])
    expect(heap.extract()).toBe(9);
    expect(heap._data[0]).toBe(8);
  });

  it('should replace the element at the top of the heap and then fix the heap', () => {
    let heap = new Heap([0,-2,-3,-1,-4,-5,-6,9,8,7,6,5,4,3,2,1])
    expect(heap.replaceTop(-100)).toBe(9);
    expect(heap._data[0]).toBe(8);
  });
});
