# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:27:36 2023

@author: KITCOOP
"""

############################
#  Collection : 여러개의 데이터 저장할 수 있는 객체
#   list(리스트) : 배열의 형태.인덱스사용가능. []로 표시함.
#   tuple(튜플) : 상수화된 리스트.변경불가리스트. ()로 표시함
#   set(셋) : 중복불가. 집합  {}로 표시함
#   dictionary(딕셔너리) : 자바의 Map. (key,value)쌍인 객체들 {}로 표시함
############################

'''
  Collection : 데이터의 모임. 
    리스트(list) : 배열. 순서유지. 첨자(인덱스)사용 가능. []
    튜플(tuple) : 상수화된 리스트. 변경불가 리스트.       ()
    딕셔너리(dictionary) : (key,value)쌍 인 객체         {} 
                 items() : (key,value)쌍 인 객체를 리스트 형태로 리턴
                 keys()  : key들만 리스트형태로 리턴
                 values() : value들만 리스트형태로 리턴
    셋(set)  : 중복불가. 순서모름. 첨자(인덱스)사용 불가. 집합표현 객체.  {}
                 &, intersection() : 교집합
                 |, union() : 합집합.
                 
  컴프리헨션(comprehension) : 패턴(규칙)이 있는 데이터를 생성하는 방법
'''










#리스트
a=[0,0,0,0] #[10,20,30,40]
b=[]
print(a,len(a)) #len(a) : 리스트 요소의 갯수
print(b,len(b))




#a 리스트의 길이 만큼 숫자를 입력받아, a에 저장하고, 입력받은 수의
# 전체 합계를 출력하기
hap=0
for i in range(len(a)) :#i: 0 ~ 3
    a[i] = int(input(str(i+1)+'번째 숫자 입력: '))
    hap += a[i]
print(a,"요소의 합:",hap) 
print(a,"요소의 합:",sum(a))  #sum(리스트) : 리스트요소의합  




#a 리스트의 길이 만큼 숫자를 입력받아, 
# b에 저장하고, 입력받은 수의 합계 출력하기
for i in range(len(a)) :#i: 0 ~ 3
    #b리스트 요소는 없으므로 0번인덱스에 해당하는 b[0]은 없다
#    b[i] = int(input(str(i+1)+'번째 숫자 입력: ')) #오류발생
     #b.append : b리스트에 요소를 추가.
     b.append(int(input(str(i+1)+'번째 숫자 입력: ')))
print(b,"요소의 합:",sum(b)) #sum(b) : b요소의 합   
#%s : 문자열표현의 형식 문자. list값도 %s로 사용 가능
print("b=%s" % b)





a=[11, 22, 33, 44] 
#리스트의 주요 함수
a.append(1)  #a 리스트에 1요소를 마지막 추가 
a
#a 리스트 정렬
a.sort()
a
#a 리스트의 마지막 요소 출력하기
len(a)
a[4]   #a리스트의 4번인덱스. 
a[len(a)-1] #a리스트의 마지막 인덱스. 
a[-1]       # 뒤에서 첫번째 인덱스. 마지막 인덱스 
a[-2]       # 뒤에서 두번째 인덱스
a
a.pop() #마지막 요소를 제거하여 출력
a  #[1, 10, 20, 30]


a.reverse() #요소의 순서를 역순으로 
a

#index(값) 함수 : 요소의 인덱스위치 리턴
a.index(11) 
a.index(400) #값이 없는 경우 오류 발생
a.find(400)  #함수오류. find 함수는 리스트에 없는 함수 

#insert(인덱스,값) : 리스트 중간에 요소를 추가
a
a.insert(1,222)  #입력위치, 값
a
#remove(값) : 해당 요소를 제거
a.remove(222)
a






b=[11, 22, 33, 44]
#extend() : a 리스트에 b리스트 추가
a.extend(b)
a
#10 요소의 갯수 출력하기
a.count(10)

#문자열을 분리하여 리스트로 저장하기
dd = "2022/11/25"  #문자열
c = dd.split("/")  #문자열 ---> 리스트
print(c)

#문제 : ss 문자열의 모든 숫자들의 합을 출력하기
ss = "10,20,50,60,30,40,50,60,30"
sslist = ss.split(",")
sslist
sum(sslist) #sslist 요소가 숫자가 아니고 문자열이므로 sum 사용 불가

hap=0
for n in sslist :
    hap += int(n) #n의 값을 정수형 형변환
print(sslist,"의 요소의 합:",hap) 











#map 함수 : 리스트의 요소에 적용함수를 설정 
print(sslist,"의 요소의 합:",sum(list(map(int,sslist))))
#map(함수이름 ,리스트) : 리스트의 요소들마다 함수 적용   
#map(int ,sslist) : sslist의 모든 요소들이 int 함수 적용
#    하여 요소의 자료형이 정수형으로 변환
# list 함수 : 리스트로 변환

type(map(int ,sslist))  #map
mlist = list(map(int ,sslist))
mlist
sum(mlist)   















##### dictionary : {key1:value1,key2:value2,,,}
score_dic = {'lee':100,'hong':70,'kim':90}
print(score_dic)
print(type(score_dic))

#hong의 점수 출력하기
# value <= dict['key']
score_dic['hong']
#hong 의 점수 75점으로 수정하기
score_dic['hong'] = 75
print(score_dic)
#park 의 점수 80점으로 추가하기
score_dic['park']=80
print(score_dic)

#park 정보 제거하기
del score_dic['park']
print(score_dic)

#키값만 조회
print(score_dic.keys())
print(list(score_dic.keys()))
#값들만 조회
print(score_dic.values())
print(list(score_dic.values()))
#키와값들의 쌍인 값으로 조회
print(score_dic.items())
print(list(score_dic.items()))

#dictionary 객체들을 반복문으로 조회
for n in score_dic :
    #n : key값
    print(n,"=",score_dic[n])

for n in score_dic.keys() :
    #n : key값
    print(n,"=",score_dic[n])

for n,s in score_dic.items() :
    #n:키값
    #s:value값
    print(n,"=",s)
    
#[('lee', 100), ('hong', 75), ('kim', 90)]
for v in score_dic.items() :
    #v :튜플객체. (k,v)쌍인 객체('kim', 90)
    print(v[0],"=",v[1])
    print(v) #('kim', 90),

for s in score_dic.values() :
    print(s) #key값을 조회 못함   
    


'''
문제 : 1. 궁합음식의 키를 입력받아 해당되는 음식을 출력하기
         등록안된 경우 오류 발생. => 등록여부 판단필요
       2.종료 입력시 등록된 내용 출력하기
         등록된음식 :
              떡볶이 : 오뎅
              짜장면 : 단무지
       3. 등록이 안된경우 
          등록여부를 입력받아, 등록하는 경우 궁합음식을 입력받기  
          등록하시겠습니까(y)? 
             y입력 : foods객체에 추가.
                     궁합음식 입력받아서 foods에 추가함
             y가아닌경우 :
                     음식을 다시 입력하기    
              
''' 
foods = {"떡볶이":"어묵","짜장면":"단무지","라면":"김치","맥주":"치킨"}
while True :
    myf = input(str(list(foods.keys())) + "중 입력(종료):")
    if myf == '종료' :
        break
    if myf in foods :  #foods 데이터의 키값 중 myf값이 존재?
        print("%s의 궁합음식:%s" % (myf,foods[myf]))
    else :  # 입력된값(myf)이 foods의 키값에 없는 데이터인 경우
        print("%s는 등록된 음식이 아닙니다" % myf)
        y = input(myf+"를 등록하시겠습니까(y/n)?")
        #y.lower() : y 문자열을 소문자로 변경
        if y.lower() == 'y' : # y=Y|y 
            #myf2 : 입력된 궁합음식 값
            myf2 = input(myf + "의 궁합음식 입력:") #궁합음식 입력
            foods[myf] = myf2  #(myf(키),myf2(값))   




print("등록된 음식:")    
for f in foods.items() :
    print(f[0],":",f[1])
    print(f)
for f in foods :
    print(f,":",foods[f])  
    
################# 튜플 : 상수화된(변경 불가) 리스트. ( )    

tp1 = (10,20,30)
print(tp1)

for t in tp1:
   print(t)

#인덱스 사용 가능   
print(tp1[0],tp1[1],tp1[2])
tp1.append(40) #튜플은 변경안됨
tp1[0]=100     #튜플은 변경안됨


#튜플객체를 변경하기 위해서는 리스트로 변경하면됨.
list1 = list(tp1)
list1.append(40)
list1[0]=100
list1
#tuple() : 튜플객체로 변경
tp1=tuple(list1)
tp1


#tp1의 요소의 갯수와 변수의 갯수가 동일하면 사용가능
a,b,c,d = tp1
print(a,b,c,d)

#tp1의 요소의 갯수 구하기
print(len(tp1))
#list1의 요소의 갯수 구하기
print(len(list1))

#tp1의 요소의 합구하기
print(sum(tp1))
#list1의 요소의 합구하기
print(sum(list1))

#2,3번째 요소만 출력하기
print(tp1[1],tp1[2])
print(tp1[1:3])
print(tp1[:3])
print(tp1[::2])


# 튜플 연산
my_tuple = (1, 2, 3)
print(my_tuple*3)
print(my_tuple + my_tuple)

# Named Tuple => 반드시 1:1 대응!
student = (name, age, gender) = ('제인', 27, '여')
# ('제인', 27, '여', True)의 경우 1:1이 아니라서 안 됨

print(f'학생 정보 = {student}', type(student))
print(f'이름 = {name}', type(name))
print(f'나이 = {age}', type(age))
print(f'성별 = {gender}', type(gender))

# 중첩 튜플과 리스트 튜플

# 중첩 튜플
t_2d = ((10, 30), (50, 100), (45, 34))

# 리스트 튜플 (리스트 안은 튜플) => type은 리스트
tlist_2d = [(10, 30), (50, 100), (45, 34)]

# 튜플 안은 리스트
ltuple_2d = ([10, 30], [50, 100], [45, 34])

print(t_2d, type(t_2d), len(t_2d))
print(tlist_2d, type(tlist_2d), len(tlist_2d))
print(ltuple_2d, type(ltuple_2d), len(ltuple_2d))

print(t_2d[-1], t_2d[1][1])
print(tlist_2d[0], tlist_2d[-1][-1])


tp1 #(100, 20, 30, 40)
#tp1의 요소를 역순으로 출력하기 
#tp1.reverse()   #역순으로 객체를 수정. 튜플에서 불가
list1.reverse() #역순으로 객체를 수정 
list1 
#(40, 30, 20, 100)
#1 tp1 요소를 역순으로 출력
for i in range(len(tp1)-1,-1,-1) :
    print(tp1[i],end=",")

#2 
print(tp1[::-1]) #역순 출력
tp1
print(list1[::-1]) #역순 출력


############## set : 중복불가. 집합을 표현하는 객체 {}
set1 = {30,10,20,10}
print(set1) #10 요소는 한개만 출력됨. 순서지정안됨
#print(set1[0]) #인덱스 사용 불가

#집합 구현하기
set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,1,2,3,4,5}
print(set1)
print(set2)
set3 = {5,6,7,8}
#교집합 : 두개의 집합에 공통 요소들
print("set1과 set2의 교집합 요소:",set1 & set2)
print("set1과 set3의 교집합 요소:",set1 & set3)
print("set1과 set3의 교집합 요소:",set1.intersection(set3)) #교집합 함수 
#합집합 : 두개의 집합에 속한 모든 요소들
print("set1과 set2의 합집합 요소:",set1 | set2)
print("set1과 set3의 합집합 요소:",set1 | set3)
print("set1과 set3의 교집합 요소:",set1.union(set3))

del set3


#### comprehension(컴프리헨션) 방식으로 Collection 객체 생성
# 규칙성이 있는 데이터를 Collection 객체의 요소로 저장하는 방식
# numbers 리스트 : 1 ~ 10까지의 데이터 저장
#1. 값을 대입
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
#2. 반복문 이용
numbers=[]
for n in range(1,11) : #1~10
    numbers.append(n)
print(numbers)

#3.컴프리헨션 이용
numbers=[x for x in range(1,11)]
print(numbers)


# numbers 리스트 : 2 ~ 20까지의 짝수 데이터 저장
#1
numbers=[x*2 for x in range(1,11)]
print(numbers)
#2
numbers=[x for x in range(2,21,2)]
print(numbers)
#3
numbers=[x for x in range(1,21) if x%2==0]
print(numbers)


# 문제 : 1 ~ 20까지의 수 중 2의 배수와 3의 배수만을 nums 리스트에 
# 데이터 저장.

numbers=[x for x in range(1,21) if (x%2==0) | (x%3==0)]
print(numbers)

numbers=[x for x in range(1,21) if (x%2==0) or (x%3==0)]
print(numbers)


#두개의 리스트 데이터를 각각 한개식 튜플로 생성하고, 
# 튜플을 리스트로 생성하기
clist=['black','white']
slist=['S','M','L']
# [(black,S),(black,M),(black,L),(white,S),(white,M),(white,L)]


#1 반복문이용
dlist = [] #('black','S'),('black','M'),('black','L'),('white','S')..
for c in clist :   #'black','white'
    for s in slist :   #'S','M','L'
        dlist.append((c,s))
print(dlist)

#2 컴프리헨션 방식
dlist=[(c,s) for c in clist for s in slist] 
print(dlist)


dlist=[[c,s] for c in clist for s in slist] 
print(dlist)


#1 ~10사이의 짝수 제곱값을 가진 set 객체 생성하기
set1 = {x*x for x in range(1,11) if x%2==0}
print(set1)

set1 = {x*x for x in range(2,11,2)}
print(set1)


#dictionary 데이터 생성하기
products = {"냉장고":220,"건조기":140,"TV":130,"세탁기":150,"컴퓨터":200}
#200미만의 제품만 product1 객체 저장하기
product1={} # '건조기':140,'TV':130

for k in products :  #k=TV
    if products[k] < 200 :   #130
       product1[k] = products[k]
print(product1)

product1={}
for k in products.keys() :
    if products[k] < 200 :   
       product1[k] = products[k]
print(product1)

product1={} # '건조기':140,'TV':130
for k,v in products.items() : #k="TV" v=130
    if v < 200 :   
       product1[k] = v
print(product1)

#comprehension 방식으로 #dictionary 데이터 생성하기 ㅔㄱ

product2 = { k:v    for k,v in products.items()   if v < 200          }
print(product2)

product2 = { k:products[k]    for k in products   if products[k] < 200          }
print(product2)
