const BST = require('./BST');

class AVL extends BST {
  constructor() {
    super();
  }

  insert(data) {
    let {_newNode} = this;
    if (data.key == undefined) {
      throw new Error('Cannot create node without key value');
    } else if (data.data == undefined) {
      throw new Error('Cannot create node without data value');
    }

    if (this._head == null) {
      this._head = _newNode(data, null);
      this._size++;
    } else {
      let node = this._head;
      while (node !== null) {
        let {key} = node;
        if(data.key < key) {
          if(node.left == null) {
            node.left = _newNode(data, node);
            this._size++;
            node.setHeight();
            this._fixAvl(node.parent);
            node = null;
          } else {
            node = node.left;
          }
        } else if (data.key > key) {
          if(node.right == null) {
            node.right = _newNode(data, node);
            this._size++;
            node.setHeight();
            this._fixAvl(node.parent);
            node = null;
          } else {
            node = node.right;
          }
        } else {
          // Ignore duplicate keys
          node = null;
        }
      }
    }
  }

  delete(key, Node) {
    if (!key && !Node) {
      throw new Error('Must provide one of (key, Node) to AVL.prototype.delete(key, Node)')
    }
    
    if (Node === undefined) {
      // Find the relevant node
      Node = this.search(key);
      if (Node === null) {
        return null; //Node does not exist
      }
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
      this._fixAvl(Node.parent);
      return Node;
    } else {
      let n = this._next(Node);
      [n.key, Node.key] = [Node.key, n.key];
      [n.data, Node.data] = [Node.data, n.data];
      [n.height, Node.height] = [Node.height, n.height];
      process.nextTick(() => {
        this.delete(null, n);
      });
    }
  }

  _fixAvl(node) {
    while (node != null) {
      node.setHeight();
      if(!node.isBal()) {
        if(node.isLH()) {
          if (node.left.isLH()) {
            this._rrotate(node);
          } else {
            this._lrotate(node.left);
            this._rrotate(node);
          }
        } else {
          if (node.right.isRH()) {
            this._lrotate(node);
          } else {
            this._rrotate(node.right);
            this._lrotate(node);
          }
        }
      }
      node = node.parent;
    }
  }

  _lrotate(node) {
    const {right, parent} = node;
    const {left} = right;

    node.right = left;
    if (left != null) {
      left.parent = node;
    }

    right.parent = parent;
    if(parent != null) {
      if (node == parent.left) {
        parent.left = right;
      } else if (node == parent.right) {
        parent.right = right;
      }
    } else {
      this._head = right;
    }

    right.left = node;
    node.parent = right;

    node.setHeight();
    right.setHeight();
  }

  _rrotate(node) {
    const {left, parent} = node;
    const {right} = left;

    node.left = right;
    if (right != null) {
      right.parent = node;
    }

    left.parent = parent;
    if(parent != null) {
      if (node == parent.left) {
        parent.left = left;
      } else if (node == parent.right) {
        parent.right = left;
      }
    } else {
      this._head = left;
    }

    left.right = node;
    node.parent = left;

    node.setHeight();
    left.setHeight();
  }

  _newNode(data, parent) {
    return new AVLNode(data, parent);
  }
}

class AVLNode {
  constructor(data, parent) {
    this.key = data.key;
    this.data = data.data;
    this.parent = parent;
    this.left = null;
    this.right = null;
    this.height = 0;
  }
  isLH() {
    const left = this.left == null ? -1 : this.left.height;
    const right = this.right == null ? -1 : this.right.height;
    return left > right;
  }
  isRH() {
    const left = this.left == null ? -1 : this.left.height;
    const right = this.right == null ? -1 : this.right.height;
    return left < right;
  }
  isBal() {
    const left = this.left == null ? -1 : this.left.height;
    const right = this.right == null ? -1 : this.right.height;
    return Math.abs(left - right) <= 1;
  }
  setHeight() {
    const {left, right} = this;
    const leftH = left === null ? -1 : left.height;
    const rightH = right === null ? -1 : right.height;
    this.height = Math.max(leftH, rightH) + 1;
  }
}

module.exports =  AVL;
