/** @format */

'use strict';

/**
 *두 개 뽑아서 더하기
  link - https://programmers.co.kr/learn/courses/30/lessons/68644?language=javascript

  numbers      result
  [2,1,3,4,1]	 [2,3,4,5,6,7]
  [5,0,2,7]	   [2,5,7,9,12]
 */

const case_1 = [2, 1, 3, 4, 1];
const case_2 = [5, 0, 2, 7];

function my_solution(numbers) {
  const answer = [];

  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const sum = numbers[i] + numbers[j];
      if (answer.indexOf(sum) < 0) {
        answer.push(sum);
      }
    }
  }
  return answer.sort((a, b) => a - b);
}

const result1 = my_solution(case_1);
const result2 = my_solution(case_2);

console.log(result1);
console.log(result2);

/* best solution i think*/
function solution(numbers) {
  var answer = [];

  numbers.forEach((v) => {
    const num1 = numbers.slice();

    let a = num1.indexOf(v);
    num1.splice(a, 1);

    num1.forEach((z) => {
      let num2 = v + z;

      if (!answer.includes(num2)) {
        answer.push(num2);
      }
    });
  });

  return answer.sort((a, b) => a - b);
}
