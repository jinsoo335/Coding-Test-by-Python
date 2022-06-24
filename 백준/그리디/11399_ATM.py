'''
사람의 수가 주어지고, 사람마다 ATM에서 인출하는 시간이 주어진다.
ATM에서 인출하는 시간은 앞 사람이 걸린 시간이 누적되어 계산된다.

1) 적게 걸리는 순서대로 정렬한 후
2) 누적하여 값을 계산하자
  2-1) 반복문을 통해 이전 까지의 값을 더하고,
  2-2) 이번 숫자를 더하자

'''

N = int(input())

num_line = list(map(int, input().split()))
num_line.sort()

min_sum = 0

for i in range(len(num_line)):
  for j in range(i):
    min_sum += num_line[j]
  min_sum += num_line[i]

print(min_sum)
