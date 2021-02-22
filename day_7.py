'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-22
범위 : 파트13. 종합문제
'''

# 81. 주사위 2개를 던지면 ? 
## 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우의 수 출력 
'''
n, m = map(int, input().split())

for i in range(1, n+1) :
    for j in range(1, m+1) : 
        print(i, j)
'''
# 82. 16진수 구구단 
## A~F까지 임의의 16진수 값이 입력될 때, 입력된 수 * 1~F까지의 곱을 출력 
'''
num = input()
for i in range(1,16) : 
    print("{} * {} = {}".format(num, hex(i).upper()[2:], hex(int(num,16)*i).upper()[2:]))
'''
# 83. 3 6 9의 왕이되자 
## 코드업에서는 3의 배수를 정답으로 치고있으므로 두가지 (3의배수, 진짜 369규칙) 방법으로 문제를 풀이 
## 10보다 작은 정수 1개가 입력되었을 때 그 수까지의 369 게임 결과를 출력

# (1) 3의 배수일 경우 X를 출력
'''
num = int(input())
for i in range(1, num+1) :
    # 
    if not i%3 : 
        print("X", end= ' ')
    else : print(i, end=' ')
# 3항 연산자 활용 익숙해지기 
for i in range(1, num+1) : 
    count = i if i%3 else 'X'
    print(count, end=' ')
'''
# (2) 실제 3 6 9 규칙에 따라 출력
'''
# in 연산자는 해당 문자열에 찾고자 하는 문자열이 있는지 확인
for i in range(1, num+1) :
    if '3' in str(i) or '6' in str(i) or '9' in str(i): 
        print("X", end=' ')
    else : print(str(i), end=' ')
'''
'''
# 3항 연산자를 활용 
for i in range(1, num+1) :
    print("X" if '3' in str(i) or '6' in str(i) or '9' in str(i) else i, end= ' ')
'''
'''
# in을 활용해서 문자열의 각개 값에 접근할 수 있음 
i = '33'
for x in range(0,len(i)) : 
    #print(type(x))
    print(i[x])
'''

# 84. 빛 섞어 색 만들기 
## R, G, B 세 색상에 가짓수(0~128)가 입력될 때 만들어질 수 있는 색의 조합과 가짓수 출력
count = 0
r, g, b = map(int, input().split())
for i in range(0,r) : 
    for j in range(0,g) :
        for k in range(0,b) : 
            print(i, j, k) 
            count += 1
print(count)