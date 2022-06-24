'''
N개의 행과 M개의 열이 있는 카드 뭉치들에서 하나의 행을 골라
그 행에서 가장 작은 숫자 카드를 골랐을 때, 그 카드가 다른 행에서 뽑은 수들보다 가장 커야한다.

1) 행을 기준으로 하여 가장 작은 값들을 뽑아내고 그들 중 가장 큰 값을 골라내자
2) 행을 기준으로 min, 열을 기준으로 max

'''

N, M = map(int, input().split())

cards = list()

rows = list()

for i in range(N):
  temp = list(map(int, input().split()))
  #cards.append(temp)
  rows.append(min(temp))

print(max(rows))