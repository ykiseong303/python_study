'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-20
범위 : 파트13. 종합문제
'''

# 78. 짝수 합 구하기 
## 1부터 입력된 수까지 짝수의 합을 구한다
'''
num = int(input())
'''
# for 사용
'''
sum = 0
for i in range(1, num+1) : 
    if i%2 : 
        continue
    sum += i
print(sum)
'''
# range 사용
## 문제에서는 1부터라고 햇지만 2부터 2만큼 증가시키면 바로 짝수의 합을 구할 수 있음
## range는 범위 지정함수이므로 sum, list등을 사용해서 출력해줄 수 있음 
'''
print(sum(range(2,num+1,2))) 
'''
# list comprehension 사용
## [ '리스트로 만들어 줄 변수' for 구문 ]
'''
print(sum([i for i in range(2,num+1,2)]))
'''

# 79. 원하는 문자가 입력될때까지 반복 출력하기
## q가 입력될때까지 문자를 한줄마다 출력
''' 
# for 사용
arr = input().split()
for i in arr : 
    if i == 'q' : 
        break
    print(i)
'''

# 람다식 사용 (틀린 답)
## q를 제외하고서 출력이 됨 (q를 만나면 어떻게 멈춰야 하는지 아직 모르겠음)
'''
word = input().split()
print(*filter(lambda x : x!='q' , word))
''' 

# 80. 어디까지 더해야할까?
## 1부터 입력받은 n까지 더해간다고 할 때, 어디까지 더해야 입력받은 수보다 같거나 커지는지 구하기 
'''
end_point = int(input())

total = 0
for i in range(1, end_point+1) :
    total += i
    # 전체합과 비교하는 위치가 어디인지를 파악하는게 중요 
    if total >= end_point : 
        break 
print(i)
'''
'''
# while 문으로 실행
end_point = int(input())
total = 0
i = 0
while total < end_point : 
    i += 1
    total += i
print(i)
'''
