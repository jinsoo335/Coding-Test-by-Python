'''
숫자야구 만들기

1) 입력받은 숫자를 비교해 스트라이크 볼의 갯수 확인
2) s,b의 갯수와 숫자간의 비교를 하자


'''
def baseball(ori, sub):
  s, b = 0, 0
  str_ori = f"{ori}"
  str_sub = f"{sub}"

  
  for i in range(len(str_ori)):
    if str_ori[i] == str_sub[i]:
      s += 1
      
    elif str_sub[i] in str_ori:
      b += 1

  return s, b



N = int(input())

num_lines = list()

answers = list()

for _ in range(N):
  num_lines.append(list(map(int, input().split())))


for num in range(111, 1000):
  str_num = f"{num}"
  if "0" in str_num:
    continue

  twice_check = False
  for i in range(len(str_num)):
    for j in range(i + 1, len(str_num)):
      if str_num[i] == str_num[j]:
        twice_check = True
        break

    if twice_check:
      break

  if twice_check:
    continue
  
  
  check = False
  for i in range(len(num_lines)):
    s, b = baseball(num, num_lines[i][0])

    if s == num_lines[i][1] and b == num_lines[i][2]:
      check = True
    else:
      check = False
      break

  if check:
    answers.append(num)

print(len(answers))