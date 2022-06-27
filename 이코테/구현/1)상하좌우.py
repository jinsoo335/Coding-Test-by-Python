'''
N x N 크기의 정사각형 공간에서 L, R, U, D의 문자들이 주어졌을때, 최종 적인 위치 구하기
가장 왼쪽 위 좌표 (1, 1)
가장 오른쪽 아래 좌표 (N, N)

1) N + 1 크기의 2차원 배열 만들기
2) 조건문을 통해 이동하기
'''

N = int(input())

move_list = list(input().split())

x, y = 1, 1
max_x, max_y = N, N


for move in move_list:
  if move == "R" and x + 1 <= max_x:
    x += 1
  elif move == "L" and x - 1 >= 1:
    x -= 1
  elif move == "U" and y - 1 >= 1:
    y -= 1
  elif move == "D" and y + 1 <= max_y:
    y += 1

print(y, x)