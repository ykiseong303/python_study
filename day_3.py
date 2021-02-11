'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-11
범위 : 파트3. 입출력(이어서)
'''

# 숫자 두개를 입력받아 정수형태로 출력하기
## split()의 구분자로 입력받는 값을 분리
## iterable 형태는 형변환이 바로 되지 않으므로 mapping과정을 거침
## 매핑 후 list형태로 재 변환
# var = list(map(int, (input().split(' '))))
# print(var[0], var[1])  #print(*var)으로도 출력가능
# print(*var)

# 실수를 입력받아 소수 셋째자리에서 반올림하고 둘째자리까지 출력
# var = round(float(input()),2)
# print(var)

# 기준문자를 통해 입력 구분하기 
#h, m = input().split(':')
#print("{}:{}".format(h, m))

# 연, 월, 일을 입력받아서 지정된 형식으로 출력 (월, 일은 한자리 일경우 0을 앞에 추가)
## input은 기본이 문자열로 받음
## '+'연산자를 통해 문자열끼리 붙임이 가능
# y, m, d = input().split('.')
# if len(m) == 1 :
#     m = '0' + m
# if len(d) == 1 :
#     d = '0' + d
# print("{}.{}.{}".format(y,m,d))

# 숫자를 입력받아 자리단위별로 출력
# integer = input()
# ## 자리수를 나타내기 위한 변수가 필요 
# count = len(integer) - 1 # 0의 개수는 해당위치의 자리수 -1
# for i in integer : # 파이썬에서 for문은 리스트나 어떤 항목에서 앞에 하나씩 끌어간다고 생각
#     print([int(i + '0'*count)]) # 문자 * 숫자형태로 문자의 출력횟수 조절 가능
#     count-=1 

# 연, 월, 일을 입력받아(기준은 . ) (dd-mm-yyyy)으로 출력
y,m,d = input().split('.')
# if len(m) == 1 :
#     m = '0' + m
# if len(d) == 1 :
#     d = '0' + d

m = '0'+m if len(m) == 1 else m # 3항 연산자를 이용한 방법 
d = '0'+d if len(d) == 1 else d # 조건이 맞다면 앞에 값을, 틀리다면 else의 값

print("{}-{}-{}".format(d,m,y))


