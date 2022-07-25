# Coding-test

<h1>주의 사항</h1>
<body> 
  <p>
    <li>문제 풀 때, 처음에 글로 쓰면서 생각하고 코드로 작성하기</li>
    <li>변수 이름은 알기 쉽게 쓰기</li>
    <li>replit 에서 코딩할때, sys.stdin.readlines() 조심히 쓰기 -> 가끔 console에 중복되서 나올 수 있음</li>
  </p> 
</body>

<h1>그리디</h1>
<body> 
  <p>
    <li>현 상황에서 지금 당장 좋아 보이는 것을 선택해 나가기...</li>
  </p> 
</body>

<h1>구현</h1>
<body>
  <p>
    <li>
      자료구조를 사용할 때, from collections import deque와 같이 import하는 것 잊지말 것
    </li>
    <li>
      deque는 append, appendleft, pop, popleft를 사용 가능
    </li>
    <li>
      temp = deque()와 같이 사용했다면, if temp: 만으로 안에 차있는지 확인 가능 
    </li>
    <li>
      리스트 슬라이싱 -> list[0:5], 리스트 슬라이싱을 하며 역순으로 -> list[::-1]
    </li>
    
  </p>
</body>

<h1>그래프 탐색</h1>
<body>
  <p>
    그래프 탐색에 있어, 일단 두 가지를 생각하자
    1. 그래프가 주어졌다면, 바로 연결관계 만들기
    2. 단순히 좌표로만 몇몇개들이 존재한다면, 재귀를 돌며 방문 한 것을 체크하자...
    3. dfs문제 에서는 재귀가 길어질 수 있다. 재귀 한계를 늘려주자
      import sys
      sys.setrecursionlimit(5000000)
      를 쓰자
  </p>
  
</body>

<h1>다이나믹</h1>
<body>
  <p>
    
  </p>
</body>