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
  delete(key) {}
  traverse() {}
  prev(node) {}
  next(node) {}
  _newNode(data, parent) {
    return {key: data.key, data: data.data, left: null, right: null, parent,};
  }
  _appendBst(node, head) {}
}

module.exports = BST;
