/*class Stack {
  constructor(item) {
      this._stack = [];
      if(item) this._stack.push(item);
  }
  push(item) {
    return this._stack.push(item);
  }
  pop(item) {
    return this._stack.pop(item);
  }
  list() {
    for (const item of this._stack.reverse()) {
      console.log(item);
    }
  }
}*/

function Stack(item) {
  this._stack = [];
  if (item) this._stack.push(item);

  this.push = (item) => this._stack.push(item);
  this.pop = (item) => this._stack.pop(item);
  this.list = () => console.log(...this._stack.reverse());
}

module.exports = Stack;
