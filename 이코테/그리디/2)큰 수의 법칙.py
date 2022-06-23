N, M, K = map(int, input().split())

num_line = list(map(int, input().split()))

num_line.sort(reverse=True)

check = 0
result = 0

while check <= M:
  for i in range(K):
    if check == M:
      break

    result += num_line[0]
    check += 1

  if check == M:
    break
  
  result += num_line[1]
  check += 1
  

print(result)