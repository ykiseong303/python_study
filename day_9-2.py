'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-24
범위 : 파트13. 종합문제
'''

# 내 미래 (이차원 배열 활용문제)
## 현재 위치는 첫 입력 값을 공백으로 기준하여 둔다. 1 1 > (0,0)
## 훈련소의 크기는 5*5이고 이를 벗어날 수 없다. 
## 좌 우 상 하의 순으로 입력될 때 현재의 위치는 출력하기 
'''
import numpy as np 
h1, h2 = map(int, input().split())
l, r, u, d = map(int, input().split())
ground = np.zeros((5,5), dtype=int)
#현재의 위치를 출력하기 
#ground[(h1-1,h2-1)] = 1
#print(ground)
ground[(h1-1-u+d,h2-1-l+r)] = 1
print(ground)
'''
'''
# tuple 자료구조를 활용하여 풀이 
import numpy as np
current = tuple(map(int, input().split()))
l, r, u, d = map(int, input().split())
ground = np.zeros((5,5),dtype=int)

move = (current[0]-1-u+d,current[1]-1-l+r)
print(move)
ground[move[0]][move[1]] = 1
for grd in ground : 
    print(*grd)
'''
'''
# numpy를 사용하지 않고 2차원 배열 선언해서 푸는 방법
ground = [[0 for x in range(5)] for x in range(5)]
print(ground)
for grd in ground : 
    print(*grd)
'''
