'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-10
범위 : 파트1. 출력
'''
# 두줄로 출력하기 : '''뒤에 \ 기호를 붙이면 한줄띄움 없이 바로 출력이 가능함
print('''\
Hello
World
'''
)
print('''
Hello
World''')
print("Hello\nWorld") # 탈출문자를 통해서도 가능

# 큰따옴표, 작은따옴표 출력하기
print('"Hello World"')
print("'Hello World'"+ "Hi")
print("\\") # \는 두번 입력하면 출력가능

'''
범위 : 파트2. 입출력
'''

# 정수형 변수를 입력 받은 후 출력
# var = int(input())
#print(var)
# 문자형으로 변수를 입력 받은 후 출력 : input함수는 반환값은 기본적으로 문자열로 지정되어있다.
var = input()
print(var)