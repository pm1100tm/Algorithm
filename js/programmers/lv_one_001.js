/** @format */

'use strict';

/**
 *완주하지 못한 선수
  link - https://programmers.co.kr/learn/courses/30/lessons/42576?language=javascript
  participant
        case 1 - ["leo", "kiki", "eden"]
        case 2 - ["marina", "josipa", "nikola", "vinko", "filipa"]
        case 3 - ["mislav", "stanko", "mislav", "ana"]

  completion
        case 1 - ["eden", "kiki"]
        case 2 - ["josipa", "filipa", "marina", "nikola"]
        case 3 - ["stanko", "ana", "mislav"]

  return
      "leo"       : leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
      "vinko"     : vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
      "mislav"    : mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

 */

const p_case_1 = ['leo', 'kiki', 'eden'];
const p_case_2 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa'];
const p_case_3 = ['mislav', 'stanko', 'mislav', 'ana'];

const c_case_1 = ['eden', 'kiki'];
const c_case_2 = ['josipa', 'filipa', 'marina', 'nikola'];
const c_case_3 = ['stanko', 'ana', 'mislav'];

function my_solution(participant, completion) {
  participant.sort();
  completion.sort();

  for (let i = 0; i < participant.length; i++) {
    if (participant[i] != completion[i]) {
      return participant[i];
    }
  }

  return participant.pop();
}

const result1 = my_solution(p_case_1, c_case_1);
const result2 = my_solution(p_case_2, c_case_2);
const result3 = my_solution(p_case_3, c_case_3);

console.log(result1);
console.log(result2);
console.log(result3);

// other soutions to be update
