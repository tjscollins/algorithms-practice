const {LinkList} = require('../Data Structures/LinkList');

describe('LinkList class: ', () => {
  it('should return a new LinkList object', () => {
    let list = new LinkList();

    expect(typeof list).toBe('object');
    expect(list.head).toBe(null);
    expect(typeof list.insert).toBe('function');
    expect(typeof list.find).toBe('function');
    expect(typeof list.pop).toBe('function');
  });

  it('should insert new items at the top of the list', () => {
    let list = new LinkList();

    list.insert(1);
    expect(list.head.data).toBe(1);
    list.insert('a');
    expect(list.head.data).toBe('a');
    expect(list.head.next.data).toBe(1);
  });

  it('should pop items off the top of the list', () => {
    let list = new LinkList();
    list.insert('a');
    list.insert('b');
    expect(list.head.data).toBe('b');
    expect(list.pop()).toBe('b');
  });

  it('should find and return items from the list', () => {
    let list = new LinkList();
    list.insert('a');
    list.insert('b');
    list.insert('c');
    list.insert('d');
    expect(list.find(1)).toBe(null);
    expect(typeof list.find('a')).toBe('object');
    expect(list.find('a').data).toBe('a');
  });
})
