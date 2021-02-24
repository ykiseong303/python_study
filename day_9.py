'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-24
범위 : 파트13. 종합문제
'''

# 88. 3의 배수는 통과? 
## 1부터 입력한 수까지 출력하되, 3의 배수는 출력하지 않기 
## 3의 배수가 아닐때만 출력하면 된다는 사고로 시작
'''
num = int(input())
for i in range(1, num+1) : 
    if i%3 : 
        print(i, end=' ')
'''
# 89. 수 나열하기 1 
## 시작 값(a), 등차(b), 몇번 째(n)인지를 나타내는 변수가 입력될 때, n번째의 수 출력하기 
### 이 방법은 range의 끝을 알고 있을 때에만 사용할 수 있으므로 한계가 있음
'''
a, b, n = map(int, input().split())
count = 1
for i in range(a,101,b) : 
    if count == n : 
        print(i)
        break
    count += 1
'''
### 범위를 모르는 경우, 리스트에 추가하며 리스트의 수를 조회하는 방식으로 진행
## 반복을 마친 후, count의 값은 +1이 된 상태이지만, 조건에 적합하지 않으므로 아래의 코드는 실행되지 않음 
## 만약 실제 반복횟수를 찾아야 한다면 그대로 사용해도 되지만, 리스트에 접근해야 하는 답이라면 인덱스에 -1을 해야함에 유의
'''
a, d, n = map(int, input().split())
result = []
count = 0
while count < n : 
    result.append(a)
    a += d
    count += 1
## 마지막 행을 출력하면 됌, [-1]
print(result[-1])
'''
# 88-1. 시작위치 a, 등차 값 b, 임의의 값 n이 입력될 때 n보다 커지는 숫자의 리스트 상의 위치(혹은 그 값의 위치 : 이럴땐 +1)와 그 값은? 
'''
a, b, n = map(int, input().split())
result = []
count = 0
while a < n :
    result.append(a)
    a += b 
    count += 1
print(a,count)
'''
# 89. 수 나열하기 2 
## 시작 값 a, 등비 r, 몇 번째인지를 나타내는 수 n이 입력될 때, n번째의 값을 출력
### 1부터 시작하는 순서와 0부터 시작하는 순서는 -1의 차이가 있음
### 탈출 조건문에서 리스트 상의 순서가 실제 나열순서보다 크거나 같아지면 멈춘다는 점을 이용 (조건문이 먼저 실행되고 이를 판별한 뒤에 아래의 연산을 수행하므로 영향x)
'''
a, r, n = map(int, input().split())
result = []
count = 0 
while count < n : 
    result.append(a)
    a *= r 
    count += 1 
print(result[-1])
'''

# 90. 수 나열하기 3
## 시작 값 a, 곱할 값 m, 더할 값 d, 몇번 째인지를 나타내는 n이 입력될 때 n번째의 값을 출력 
'''
a, m, d, n = map(int, input().split())
result = []
count = 0
while count < n : 
    result.append(a)
    a = a*m + d
    count += 1 
print(result[-1])
'''
# 91. 함께 문제 푸는 날 
## 3명이 규칙적으로 방문하는 방문주기가 공백을 두고 입력된다. 
## 3명이 동시에 방문해서 문제를 풀어보는 날을 출력한다 
'''
a, b, c = map(int, input().split())
day = 1
while True : 
    if not day%a and not day%b and not day%c : 
        break
    day += 1 
print(day)
'''
# 91-1. 최대 공약수 구하기
## 세 정수가 입력될 때, 최대공약수를 구하기.
'''
a, b, c = map(int, input().split())
end_point = max(a,b,c)
for i in range(2, end_point+1) : 
    if not a%i and not b%i and not c%i : 
        print(i)
        break
    elif i == end_point : # 이때를 서로소라고 한다. 
        print(1)
'''