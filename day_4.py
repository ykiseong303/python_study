'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-12
범위 : 파트4. 출력변환
'''

# 10진수를 8진수로 출력하기
# var = int(input())
# var = oct(var)[2:]
# print(var)

# 10진수를 16진수로 출력
# var = int(input())
# var = hex(var)[2:]
# print(var)

# 8진수를 10진수로 변환
# var = '0o'+input()
# var = int(var,8)
# print(var)

# 16진수를 10진수로 변환
# var = '0x'+input()
# var = int(var,16)
# print(var)

# 문자를 입력받아서 아스키 코드로 변환65
# var = ord(input()) # ord : 문자를 대응되는 아스키코드로 변환
# print(var)

# 아스키코드를 문자로 변환
# var = int(input())
# print(chr(var))

'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-12
범위 : 파트5. 산술연산
'''

# 영문자 한개를 입력받아서 다음 문자를 출력
# var = ord(input())
# print(chr(var+1))

# 정수 2개를 입력받아서 나눈 몫을 구해보기
# a, b = map(int,input().split(' '))
# print(a/b) # /는 나눈 값만 , //는 나눈 몫을 반환
# print(a//b)

'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-12
범위 : 파트6. 비트시프트 연산
'''

# 정수 1개를 입력받아 두배로 출력하기 
## * 으로도 처리가 가능하지만 대량의 데이터 처리시 비트시프트 연산의 속도가 더 빠름 
## 10진수를 2진수로 변환하고, 왼쪽으로 1칸 움직이면(빈칸은 0으로 채움) 두배가 됨
## 한칸씩 늘릴 수록 2의 제곱승으로 계산됨
# var = int(input())
# print(var << 3) 

'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-12
범위 : 파트7. 기초 비교연산
'''

# a, b = map(int, input().split(' '))
# if a == b : 
#     print('1')
# else : 
#     print('0')

# print( a > b and 1 or 0)
# print( 1 if a>b else 0)

'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-12
범위 : 파트8. 논리 연산
'''
# 0이 아닌 모든 숫자는 true

# 참 또는 거짓이 입력되었을 때 반대로 출력
# var = int(input())
# print( not(var))

# and 연산자, 참일 경우 뒤의 값을 출력
# print( 100 and 0 )

# or 연산자, 참일 경우 참인 값을 출력
# print(0 or 100  )

# 한개의 정수형 입력이 들어올 때 홀,짝 판별
## 0을 제외한 숫자, 문자는 모두 참
## 나머지 값이 1인 경우(참, 홀수) 계산 순서에 따라 and연산이 먼저 실행 > 참 and 참이므로 홀 출력
## 나머지 값이 0인 경우(거짓, 짝수) and 연산을 통해서는 결과값은 거짓 > 거짓 or 참 이므로 참인 값 짝 출력
# var = int(input())
# print(var%2 and "홀" or "짝")

# xor 구현
# a, b = map(int, input().split(' '))
# if (not(a) and (b)) or (a and not(b)) : 
#     print("1")
# else :
#     print("0")

# 참, 거짓이 서로 같을 때 참을 출력
# a, b = map(int, input().split(' '))
# if (a and b) or (not(a) and not(b)) :
#     print("1")
# else : 
#     print("0")

# 모두 거짓일 때만 참을 출력
## 두 값이 모두 같고, 두 값이 거짓일 때만
## 이 계산에서는 두 값이 반전되기 때문에 1 1이 들어오면 0 0이 되고, 거짓 and 거짓은 거짓이므로 and결과에 따라 뒤의 값인 거짓(0)을 출력
# a, b = map(int, input().split(' '))
# if not(a) and not(b) : 
#     print("1")
# else :
#     print("0")

'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-12
범위 : 파트9. 비트단위 논리연산
'''
# 직사각형을 만드는데 4개 중 3개의 좌표가 주어졌을 때 나머지 한개를 구하기
c = [[1,4],[3,10],[3,4]]
x = []
# for i in range(2) : 
#     if (c[0][i]^c[1][i]) == 0 : 
#         x.append(c[2][i])
#     elif (c[0][i]^c[2][i]) == 0 : 
#         x.append(c[1][i])
#     elif (c[1][i]^c[2][i]) == 0 : 
#         x.append(c[0][i])
# print(x)

## 같은 수끼리 XOR연산하면 값은 0이 됨을 적용(연산의 순서상관없이 같은수끼리 XOR되면 0) > 한번만 나온 숫자 찾기 
x.append(c[0][0]^c[1][0]^c[2][0])
x.append(c[0][1]^c[1][1]^c[2][1])
print(x)