function LinkList() {
  this.head = null;

  this.insert = function (data) {
    if (this.head === null) {
      this.head = this._newNode(data);
    } else {
      let node = this.head.next;
      while (node.next !== null) {
        node = node.next;
      }
      node.next = this._newNode(data);
    }
  };

  this.find = function(data) {
    let node = this.head;
    while (node !== null) {
      if (node.data === data) {
        return node;
      } else {
        node = node.next;
      }
    }
    return null;
  }

  this._newNode = function(data) {
    return {
      data,
      next: null,
    };
  };
}
