'''
N(숫자 갯수), M(더할 횟수), K(같은걸 최대로 더할 수 있는 횟수)


'''

N, M, K = map(int, input().split())

num_line = list(map(int, input().split()))

num_line.sort(reverse=True)

result = 0
count = 0
index = 0

while count < M:
  result += num_line[0]
  count += 1
  index += 1
  
  if count == M:
    break

  if index == K:
    result += num_line[1]
    count+= 1
    index = 0

print(result)
