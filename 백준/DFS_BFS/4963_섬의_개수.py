'''
가로 세로 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형
걸어갈 수 있으면, 같은 섬에 위치해 있다.

w는 너비, h는 높이
'''
import sys

sys.setrecursionlimit(5000000)


def dfs(x, y, island):

    if y >= 0 and x >= 0 and y < h and x < w:
        '''if island[y][x] == 0:
            return False'''

        if island[y][x] == 1:
            island[y][x] = 0

            dfs(x + 1, y, island)

            dfs(x + 1, y + 1, island)

            dfs(x, y + 1, island)

            dfs(x - 1, y, island)

            dfs(x, y - 1, island)

            dfs(x - 1, y - 1, island)

            dfs(x + 1, y - 1, island)

            dfs(x - 1, y + 1, island)

            return True
    return False


ans_list = list()

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = list()
    island_cnt = 0
    for _ in range(h):
        island.append(list(map(int, input().split())))

    for y in range(h):
        for x in range(w):
            if dfs(x, y, island):
                island_cnt += 1

    ans_list.append(island_cnt)

for i in range(len(ans_list)):
    print(ans_list[i])
