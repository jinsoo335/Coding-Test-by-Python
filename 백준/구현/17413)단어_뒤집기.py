'''
문자열에서 단어 뒤집기
< > 안에 있으면 뒤집기 X
단어와 단어는 공백으로 구분
단어는 숫자 알파벳으로 이루어짐

1) 입력받은 문자열 S에서 단어로 이루어 진 부분은 뒤집고 나머지는 그냥 sol_que에 집어 넣기
2) sol_que에서 나중에 들어온걸 먼저 빼자... stack?
'''

from collections import deque

S = input()

sol_list = list()

spec_check = False
spec_index = 0


str_que = deque()
word = ""

for index in range(len(S)):

  if S[index] == "<":
    spec_check = True
    spec_index = index

    word = ""
    while str_que:
      word += str_que.pop()

    if word != "":
      sol_list.append(word)

    
  
  elif S[index] == ">":
    spec_check = False
    sol_list.append(S[spec_index : index + 1])

  
  elif spec_check:
    continue


  elif S[index] == " ":
    word = ""
    while str_que:
      word += str_que.pop()

    if word != "":
      sol_list.append(word)
    sol_list.append(" ")

  else:
    str_que.append(S[index])

word = ""
while str_que:
  word += str_que.pop()

if word != "":
  sol_list.append(word)
  


for sol in sol_list:
  print(sol, end="")
print()