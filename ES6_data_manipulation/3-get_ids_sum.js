export default function getStudentIdsSum(array) {
  const initialValue = 0;
  const sumOdIds = array.reduce((accumulator, student) => accumulator + student.id, initialValue);
  return sumOdIds;
}
