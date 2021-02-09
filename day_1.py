
# #url = "http://naver.com"
# url = "http://google.com"
# #규칙1 
# url = url.replace("http://", "")
# #규칙2 : 처음 만나는 점(.)이후 부분은 제외
# url = url[:url.index(".")]
# #규치3 : 글자 개수 + 알파벳 e의 개수
# password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
# print(password)


# num_list = [10,20,30]
# print(num_list)
# num_list.append(40)
# print(num_list)
# num_list.insert(1,-10)
# print(num_list)
# num_list.pop()
# print(num_list)
# str_list=["a","b","c"]
# str_list.extend(num_list)
# print(str_list)

# cabinet = {"A" : "유재석", "B" : "박명수"} # 리스트는 []으로 사전은 {}으로 시작함에 유의
# print(cabinet)
# print(cabinet["A"])
# #print(cabinet["C"]) # 없는 값에 대해서는 에러 출력 (멈춤)
# print(cabinet.get("C")) # 없는 값에 대해서는 none으로 출력 (멈춤 x)
# print(cabinet.get("C", "사용가능"))

# cabinet["A"] = "김태호"
# print(cabinet)

# print(cabinet.keys()) # 사전의 key값들만 출력
# print(cabinet.values()) # 사전의 value값들만 출력
# print(cabinet.items()) # 사전의 key와 value 값을 동시에 출력

from random import *

# player = list(range(20)) # player = range(1,21)
# for i in player : 
#     player[i] = i+1
# print(player)

# #리스트를 무작위로 셔플

# random.shuffle(player)
# print(player)
# chicken = random.sample(player,1)
# print(chicken)
# player = set(player) - set(chicken) # set끼리 연산을 거치고 나면 알아서 정렬??
# player = list(player)
# random.shuffle(player)
# coffee = random.sample(player,3)
# print(coffee)
# print(coffee)

# print("--------")
# print("당첨자")
# print(f"치킨 당첨자 : {chicken}번")
# print(f"커피 당첨자 : {coffee}")
# print("--------")

# user = range(1,21)
# # print(user)
# # print(type(user))
# user = list(user)
# # print(user)
# # print(type(user))

# shuffle(user)
# winner = sample(user,4)
# print(winner)

# print("치킨 당첨자 : {}".format(winner[0]))
# print("커피 당첨자 : {}".format(winner[1:4]))

# weather = input("오늘의 날씨는? : ")
# if weather == "비" :
#     print("우산을 챙기세요")
# elif weather == "맑음" : 
#     print("날씨가 맑습니다")
# else : 
#     print("좋습니다.")

# cel = int(input("오늘의 기온은 ? : "))
# if cel >= 30 : 
#     print("30도 이상입니다.")
# elif cel < 20 : 
#     print("20도 미만입니다.")
# else :
#     print("20~30도 사이입니다.")
# index = 0
# x = list(range(0,11))
# for i in x :
#     print("{}".format(x[index]))
#     index += 1

user = ["박명수","유재석","김태호"]
# for owner in user : #리스트에 있는 값에 한개씩 접근
#     print("{}, 커피가 준비되었습니다.".format(owner))
# index = 0
# for owner in user : 
#     print("{}, 커피가 준비되었다.".format(user[index]))
#     index += 1
# index = 5
# while index >=0 : 
#     print("커피가 준비되었다. {}번 남았다.".format(index))
#     index -= 1
#     if index == 0 : 
#         print("폐기처분되었다.")
#         break;

# 조건에 맞을때까지 반복
# name = "토르"
# person = "주문자"
# index = 1
# while True :
#     print("{}, 커피 준비되었다. {}번 호출".format(name, index))
#     x = input("이름은 ? : ")
#     if x == "토르" : 
#         print("커피 받으세요.")
#         break;
#     index += 1 

# absent = [2, 5]
# student = range(1,11)
# no_book = [7]
# for x in student : 
#     if x in absent : 
#         print("{}번 결석입니다.".format(x))
#         continue 
#     if x in no_book : 
#         print("{}번 책이 없습니다.".format(x))
#         break;
#     print("{}번 책 읽어봐".format(x))

# students = ["namuu", "babo", "gosu"]
# # students = [len(x) for x in students]
# # print(students)
# students = [x.upper() for x in students]
# print(students)

import random
person = [random.randrange(5,51) for x in range(1,51)]
print(person)
flag = 0
index = 1
for i in person : 
    # print("[{}], {}번째 손님 (소요시간 : {})".format("O" if 5 <= i <= 15 else " ", index,i))
    if 5 <= i <= 15 :
        print("[{}],{}번째 손님 (소요시간 : {})".format("O", index, i))
        flag += 1
    else :
        print("[{}],{}번째 손님 (소요시간 : {})".format(" ", index, i))
    index += 1 
print("총 탑승 승객 : {}명".format(flag))