export default function createEmployeesObject(departmentName, employees) {
  const x = { [departmentName]: employees };
  return x;
}
