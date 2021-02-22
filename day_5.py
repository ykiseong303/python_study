'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-20
범위 : 파트10. 삼항연산자
'''

# 파이썬의 삼항연산자는 '조건식' and (참일때의 값) or (거짓일때의 값)
# and는 모두 참일 경우 뒤의 값을 출력, or는 모두 참일 경우 뒤의 값을 출력
# 0 or '거짓' 에서 앞이 거짓일 경우 뒤의 값을 출력, 앞이 참일 경우 앞의 값을 출력 (인터프리터 방식, 앞이 참이므로 뒤를 볼필요도 없음)
'''
print( 3 > 10 and '참'  or '거짓')
'''

# 3개의 수 중에서 최소 값 찾기 (삼항연산자 사용)
'''
a,b,c = map(int, input().split())
num = b if a>b else a 
print(c if num > c else num )
'''

# 입력 받은 수가 짝수인지 판별
'''
num = int(input())
print("짝" if not num%2 else "홀")
'''


'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-20
범위 : 파트11. 조건-선택 실행구조(람다식)
'''

# 세 정수 a,b,c가 입력 되었을때 짝수만 출력
'''
a,b,c = list(map(int, input().split()))
print(*filter(lambda var : not var%2 , [a,b,c]))
'''
# 세 정수 a,b,c가 입력 되었을 때 짝수(even)와 홀수(odd) 구분
## for와 삼항연산자를 이용한 방법
'''
for i in [a,b,c] : 
    print("even" if not i%2 else "odd")
'''
## map함수는 iterable 데이터가 function구문으로 들어가 수행을 마친 것들을 묶어서 반환 
'''
print(*map(lambda x : "even" if not x%2 else "odd", [a,b,c]))
'''

'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-20
범위 : 파트12. 재귀함수
'''
# 정수가 일렬로 입력될 때 0을 만나면 출력 중지 
## for문을 활용한 방법 
'''
var = list(map(int, input().split()))
index = 0
for i in var : 
    if var[index] == 0 : 
        break
    print(var[index], end=" ")
    index += 1 
'''

## 재귀함수를 사용한 방법
'''
def goto (var, index) :
    if var[index] == 0: 
        return
    print(var[index], end=' ')
    index += 1
    goto(var, index)
    return 
var = list(map(int, input().split()))
goto(var, index = 0)
'''

# 입력 받은 숫자의 크기만 큼 임의의 수를 입력하고 하나하나 출력하기
'''
def goto(n,num,i) :
    if i>4:
        return  
    print(num[i])
    i+=1
    goto(n,num,i)
n = int(input())
num = list(map(int, input().split()))
goto(n,num,i=0)
'''

# 입력받은 숫자 ~ 0까지 출력
'''
num = int(input())
for i in range(num,-1,-1) : 
    print(i)
'''

# 입력받은 숫자-1 ~ 1까지 출력
'''
num = int(input())
for i in range(num-1, 0, -1) :
    print(i)
'''

# 영문자 1개 입력받았을 때, 그 문자까지 순서대로 알파벳 출력
# 공백을 두고 출력한다
'''
var = ord(input())
for i in range(97, var+1) : 
    print(chr(i), end=' ')
'''


