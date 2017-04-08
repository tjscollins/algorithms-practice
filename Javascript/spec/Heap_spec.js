const Heap = require('../Data Structures/Heap');

describe('Heap class: ', () => {
  it('should return a new Heap object', () => {
    let heap = new Heap();
    // Values
    expect(heap._data).toBeDefined();
    expect(heap._type).toBeDefined();
    expect(heap._size).toBeDefined();

    // Methods:
    // Return top element of the heap
    expect(heap.top).toBeDefined();

    // Insert new elements into heap
    expect(heap.insert).toBeDefined()

    // Remove and return top element from heap
    expect(heap.extract).toBeDefined();

    // Replace top element with new element
    expect(heap.replaceTop).toBeDefined();

    // Private method to build heap from array
    expect(heap._buildHeap).toBeDefined();

    // Private method to fix single violation of heap property
    expect(heap._fixHeapProp).toBeDefined();
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
    let heap = new Heap([
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8
    ]);
    expect(heap._data[0]).toBe(8);
    heap = new Heap([
      -1,
      -2,
      -3,
      0,
      9,
      8,
      7,
      6,
      5,
      4,
      3,
      2,
      1
    ], 'min');
    expect(heap._data[0]).toBe(-3);
  });

  it('should extract the top of the heap and then fix the heap', () => {
    let heap = new Heap([
      0,
      -2,
      -3,
      -1,
      -4,
      -5,
      -6,
      9,
      8,
      7,
      6,
      5,
      4,
      3,
      2,
      1
    ])
    expect(heap.extract()).toBe(9);
    expect(heap._data[0]).toBe(8);
    expect(heap._data[1] < heap._data[0]).toBe(true);
  });

  it('should replace the element at the top of the heap and then fix the heap', () => {
    let heap = new Heap([
      0,
      -2,
      -3,
      -1,
      -4,
      -5,
      -6,
      9,
      8,
      7,
      6,
      5,
      4,
      3,
      2,
      1
    ])
    expect(heap.replaceTop(-100)).toBe(9);
    expect(heap._data[0]).toBe(8);
  });

  it('should implement heapsort on an array', () => {
    let heap = new Heap([
      0,
      -2,
      -3,
      -1,
      -4,
      -5,
      -6,
      9,
      8,
      7,
      6,
      5,
      4,
      3,
      2,
      1
    ])
    expect(heap.sort()).toEqual([
      0,
      -2,
      -3,
      -1,
      -4,
      -5,
      -6,
      9,
      8,
      7,
      6,
      5,
      4,
      3,
      2,
      1
    ].sort((a, b) => a - b));
    heap = new Heap([
      1,
      -3,
      2,
      -5,
      4,
      -6,
      7,
      -9,
      8,
      -10,
      11,
      12,
      -1,
      2,
      -10,
      10
    ])
    expect(heap.sort()).toEqual([
      1,
      -3,
      2,
      -5,
      4,
      -6,
      7,
      -9,
      8,
      -10,
      11,
      12,
      -1,
      2,
      -10,
      10
    ].sort((a, b) => a - b));
  });
});
