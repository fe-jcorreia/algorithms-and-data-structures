// UFT-16

string = "😸😾"
string2 = "😸😾"
string3 = "noël"
string4 = "〩ざ"

function reverse(inputString) {
  const stringArray = inputString.split('');
  const reversedArray = stringArray.reverse();
  const reversedString = reversedArray.join('');
  return reversedString;
}

console.log('reverse: ', reverse(string3))
console.log('substring: ', string.substring(1))
console.log('string = string2', string === string2)
console.log(string)
console.log(string.length)

console.log("asian -----------------")
console.log(string4.length)
console.log(reverse(string4))
console.log(string4.substring(1))
