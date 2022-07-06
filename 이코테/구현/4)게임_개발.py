'''
맵에서 육지만 가보기
현재 위치에서 총 가볼 수 있는 육지의 갯수를 세기


좌 상단이 (0, 0)
(A, B) => A는 북으로 부터 떨어진 칸수, B는 서로부터 떨어진 칸수

1) 2차원 배열을 만들자
2) 입력 받은 곳에서 0으로 이뤄진 곳만을 이동
'''


N, M = map(int, input().split())

pos_x, pos_y, direct = map(int, input().split())

play_map = list()

for _ in range(N):
  play_map.append(list(map(int, input().split())))

play_map[pos_y][pos_x] = 1

visit_cnt = 1
end_cnt = 0


while end_cnt < 4:
  # 북쪽 바라보면, 왼쪽(3) 방향 비어있는지 확인
  if direct == 0:
    if pos_x - 1 >= 0 and play_map[pos_y][pos_x - 1] == 0:
      pos_x -= 1
      visit_cnt += 1
      end_cnt = 0
      play_map[pos_y][pos_x] = 1
    else:
      end_cnt += 1
    direct = 3

  # 동쪽 바라보면, 왼쪽(0) 방향 비어있는지 확인
  elif direct == 1:
    if pos_y - 1 >= 0 and play_map[pos_y - 1][pos_x] == 0:
      pos_y -= 1
      visit_cnt += 1
      end_cnt = 0
      play_map[pos_y][pos_x] = 1
    else:
      end_cnt += 1
    direct = 0

  # 남쪽 바라보면, 왼쪽(1) 방향 비어있는지 확인
  elif direct == 2:
    if pos_x + 1 < M and play_map[pos_y][pos_x + 1] == 0:
      pos_x += 1
      visit_cnt += 1
      end_cnt = 0
      play_map[pos_y][pos_x] = 1
    else:
      end_cnt += 1
    direct = 1    

  # 서쪽 바라보면, 왼쪽(2) 방향 비어있는지 확인
  elif direct == 3:
    if pos_y + 1 < N and play_map[pos_y + 1][pos_x] == 0:
      pos_y += 1
      visit_cnt += 1
      end_cnt = 0
      play_map[pos_y][pos_x] = 1
    else:
      end_cnt += 1
    direct = 2

print(visit_cnt)