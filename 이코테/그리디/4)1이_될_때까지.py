'''
N이 1이 될 때까지 N에서 1을 빼거나, N을 K로 나눈다
나눌 때는 나누어 떨어질 때만 가능하다.

1) 나누어 떨어지는지 체크 되면 더이상 나누어 떨어지지 않을 때까지 반복

2) 나누어 떨어지지 않는다면, 1을 빼기

3) 1, 2의 과정을 진행하면서 횟수 세기
'''

N, K = map(int, input().split())

count = 0

while True:
  if N == 1:
    break

  while N % K == 0:
    N = N // K
    count += 1
    
  if N == 1:
    break
  
  N -= 1
  count += 1
  
print(count)
    