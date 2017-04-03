function LinkList() {
  this.head = null;

  this.pop = function() {
    let node = this.head;
    this.head = node.next;
    return node.data;
  }

  this.insert = function (data) {
    if (this.head === null) {
      this.head = this._newNode(data);
    } else {
      let node = this.head;
      this.head = this._newNode(data);
      this.head.next = node;
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

module.exports = {
  LinkList
}
