'''
N x N개의 사탕 행렬을 입력 받은 후, 인접한 2개의 사탕을 골라 위치를 바꾸고 같은 색의 사탕이 가장 연속적으로 있는 한 행 or 열을 골라 사탕을 먹는다.
한 행에서 연속적인 사탕만 먹는다...

1) 행렬 생성
2) 행과 열로 비교를 하자
  2-1) 행을 교환한 후 열을 체크
  2-2) 열을 교환한 후 행을 체크

'''
import sys


def check(candy_map):
    seq_cnt = 1
    N = len(candy_map)

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy_map[i][j] == candy_map[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            if seq_cnt < cnt:
                seq_cnt = cnt

        cnt = 1
        for j in range(1, N):
            if candy_map[j][i] == candy_map[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if seq_cnt < cnt:
                seq_cnt = cnt

    return seq_cnt


#input = sys.stdin.readlines()
N = int(sys.stdin.readlines())

candy_map = list()


candy_map = [list(input()) for _ in range(N)]

max_candy = 0
seq_cnt = 0

for row in range(N):
    for col in range(N):

        if col + 1 < N:
            candy_map[row][col], candy_map[row][col + 1] = candy_map[row][
                col + 1], candy_map[row][col]

            seq_cnt = check(candy_map)
            if max_candy < seq_cnt:
                max_candy = seq_cnt

            candy_map[row][col], candy_map[row][col + 1] = candy_map[row][
                col + 1], candy_map[row][col]

        if row + 1 < N:
            candy_map[row][col], candy_map[row + 1][col] = candy_map[
                row + 1][col], candy_map[row][col]

            seq_cnt = check(candy_map)
            if max_candy < seq_cnt:
                max_candy = seq_cnt

            candy_map[row][col], candy_map[row + 1][col] = candy_map[
                row + 1][col], candy_map[row][col]

print(max_candy)
