class BST {
  constructor() {
    this.head = null;
    this.size = 0;
  }
  insert(data) {
    if (this.head === null) {
      this.head = this._newNode(data, null);
      this.size++;
    } else {
      let node = this.head;
      let parent = null;
      while (node !== null) {
        parent = node;
        if (data.key < node.key) {
          if (node.left == null) {
            node.left = this._newNode(data, node);
            this.size++;
            node = null;
          } else {
            node = node.left;
          }
        } else {
          if (node.right == null) {
            node.right = this._newNode(data, node);
            this.size++;
            node = null;
          } else {
            node = node.right;
          }
        }
      }
    }
  }
  search(key) {
    let node = this.head;
    while (node !== null) {
      if (key < node.key) {
        node = node.left;
      } else if (key > node.key) {
        node = node.right;
      } else {
        return node;
      }
    }
    return node;
  }
  delete(key) {
    let node = this.search(key);
    if (node.parent.left == node) {
      if (node.left) {
        node.left.parent = node.parent;
        node.parent.left = node.left;
        this._appendBst(node.left, node.right);
      } else if (node.right) {
        node.right.parent = node.parent;
        node.parent.left = node.right;
      } else {
        node.parent.left = null;
      }
      this.size--;
    } else if (node.parent.right == node) {
      if (node.right) {
        node.right.parent = node.parent;
        node.parent.right = node.right;
        this._appendBst(node.right, node.left);
      } else if (node.left) {
        node.left.parent = node.parent;
        node.parent.right = node.left;
      } else {
        node.parent.right = null;
      }
      this.size--;
    } else {
      throw new Error('node not connected to parent!');
    }

  }
  traverse() {}
  prev() {}
  next() {}
  _newNode(data, parent) {
    return {key: data.key, data: data.data, left: null, right: null, parent,};
  }
  _appendBst(node, head) {
    if (head == null) {
      return;
    }
    let parent = node.parent;
    while (node !== null) {
      parent = node;
      if (head.key < node.key) {
        if (node.left == null) {
          node.left = head;
          node = null;
        } else {
          node = node.left;
        }
      } else {
        if (node.right == null) {
          node.right = head;
          node = null;
        } else {
          node = node.right;
        }
      }
    }
  }
}

module.exports = BST;
