class BST {
  constructor() {
    this.head = null;
  }
  insert(data) {
    if (this.head === null) {
      this.head = this._newNode(data, null);
    } else {
      let node = this.head;
      let parent = null;
      while (node !== null) {
        parent = node;
        if (data.key < node.key) {
          if (node.left == null) {
            node.left = this._newNode(data, node);
            node = null;
          } else {
            node = node.left;
          }
        } else {
          if (node.right == null) {
            node.right = this._newNode(data, node);
            node = null;
          } else {
            node = node.right;
          }
        }
      }
    }
  }
  search() {}
  delete() {}
  traverse() {}
  prev() {}
  next() {}
  _newNode(data, parent) {
    return {key: data.key, data: data.data, left: null, right: null, parent,};
  }
}

module.exports = BST;
