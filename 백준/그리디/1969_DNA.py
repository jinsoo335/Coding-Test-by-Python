'''
N개의 길이 M인 DNA 배열에서 Hamming Distance합이 가장 작은 DNA만들기
Adenine, Thymine, Guanine, Cytosine => A, T, G, C
Hamming Distance: 길이가 같은 두 배열의 위치가 다른 문자의 갯수

Step 1) A, T, G, C각 열과  A, T, G, C를 비교해 가장 작은 문자 만들기
Step 2) 1을 이용해 문자열 만들기

'''

N, M = map(int, input().split())

DNAs = list()

hamming_dna = ""
hamming_dis = 0

for _ in range(N):
  str = input()
  DNAs.append(list(str))
  

for col in range(M):
  dis_a = 0
  dis_t = 0
  dis_g = 0
  dis_c = 0
  
  for row in range(N):
    if DNAs[row][col] == "A":
      dis_t += 1
      dis_g += 1
      dis_c += 1
    elif DNAs[row][col] == "T":
      dis_a += 1
      dis_g += 1
      dis_c += 1
    elif DNAs[row][col] == "G":
      dis_t += 1
      dis_a += 1
      dis_c += 1
    elif DNAs[row][col] == "C":
      dis_t += 1
      dis_g += 1
      dis_a += 1

  if min(dis_a, dis_t, dis_g, dis_c) == dis_a:
    hamming_dna += "A"
    hamming_dis += dis_a

  elif min(dis_a, dis_t, dis_g, dis_c) == dis_c:
    hamming_dna += "C"
    hamming_dis += dis_c

  elif min(dis_a, dis_t, dis_g, dis_c) == dis_g:
    hamming_dna += "G"
    hamming_dis += dis_g
  
  elif min(dis_a, dis_t, dis_g, dis_c) == dis_t:
    hamming_dna += "T"
    hamming_dis += dis_t
    



print(hamming_dna)
print(hamming_dis)