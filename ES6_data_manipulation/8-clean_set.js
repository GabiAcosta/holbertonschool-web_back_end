export default function cleanSet(set, startString) {
  if (startString === '') return '';
  const filteredValues = [...set].filter((value) => typeof value === 'string' && value.startsWith(startString));
  const cleanString = filteredValues.map((value) => value.slice(startString.length)).join('-');
  return cleanString;
}
