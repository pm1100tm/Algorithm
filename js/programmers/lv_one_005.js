/** @format */

/* 두 정수 사이의 합
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건
  a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
  a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
  a와 b의 대소관계는 정해져있지 않습니다.

입출력 예
  a   b   return
  3   5   12
  3   3   3
  5   3   12
 */

function my_solution(a, b) {
  if (a > b) {
    let temp = a;
    a = b;
    b = temp;
  }

  let answer = 0;
  for (let i = a; i < b + 1; i++) {
    answer += i;
  }

  console.log(answer);
  return answer;
}

// my_solution(3, 5);
// my_solution(3, 3);
// my_solution(5, 3);

function otherSolution(a, b) {
  if (a === b) {
    return a;
  }

  let small = a < b ? a : b;
  let big = a > b ? a : b;

  for (let i = small + 1; i < big + 1; i++) {
    small += i;
  }

  return small;
}

console.log(otherSolution(3, 5));
console.log(otherSolution(3, 3));
console.log(otherSolution(5, 3));
