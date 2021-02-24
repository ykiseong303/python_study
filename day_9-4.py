'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-24
범위 : 98 ~ 99번 문제
'''

# 98. 설탕과자 뽑기 
## (1) 격자판의 가로(w), 세로(h)가 입력
## (2) 막대의 개수 (n) 입력 
## (3) 막대의 길이(i), 방향(d, 0=가로), 좌표(x,y, 가장 왼쪽이거나 위쪽) 입력 
## 위의 값들이 입력될 때 격자판을 출력하기 
'''
w, h = map(int, input().split())
n = int(input())
## h열의 리스트가 w행만큼 생겨진다고 생각 
shape = [[0 for _ in range(h)] for _ in range(w)]
for i in range(n) : 
    i, d, x, y = map(int, input().split())
    x, y = x-1, y-1
    if d == 0 :
        for j in range(y,y+i) : 
            shape[x][j] = 1
    else : 
        for k in range(x,x+i) : 
            shape[k][y] = 1
for s in shape : 
    print(*s)
'''

# 99. 성실한 개미 
## 10*10 크기의 개미집과 벽(1)과 먹이(2)가 입력된다
## 움직임의 방향은 오른쪽에서 아래 (오른쪽으로 가다 벽(1)을 만나면 아래로 방향전환)
## 좌표상 (2,2)가 시작위치일때 개미의 이동경로를 9로 출력한다

ant_house = [
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

x, y = 1,1
# 재귀호출을 이용한 방법
'''
def goto(ant_house, x, y) : 
    if ant_house[x][y] == 1 : 
        x, y = x+1, y-1

    if ant_house[x][y] == 2 : 
        return 

    ant_house[x][y] = 9
    y += 1

    goto(ant_house, x, y)

goto (ant_house, x, y)

for a in ant_house : 
    print(*a)
'''
'''
# 반복문을 이용한 방법 
while ant_house[x][y] != 2 : 
    ant_house[x][y] = 9
    y += 1 
    if ant_house[x][y] == 1 : 
        x, y = x+1, y-1
for a in ant_house : 
    print(*a)
'''