import ClassRoom from './0-classroom';

export default function initializeRooms() {
  /* same result, more code
  const array = [];
  const classRoom1 = new ClassRoom(19);
  const classRoom2 = new ClassRoom(20);
  const classRoom3 = new ClassRoom(34);
  array.push(classRoom1);
  array.push(classRoom2);
  array.push(classRoom3);
  return array; */

  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
}
