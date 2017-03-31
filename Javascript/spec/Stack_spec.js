const Stack = require('../Data Structures/Stack');

describe('Stack class', () => {
  it('should return a new Stack object', () => {
    const stack = new Stack();
    expect(typeof stack).toBe('object');
    expect(Array.isArray(stack._stack)).toBe(true);
    expect(typeof stack.push).toBe('function');
    expect(typeof stack.pop).toBe('function');
    expect(typeof stack.list).toBe('function');
  });

  it('should push new items onto the top of the Stack', () => {
    const stack = new Stack();

    stack.push(1);
    expect(stack.top()).toBe(1);
    stack.push(2);
    expect(stack.top()).toBe(2);
    stack.push(3);
    expect(stack.top()).toBe(3);
    stack.push(4);
    expect(stack.top()).toBe(4);
  });

  it('should pop items off the top of the Stack', () => {
    const stack = new Stack();
    stack._stack = [1,2,3,4,5,6];
    while(stack.top()) {
      expect(stack.top()).toBe(stack.pop());
    }
  });

  it('should list the whole Stack', () => {
    const stack = new Stack();
    stack._stack = [1,2,3,4,5,6];
    expect(stack.list()).toBe('6 5 4 3 2 1');
  })
});
