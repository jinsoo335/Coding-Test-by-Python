'''
8 X 8 좌표 평면, 나이트는 L자로만 이동 가능, 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성

'''

pos = input()

str_pos = list(pos)

move_cnt = 0

if str_pos[0] >= "c":
  if str_pos[1] >= "2" and str_pos[1] <= "7":
    move_cnt += 2

  if str_pos[1] == "1" or str_pos[1] == "8":
    move_cnt += 1

if str_pos[0] <= "f":
  if str_pos[1] >= "2" and str_pos[1] <= "7":
    move_cnt += 2

  if str_pos[1] == "1" or str_pos[1] == "8":
    move_cnt += 1



if str_pos[1] >= "3":
  if str_pos[0] >= "b" and str_pos[0] <= "g":
    move_cnt += 2

  if str_pos[0] == "a" or str_pos[0] == "h":
    move_cnt += 1

if str_pos[1] <= "6":
  if str_pos[0] >= "b" and str_pos[0] <= "g":
    move_cnt += 2

  if str_pos[0] == "a" or str_pos[0] == "h":
    move_cnt += 1



print(move_cnt)