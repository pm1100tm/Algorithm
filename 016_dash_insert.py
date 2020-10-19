"""
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤,
문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
(예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자.
"454*67-9-3"
입력 - 화면에서 숫자로 된 문자열을 입력받는다.
"""
s = input()
result = []
for i in range(len(s)):
    if i+1 < len(s):
        if int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0:
            result.append(s[i] + "*")
        elif int(s[i]) % 2 != 0 and int(s[i+1]) % 2 != 0:
            result.append(s[i] + "-")
        else:
            result.append(s[i])
print("".join(result) + s[-1])

# s = "4546793"  # 454*67-9-3
# s = "477734702349"  # 47-7-7-3470*2349