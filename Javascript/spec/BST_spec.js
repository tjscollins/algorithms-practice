const BST = require('../Data Structures/BST');

describe('BST class: ', () => {
  it('should return a new BST object', () =>{
    const bst = new BST();

    expect(bst.head).toBe(null);
    expect(typeof bst.insert).toBe('function');
    expect(typeof bst.search).toBe('function');
    expect(typeof bst.delete).toBe('function');
    expect(typeof bst.traverse).toBe('function');
    expect(typeof bst.prev).toBe('function');
    expect(typeof bst.next).toBe('function');
  });

  it('should maintain BST property after an arbitrary number of inserts', () => {
    const bst = new BST();
    for (let j = 0; j < 10; ++j) {
      for (let i = 0; i < 100; ++i) {
        bst.insert({key: Math.floor(Math.random()*10000), data: ' '});
      }
      expect(hasBstProp(bst.head)).toBe(true);
    }
    var count = 0;
    function hasBstProp(node) {
      if (node == null) {
        return true;
      }
      let left = false,
        right = false;
      if(node.left == null || node.left.key < node.key) {
        left = true;
      }
      if (node.right == null || node.right.key >= node.key) {
        right = true;
      }
      return right && left && hasBstProp(node.left) && hasBstProp(node.right);
    }
  });

  it('should search for and return a node if it exists', () => {});

  it('should support in-order traversal', () => {});

  it('should find the predecessor of an arbitrary node', () => {});

});
