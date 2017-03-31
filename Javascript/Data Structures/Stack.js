/*class Stack {
  constructor(item) {
    this._stack = [];
    if (item)
      this._stack.push(item);
    }
  push(item) {
    return this
      ._stack
      .push(item);
  }
  pop(item) {
    return this
      ._stack
      .pop(item);
  }
  list() {
    for (const item of this._stack.reverse()) {
      console.log(item);
    }
  }
  top() {
    return this._stack[this._stack.length-1];
  }
}*/

function Stack(item) {
  this._stack = [];
  if (item)
    this._stack.push(item);
  
  this.push = (item) => this
    ._stack
    .push(item);
  this.pop = (item) => this
    ._stack
    .pop(item);
  this.list = () => this
    ._stack
    .reduce((str, val) => `${val} ${str}`);

  this.top = () => this._stack[this._stack.length - 1];
}

module.exports = Stack;
