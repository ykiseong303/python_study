'''
코드업 기초 100제(파이썬)
날짜 : 2021-02-23
범위 : 파트13. 종합문제
'''

# 85. 소리파일 저장용량 계산하기 
## bit > byte > kbyte > Mbyte의 단위 이동에 대한 이해가 필요함
## 소리파일의 각 값인 h,b,c,s가 입력될 때(bit단위) 소수점 1의자리까지 반올림하여 MB 단위로 출력
## 위의 단위로 변환하는 경우 최소 단위 ~ 해당단위까지의 비트수로 나누기, 작은 단위로 가려면 곱하기로 바꾸면 됨
'''
h, b, c, s = map(int,input().split())
result = h*b*c*s 
resultMB = result / (8* 1024**2)
print("용량은 : ", round(resultMB,1), "MB")
'''
# 86. 그림파일 저장용량 계산하기 
## 85번과 마찬가지로 저장용량에 대한 단위 변환이 필요함 
## 세 변수가 입력될 때(bit단위) 소수점 셋째자리에서 반올림하여  MB단위로 출력
'''
w, h, b = map(int,input().split())
result = w*h*b
resultMB = result / (8*1024**2)
print("용량은 : {}MB".format(round(resultMB,2)))
'''
# 87. 여기까지! 이제 그만 ~ 
## 1부터 임의로 입력된 n까지 더해갈때, 어디까지 더하면 n보다 커지는지 확인 (그때의 합을 출력)
'''
num = int(input())
total = 0
for i in range(1, num+1) : 
    total += i
    if total > num : 
        break
print(total)
'''
## while로 구현할때는 for문의 탈출조건을 반대로 구현하면됌
num = int(input())
total = 0
i = 1
while total <= num : 
    total += i
    i+=1
print(total)
