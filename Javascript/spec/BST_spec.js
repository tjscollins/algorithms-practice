const BST = require('../Data Structures/BST');

describe('BST class: ', () => {
  describe('BST constructor:', () => {
    it('should return a new BST object', () => {
      const bst = new BST();

      // Values
      expect(bst._head).toBe(null);
      expect(bst._size).toBe(0);

      // Methods
      // Insert a value into the tree
      expect(typeof bst.insert).toBe('function');

      // Search for and return a node if it exists
      expect(typeof bst.search).toBe('function');

      // Delete a node from the tree
      expect(typeof bst.delete).toBe('function');

      // Return an in-order list of all stored values
      expect(typeof bst.traverse).toBe('function');

      // Private method to create new nodes
      expect(typeof bst._newNode).toBe('function');

      // Private predecessor method
      expect(typeof bst._prev).toBe('function');

      // Private successor method
      expect(typeof bst._next).toBe('function');
    });
  });

  describe('BST.prototype.insert: ', () => {
      it('should maintain BST property after an arbitrary number of inserts', () => {
        for (let j = 0; j < 100; ++j) {
          let bst = new BST();
          for (let i = 0; i < 100; ++i) {
            bst.insert({
              key: Math.floor(Math.random() * 500),
              data: ' '
            });
          }
          expect(bst._size).toBe(100);
          expect(bst._head).not.toBe(null);
          expect(hasBstProp(bst._head)).toBe(true);
        }
      });

      it('should throw an error if the argument lacks a key value', () => {
        const bst = new BST();
        let errorThrown = false;
        try {
          bst.insert({data: 123});
        } catch (error) {
          expect(error).toBeDefined();
          errorThrown = error.message === 'Cannot create node without key value';
        }
        expect(errorThrown).toBe(true);
      });

      it('should throw an error if the argument lacks a data value', () => {
        const bst = new BST();
        let errorThrown = false;
        try {
          bst.insert({key: 123});
        } catch (error) {
          expect(error).toBeDefined();
          errorThrown = error.message === 'Cannot create node without data value';
        }
        expect(errorThrown).toBe(true);
      });
  });

  describe('BST.prototype.search: ', () => {
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

      it('should return null if the target node does not exist', () => {
        const bst = new BST();
        for (let i = 0; i < 1000; ++i) {
          let key = Math.floor(Math.random() * 1000);
          if (key !== 123 && key !== 321 && key !== 234) {
            bst.insert({key, data: ' '});
          }
        }
        expect(bst.search(123)).toBe(null);
        expect(bst.search(321)).toBe(null);
        expect(bst.search(234)).toBe(null);
      });
  });

  describe('BST.prototype.delete: ', () => {
      it('should delete a node from the tree', () => {
          const bst = new BST();
          for (let i = 0; i < 100; ++i) {
            let key = Math.floor(Math.random() * 10000);
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
          bst.delete(123);
          expect(bst.search(123)).toBe(null);
          bst.delete(321);
          expect(bst.search(321)).toBe(null);
          bst.delete(234);
          expect(bst.search(234)).toBe(null);
      });

      it('should maintain BST property after deletions', () => {
        for (let j = 0; j < 10; ++j) {
          let bst = new BST();
          for (let i = 0; i < 1000; ++i) {
            let key = Math.floor(Math.random() * 10000);
            bst.insert({key, data: ' '});
          }
          bst.delete(pickNode(bst));
          bst.delete(pickNode(bst));
          bst.delete(pickNode(bst));
          bst.delete(pickNode(bst));
          expect(hasBstProp(bst._head)).toBe(true);
          expect(bst._size).toBe(countBst(bst._head));
        }
      });
  });

  describe('BST.prototype.traverse: ', () => {
    it('should return a sorted array of all the nodes', () => {
        let bst = new BST();
        bst.insert({key: 5, data: 5});
        bst.insert({key: 2, data: 2});
        bst.insert({key: 8, data: 8});
        bst.insert({key: 1, data: 1});
        bst.insert({key: 4, data: 4});
        bst.insert({key: 3, data: 3});
        bst.insert({key: 7, data: 7});
        bst.insert({key: 6, data: 6});
        bst.insert({key: 9, data: 9});
        bst.insert({key: 10, data: 10});
        let array = bst.traverse().map(node => node.key);
        expect(array).toEqual(array.sort((a,b) => a-b));
    });
  });

  describe('BST.prototype private methods: ', () => {
    it('should find the predecessor of an arbitrary node', () => {
      let bst = new BST();
      bst.insert({key: 5, data: 5});
      bst.insert({key: 2, data: 2});
      bst.insert({key: 8, data: 8});
      bst.insert({key: 1, data: 1});
      bst.insert({key: 4, data: 4});
      bst.insert({key: 3, data: 3});
      bst.insert({key: 7, data: 7});
      bst.insert({key: 6, data: 6});
      bst.insert({key: 9, data: 9});
      bst.insert({key: 10, data: 10});
      for (let i = 10; i > 1; --i) {
        let node = bst.search(i);
        expect(bst._prev(node).key).toBe(i-1);
      }
    });

    it('should find the successor of an arbitrary node', () => {
      let bst = new BST();
      bst.insert({key: 5, data: 5});
      bst.insert({key: 2, data: 2});
      bst.insert({key: 8, data: 8});
      bst.insert({key: 1, data: 1});
      bst.insert({key: 4, data: 4});
      bst.insert({key: 3, data: 3});
      bst.insert({key: 7, data: 7});
      bst.insert({key: 6, data: 6});
      bst.insert({key: 9, data: 9});
      bst.insert({key: 10, data: 10});
      for (let i = 1; i < 10; ++i) {
        let node = bst.search(i);
        expect(bst._next(node).key).toBe(i+1);
      }
    });
  });
});

function pickNode(bst) {
  let node = bst._head;
  let iter = Math.floor(Math.random()*Math.log(bst._size))
  let next = Math.floor(Math.random()*2) > 1 ? 'left' : 'right';
  while (node[next] != null && iter > 0) {
    next = Math.floor(Math.random()*2) > 1 ? 'left' : 'right';
    node = node[next]
  }
  return node !== null && node !== bst._head ? node.key : pickNode(bst);
}


/**
 * hasBstProp - Tests a bst node and its subtrees to verify that
 *              they satisfy the bst property.
 *
 * @param  {object} node a bst node to be checked for the bst property
 * @return {bool}      true if bst property holds, false if not
 */
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
