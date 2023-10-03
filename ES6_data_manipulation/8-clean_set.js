export default function cleanSet(set, startString) {
  if (startString === '') return '';
  const filteredValues = [...set].filter((value) => value.startsWith(startString));
  const cleanString = filteredValues.map((value) => value.substring(startString.length)).join('-');
  return cleanString;
}
