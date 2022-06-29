'''
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

1) h, m, s의 변수를 만들고
2) 반복문을 통해 값을 증가시키면서 3이 포함된 경우를 세자
'''

N = int(input())

hour, min, sec, cnt = 0, 0, 0, 0

while hour <= N:
  sec += 1
  if sec == 60:
    min += 1
    sec = 0

  if min == 60:
    hour += 1
    min = 0

  if sec % 10 == 3 or min % 10 == 3 or hour % 10 == 3:
    cnt += 1

  elif sec // 10 == 3 or min // 10 == 3:
    cnt += 1
  


print(cnt)