export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }
  /* valid methods but [Symbol.toPrimitive] is more accurate in this case
  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  } */

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') {
      return this._size;
    }
    if (hint === 'string') {
      return this._location;
    }
    return this;
  }
}
