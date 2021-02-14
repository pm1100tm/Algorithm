/** @format */

'use strict';

/**
 *모의고사

  link - https://programmers.co.kr/learn/courses/30/lessons/42840?language=javascript

  answers	      return
  [1,2,3,4,5]	  [1]
  [1,3,2,4,2]	  [1,2,3]
 */

function solution(answers) {
  const student_one = [1, 2, 3, 4, 5];
  const student_two = [2, 1, 2, 3, 2, 4, 2, 5];
  const student_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  const count = [0, 0, 0];

  for (let i = 0; i < answers.length; i++) {
    if (student_one[i % answers.length] === answers[i]) {
      count[0]++;
    }

    if (student_two[i % answers.length] === answers[i]) {
      count[1]++;
    }

    if (student_three[i % answers.length] === answers[i]) {
      count[2]++;
    }
  }

  const max = Math.max(count[0], count[1], count[2]);
  const result = [];

  for (let j = 0; j < count.length; j++) {
    if (count[j] === max) {
      result.push(j + 1);
    }
  }
  return result;
}

const r1 = solution([1, 2, 3, 4, 5]);
const r2 = solution([1, 3, 2, 4, 2]);
console.log(r1);
console.log(r2);

// other solution one
function solution(answers) {
  let answer = []; //정답 출력
  let a1 = [1, 2, 3, 4, 5]; //반복주기 5
  let b1 = [2, 1, 2, 3, 2, 4, 2, 5]; // 반복주기 8
  let c1 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; //반복주기 10
  function max(a, b) {
    //최대값 함수
    if (a > b) return a;
    else return b;
  }
  let value = 0;
  let cnt = [0, 0, 0]; //수포자들의 점수
  for (var i = 0; i < answers.length; i++) {
    if (a1[i % 5] === answers[i]) cnt[0]++;
    if (b1[i % 8] === answers[i]) cnt[1]++;
    if (c1[i % 10] === answers[i]) cnt[2]++;
  }
  value = max(max(cnt[0], cnt[1]), cnt[2]); //최대값 입력
  var idx = 0;
  for (var i = 0; i < 3; i++) {
    //최대점수를 가진 수포자 찾기
    if (cnt[i] === value) {
      answer[idx] = i + 1;
      idx += 1;
    }
  }
  return answer;
}

// other solution two
function solution(answers) {
  var answer = [];
  const man1 = [1, 2, 3, 4, 5];
  const man2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let count = [0, 0, 0];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] == man1[i % man1.length]) count[0]++;
    if (answers[i] == man2[i % man2.length]) count[1]++;
    if (answers[i] == man3[i % man3.length]) count[2]++;
  }

  const max = Math.max(count[0], count[1], count[2]);
  for (let i = 0; i < count.length; i++) {
    if (max == count[i]) answer.push(i + 1);
  }

  return answer;
}
