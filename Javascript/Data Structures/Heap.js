class Heap {
  constructor(data = [], type = 'max') {
    this._data = data;
    this._type = type;
    this._size = this._data.length;
    if (this._data.length > 0) {
      this._buildHeap();
    }
  }
  insert(data) {
    this._data.push(data);
    this._size++;
    this._buildHeap();
    return this;
  }
  extract() {
    [this._data[0], this._data[this._size-1]] = [this._data[this._size-1], this._data[0]];
    let value = this._data.pop();
    this._size--;
    this._buildHeap();
    return value;
  }
  top() {
    return this._data[0];
  }
  replaceTop(data) {
    [data, this._data[0]] = [this._data[0], data];
    this._buildHeap();
    return data;
  }
  sort() {
    let arr = [];
    let length = this._size;
    while (arr.length < length) {
      arr.push(this.extract());
    }
    return arr;
  }

  _buildHeap() {
    for (let i = Math.floor(this._size - 1 / 2); i >= 0; --i) {
      this._fixHeapProp(i);
    }
  }
  _fixHeapProp(index) {
    const {_data, _type} = this;
    let largest = index;
    let left = 2*index + 1;
    let right = 2*index + 2;

    if(_data[left] > _data[largest] && _type == 'max' || _type=='min' && _data[left] < _data[largest]) {
      largest = left;
    }
    if(_data[right] > _data[largest] && _type == 'max' || _type=='min' && _data[right] < _data[largest]) {
      largest = right;
    }
    if (largest !== index) {
      [_data[index], _data[largest]] = [_data[largest], _data[index]];
      this._fixHeapProp(largest);
    }
  }
}

module.exports = Heap;
