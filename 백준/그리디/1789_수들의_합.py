'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

1) 더해가다가 합이 넘어가면, 이전 값을 빼고 합에 맞는 값을 더한다.



'''
S = int(input())

result = 0
index = 1
count = 0

while True:
  result += index
  index += 1
  count += 1
  
  if result > S:
    break

if result > S:
  print(count - 1)
else:
  print(count)