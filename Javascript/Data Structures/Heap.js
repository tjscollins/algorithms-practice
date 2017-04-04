function Heap(input = [], type='max') {
  this.top = () => this._data[0];

  this.insert = (item) => {
    this._data.push(item);
    this._fixHeapProp(this._data.length-1);
    return this;
  }

  this._fixHeapProp = (index) => {
    const {_data} = this;
    parent = Math.floor((index-1)/2);
    if(parent >= 0) {
      let largest = parent;
      let children = [2*parent + 1, 2*parent + 2];
      if ( _data[children[0]] > _data[largest] && type=='max' || type=='min' && _data[children[0]] < _data[largest] ) {
        largest = children[0];
      }
      if (_data[children[1]] > _data[largest] && type=='max' || type=='min' && _data[children[1]] < _data[largest] ) {
        largest = children[1];
      }
      if (largest !== parent) {
        [_data[parent], _data[largest]] = [_data[largest], _data[parent]];
        this._fixHeapProp(parent);
        this._fixHeapProp(largest*2+1);
      }
    }
  }
  this.extract = () => {
    const {_data} = this;
    [_data[0], _data[_data.length-1]] = [_data[_data.length-1], _data[0]];
    const output = _data.pop();
    this._fixHeapProp(1);
    return output;
  }

  this.replaceTop = (item) => {
    top = this._data[0];
    this._data[0] = item;
    this._fixHeapProp(1);
    return top;
  }

  this._data = [];
  if(input.length > 0) {
    input.forEach((value) => this.insert(value));
  }
}

module.exports = Heap;
