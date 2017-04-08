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
    this._data[this._size++] = data;
    this._buildHeap();
    return this;
  }
  extract() {
    [this._data[0], this._data[this._size-1]] = [this._data[this._size-1], this._data[0]];
    let value = this._data.pop();
    this._size--;
    this._fixHeapProp(0);
    return value;
  }
  top() {
    return this._data[0];
  }
  replaceTop(data) {
    [data, this._data[0]] = [this._data[0], data];
    this._fixHeapProp(0);
    return data;
  }
  sort() {
    while (this._size > 0) {
      [this._data[0], this._data[this._size-1]] = [this._data[this._size-1], this._data[0]];
      this._size--;
      this._fixHeapProp(0);
    }
    return this._data;
  }

  _buildHeap() {
    for (let i = Math.floor(this._size - 1 / 2); i >= 0; --i) {
      this._fixHeapProp(i);
    }
  }
  _fixHeapProp(index) {
    const {_data, _type, _size} = this;
    let largest = index;
    let left = 2*index + 1;
    let right = 2*index + 2;

    if(left < _size
      && (_data[left] > _data[largest] && _type == 'max'
      || _type=='min' && _data[left] < _data[largest])) {
      largest = left;
    }
    if(right < _size
      && (_data[right] > _data[largest] && _type == 'max'
      || _type=='min' && _data[right] < _data[largest])) {
      largest = right;
    }
    if (largest !== index) {
      [_data[index], _data[largest]] = [_data[largest], _data[index]];
      this._fixHeapProp(largest);
    }
  }
}

module.exports = Heap;
