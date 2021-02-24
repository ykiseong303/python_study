'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-24
범위 : 파트13. 종합문제
'''
# 93. 이상한 출석번호 부르기 1
## 출석번호를 n번 무작위로 불렀을 때, 각 번호(1~23)가 출력된 횟수를 출력해보기.
'''
import random 
person = int(input())
# list comprehension으로 구현
# 1이상 23미만의 난수 > range 범위 설정과 같다고 생각하면 됌
student = [random.randrange(1,24) for x in range(1,person+1)]
print(student)
result = [0 for x in range(0,23)]
'''
'''
for i in student : 
    for j in range(0,23) : 
        if i == (j+1) : 
            result[j] += 1
print(*result)
'''
'''
# 실제 번호와 리스트의 인덱스는 -1의 차이가 있음을 활용
for i in student : 
    result[i-1] += 1 
print(result)
print(result[i], i)
'''

# 94. 이상한 출석번호 부르기 2
## 출석번호를 n번 무작위로 부를때, 부른 번호(1~23)를 거꾸로 출력해보기 
'''
import random
person = int(input())
student = [random.randrange(1,24) for i in range(0,person)]
print (student)
for i in range(person-1, -1, -1) :
    print(student[i], end=' ')
'''
'''
# reverse 함수 사용하기
import random
person = int(input())
# student = list(map(int, input().split()))
student = [random.randrange(1,23) for x in range(0,person)]
print(student)
student.reverse()
print(student)
'''

# 95. 이상한 출석번호 부르기 3 
## 출석번호를 n번 무작위로 부를때, 가장 빠른 번호를 출력하기 
'''
import random
person = int(input())
# student = list(map(int, input().split()))
student = [random.randrange(1,23) for x in range(0,person)]
print(student)
# min을 이용
print(min(student))
'''
## 비효율적이지만 오름차순 정렬 후, 0번째의 값을 출력
## 선택정렬을 사용
'''
min = student[0] 
index = 0
for i in student : 
    if min > student[index] : 
        min = student[index]
    index += 1
print(min)
'''