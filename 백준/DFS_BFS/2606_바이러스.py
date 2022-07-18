'''
연결되어 있는 컴퓨터들 중 하나가 바이러스에 감염되면 연달아 감염이 된다.
우선 입력 받은 것을 통해 그래프를 만들고, 연결 되어 있는 컴퓨터들을 찾자
'''

def dfs(group, index, virus_list):
  if index not in virus_list:
    virus_list.append(index)
    for i in range(len(group[index])):
      dfs(group, group[index][i], virus_list)


N = int(input())

couple_cnt = int(input())

group = list()
group.append(list())

for i in range(N):
  group.append(list())

for i in range(couple_cnt):
  left, right = map(int, input().split())

  if right not in group[left]:
    group[left].append(right)
  if left not in group[right]:
    group[right].append(left)

temp_list = list()
dfs(group, 1, temp_list)

print(len(temp_list) - 1)

