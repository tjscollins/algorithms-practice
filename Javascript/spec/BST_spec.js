const BST = require('../Data Structures/BST');

describe('BST class: ', () => {
  it('should return a new BST object', () => {
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
    for (let j = 0; j < 100; ++j) {
      for (let i = 0; i < 100; ++i) {
        bst.insert({
          key: Math.floor(Math.random() * 500),
          data: ' '
        });
      }
      expect(hasBstProp(bst.head)).toBe(true);
    }
  });

  it('should search for and return a node if it exists', () => {
    const bst = new BST();
    for (let i = 0; i < 1000; ++i) {
      let key = Math.floor(Math.random() * 1000);
      if (key !== 123 && key !== 321 && key !== 234) {
        bst.insert({key, data: ' '});
      }
    }
    bst.insert({key: 123, data: 'a'});
    bst.insert({key: 321, data: 'b'});
    bst.insert({key: 234, data: 'c'});

    expect(bst.search(123).data).toBe('a');
    expect(bst.search(321).data).toBe('b');
    expect(bst.search(234).data).toBe('c');
  });

  it('should delete a node from the tree', () => {
    const bst = new BST();
    for (let i = 0; i < 1000; ++i) {
      let key = Math.floor(Math.random() * 1000);
      if (key !== 123) {
        bst.insert({key, data: ' '});
      }
    }
    bst.insert({key: 123, data: 'a'});
    expect(bst.search(123).data).toBe('a');
    bst.delete(123);
    expect(bst.search(123)).toBe(null);
  });

  it('should maintain BST property after deletions', () => {
    for (let j = 0; j < 10; ++j) {
      let bst = new BST();
      for (let i = 0; i < 1000; ++i) {
        let key = Math.floor(Math.random() * 1000);
        bst.insert({key, data: ' '});
      }
      bst.delete(pickNode(bst));
      bst.delete(pickNode(bst));
      bst.delete(pickNode(bst));
      bst.delete(pickNode(bst));
      expect(hasBstProp(bst.head)).toBe(true);
      expect(bst.size).toBe(countBst(bst.head));
      console.log(bst);

    }
  });

  it('should support in-order traversal', () => {});

  it('should find the predecessor of an arbitrary node', () => {});

});

function pickNode(bst) {
  let node = bst.head;
  let iter = Math.floor(Math.random()*Math.log(bst.size))
  let next = Math.floor(Math.random()*2) > 1 ? 'left' : 'right';
  while (node[next] != null && iter > 0) {
    next = Math.floor(Math.random()*2) > 1 ? 'left' : 'right';
    node = node[next]
  }
  return node !== null && node !== bst.head ? node.key : pickNode(bst);
}
function hasBstProp(node) {
  if (node == null) {
    return true;
  }
  let left = false,
    right = false;
  if (node.left == null || node.left.key < node.key) {
    left = true;
  }
  if (node.right == null || node.right.key >= node.key) {
    right = true;
  }
  return right && left && hasBstProp(node.left) && hasBstProp(node.right);
}

function countBst(node) {
  if (node == null) {
    return 0;
  } else {
    return 1 + countBst(node.left) + countBst(node.right);
  }

}
