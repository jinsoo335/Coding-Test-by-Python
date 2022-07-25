'''
N, M의 정수
N개의 줄에 M개의 정수로 미로 정보가 주어진다.
각각의 수들은 공백 없이 붙어서 입력으로 제시
시작칸과 마지막 칸은 항상 1
'''

from collections import deque

N, M = map(int, input().split())

maze = list()

for _ in range(N):
    maze.append(list(map(int, input())))

# dx, dy의 조합으로 상,하,좌,우 방향 결정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs
def bfs(x, y):

    # 큐에 좌표 넣기
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 맨 앞에 있는 노드 하나 빼기
        x, y = queue.popleft()

        # 현재 좌표에 상,하,좌,우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 넘어가는 경우 넘기기
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 갈 수 없는 경우 넘기기
            if maze[nx][ny] == 0:
                continue

            # 갈 수 있는 경우, 그 방향에 지금 위치에 있는 값 + 1을 적는다.
            # 1 -> 2 이런식으로 시작 위치 부터 해당 위치로 가는 데 걸리는 칸 수를 적게된다.
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N - 1][M - 1]


print(bfs(0, 0))
