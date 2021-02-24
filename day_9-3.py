'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-24
범위 : 파트15. 2차원 배열 
'''

# 96. 바둑판에 흰돌 놓기 
## 바둑판에 올려놓을 흰 돌의 개수(n)가 첫째 줄에 입력
## 둘째줄 부터 n+1줄까지 돌을 올려 놓을 좌표(x,y)가 입력된다. 
## n은 10 이하 좌표는 1~19까지 
'''
n = int(input())
shape = [[0 for _ in range(19)] for _ in range(19)]

for _ in range(n) : 
    # 실제 입력 위치와 리스트의 인덱스는 -1의 차이가 존재
    x, y = map(lambda x : int(x)-1, input().split())
    # 위의 람다식에서 -1을 안하고 아래의 index 접근에서 -1을 해도 되지만, 추후에 사용할 필요가 있을 때마다 -1을 또 해줘야 하는 번거로움 있음
    shape[x][y] = 1
for s in shape : 
    print(*s)
'''
# 97. 바둑판에 십자 뒤집기 
## 십자 뒤집기 횟수(n)이 입력되고, n번만큼 십자뒤집기 진행 
'''
baduk = [
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
]
n = int(input())
for _ in range(n) : 
    x, y = map(lambda x : int(x) - 1, input().split())
    for i in range(19) : 
        baduk[i][y] = 1 if baduk[i][y] == 0 else 0
        baduk[x][i] = 1 if baduk[x][i] == 0 else 0
        # baduk[i][y] = int (not baduk[i][y])
        # baduk[x][i] = int (not baduk[x][i])
for b in baduk : 
    print(*b)
'''