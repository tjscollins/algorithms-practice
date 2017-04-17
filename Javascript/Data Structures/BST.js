class BST {
  constructor() {
    this._head = null;
    this._size = 0;
  }
  insert(data) {
    let {_newNode} = this;
    if (data.key == undefined) {
      throw new Error('Cannot create node without key value');
    } else if (data.data == undefined) {
      throw new Error('Cannot create node without data value');
    }

    if (this._head === null) {
      this._head = _newNode(data, null);
      this._size++;
    } else {
      let node = this._head;
      while (node !== null) {
        let {key} = node;
        if(data.key < key) {
          if(node.left === null) {
            node.left = _newNode(data, node);
            this._size++;
            node = null;
          } else {
            node = node.left;
          }
        } else if(data.key > key) {
          if(node.right === null) {
            node.right = _newNode(data, node);
            this._size++;
            node = null;
          } else {
            node = node.right;
          }
        } else {
          // ignore duplicate keys
        }
      }
    }
  }
  search(key) {
    if (this._head === null) {
      return null;
    }

    let node = this._head;
    while(node !== null) {
      if (key < node.key) {
        node = node.left;
      } else if (key > node.key) {
        node = node.right;
      } else {
        return node;
      }
    }
    return null;
  }
  delete(key, Node) {
    if (Node === undefined) {
      // Find the relevant node
      let node = this._head;
      while(node !== null) {
        if (key < node.key) {
          node = node.left;
        } else if (key > node.key) {
          node = node.right;
        } else {
          break;
        }
      }
      if (node === null) {
        return; //Node does not exist
      } else if (node === this._head) {
        // throw new Error('Deleting head node');
      }
      Node = node;
    }

    if (Node.left === null || Node.right === null) {
      if (Node === Node.parent.left) {
        Node.parent.left = Node.left || Node.right;
        if (Node.parent.left !== null) {
          Node.parent.left.parent = Node.parent;
        }
      } else {
        Node.parent.right = Node.left || Node.right;
        if (Node.parent.right !== null) {
          Node.parent.right.parent = Node.parent;
        }
      }
      this._size--;
      return Node;
    } else {
      let n = this._next(Node);
      [n.key, Node.key] = [Node.key, n.key];
      [n.data, Node.data] = [Node.data, n.data];
      process.nextTick(() => {
        this.delete(null, n);
      });
    }
  }
  traverse() {
    let min = this._head;
    while (min.left !== null) {
      min = min.left;
    }
    let array = [{key: min.key, data: min.data}];
    let current = this._next(min);
    while (current !== null) {
      array.push({key: current.key, data: current.data});
      current = this._next(current);
    }
    return array;
  }
  _prev(node) {
    if (node.left !== null) {
      let n = node.left;
      while (n.right !== null) {
        n = n.right;
      }
      return n;
    }
    let current = node;
    while (current.parent !== null && current === current.parent.left) {
      current = current.parent;
    }
    return current.parent;
  }
  _next(node) {
    if (node.right !== null) {
      let n = node.right;
      while (n.left !== null) {
        n = n.left;
      }
      return n;
    }
    let current = node;
    while (current.parent !== null && current === current.parent.right) {
      current = current.parent;
    }
    return current.parent;
  }
  _newNode(data, parent) {
    return {key: data.key, data: data.data, left: null, right: null, parent,};
  }
}

module.exports = BST;
