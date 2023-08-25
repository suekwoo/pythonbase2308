# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:19:09 2023

@author: KITCOOP
"""

###########################
#  함수와 람다
#  함수:def 예약어 사용
###########################

def func1() :
    print("func1() 함수 호출됨")
    return 10  #함수 종료 후 값을 리턴

def func2(num) :
    print("func2() 함수 호출됨:",num)
     #리턴값이 없는 함수
a=func1()
print(a)
b=func2(100)
print(b)
func2('abc')

#전역변수 : 모든 함수에서 접근이 가능한 변수
#지역변수 : 함수 내부에서만 접근이 가능한 변수

def func3() :
    c=300 #지역변수
    print("func3() 함수 호출:",a,b,c)
def func4() :
    a=110 #지역변수
    b=220 #지역변수
    print("func4() 함수 호출:",a,b)
#함수 내부에서 전역 변수값 수정하기
def func5() :
    global a,b   #a,b 변수는 전역변수를 사용함
    a=110
    b=220
    print("func5() 함수 호출:",a,b)

a=100
b=200

func3()
#print("main:",a,b,c)      #c 변수는 func3() 함수에서만 사용가능
print("main:",a,b)
func4()
print("main:",a,b)
func5()
print("main:",a,b)

#매개변수
def add1(v1,v2):
    return v1+v2
def sub1(v1,v2):
    return v1-v2

hap = add1(10,20)
sub=sub1(10,20)
print(hap)
print(sub)

hap = add1(10.5,20.1)
sub=sub1(10.5,20.1)
print(hap)
print(sub)


hap = add1("python","3.9")
print(hap)
# sub=sub1("python","3.9")
#hap = add1("python","3.9", "aaaa")


#가변 매개 변수 : 매개변수의 갯수를 정하지 않음 경우
def multiparam(* p) :
    result = 0
    for i in p :
        result += i
    return result
print(multiparam())
print(multiparam(10))
print(multiparam(10,20))
print(multiparam(10,20,30))
print(multiparam(1.5,2.5,3))


print(multiparam("1.5",2.5,3))  #result += i error


#매개변수에 기본값 설정
def hap1(num1=0,num2=1) :  #매개변수가 없는 경우 0,1 기본값 설정됨
    return num1+num2

print(hap1())    #num1=0,num2=1 기본값 설정
print(hap1(10))  #num1=10,num2=1 기본값 설정
print(hap1(10,20)) #num1=10,num2=20
print(hap1(0,20))  #num1=0,num2=20


# print(hap1(10,20,30)) #오류


#리턴값 두개인 경우 : 리스트로 리턴
def multiReturn(v1,v2) :
    list1=[]
    list1.append(v1+v2)
    list1.append(v1-v2)
    return list1

list1=multiReturn(200,100)
print(list1)


# 계산기호인자 값에 따라서 뒤의 가변인자값을 계산하는 함수 정의
def calChoice(choice, *args):
    if choice == '*':
        res = 1
        for i in range(0, len(args)):
            res *= args[i]
        return print(f'계산결과 = 곱 : {res}')
    elif choice == '+':
        res = 0
        for i in range(0, len(args)):
            res += args[i]
        return print(f'계산결과 = 합 : {res}')
    else:
        return print('계산 오류')
    
calChoice('*', 20, 30)
calChoice('+', 20, 30, 50)
calChoice('!', 20, 30 ,50)

# 딕셔너리 가변인자 **kwargs

def dictDefine(**kwargs):
    print('='*30)
    print(kwargs)
#     kwargs.sort() 에러
    for k in kwargs:
        print(k,':', kwargs[k])
    print('\n딕셔너리의 총 길이는?', len(kwargs))
# 함수 호출
dictDefine()
dictDefine(a='apple', b='banan', c='carrot')
dictDefine(n='nano', u='umbrella', m='moutain', s='sweet', d='dress')


# 람다식을 이용한 함수
hap2=lambda num1,num2:num1+num2  
#print(hap2(10))  #오류 
print(hap2(10,20))  #30
print(hap2(10.5,20.5)) #31.0

#기본값 매개변수
hap3=lambda num1=0,num2=1:num1+num2
print(hap3(10))  #11
print(hap3(10,20))  #30
print(hap3(10.5,20.5)) #31.0


#문제:리스트의 평균을 구해주는 함수 getMean 구현하기

def getMean(li) :
    if len(li)>0 :
        return sum(li)/len(li)
    else:
        return 0


list1 = [1,2,3,4,5,6]
print(getMean(list1))
print(getMean([]))

# lambda  p : 명령문 
getMean2 = lambda li : sum(li)/len(li) if len(li)>0 else 0
print(getMean2(list1))
print(getMean2([]))

#mylist1 보다 각각의 요소가 10이 더많은 요소를 가진 mylist2 생성
mylist1=[1,2,3,4,5]
mylist2=[] #11,12,13,14,15

#1 반복문
for n in mylist1 :
    mylist2.append(n+10)
print(mylist2)


#2 컴프리헨션
mylist2=[ n+10   for n in mylist1 ]
print(mylist2)

#3 map 방식
#map(함수,리스트) : 리스트의 각 요소에 함수(add10) 적용
def add10(n) :
    return n+10

mylist2=list(map(add10, mylist1))
print(mylist2)


#4 map 람다방식 
mylist2=list(map(lambda n:n+10, mylist1))
print(mylist2)


#filter()
#일반함수 + filter()

#숫자 리스트에서 짝수만 추출하여 새로운 리스트로 반환

def evenNumber(dataList):
    resList = []
    for i in dataList:
        if i % 2 == 0:
            resList.append(i)
    return resList
print(evenNumber([13, 50, 47, 67, 12, 34, 55, 134, 85, -41, -85, -36]))



list1 = [13, 50, 47, 67, 12, 34, 55, 134, 85, -41, -85, -36]
# filter() + 일반 함수 스타일
# 1) 값이 짝수이면 True, 아니면 False인 일반 함수 정의

def evenNum(n):
    return n % 2 == 0

# 1-1) 람다로 변경
evenNum2 = lambda n:n % 2 == 0

# 2) Test 호출
print(evenNum(5))
print(evenNum(-3))
print(evenNum(8))

# filter() + 일반 함수 스타일
print(list(filter(evenNum, list1)))

# 람다식을 filter(True or False return 함수,  collection)
print(list(filter(lambda n:n % 2 == 0, list1)))



# filter(filter()) 함수를 이용하여 다음 문자열에서 숫자만 리스트로 만들어 출력하여라
message = 'ab4690cfvg342가1나1다0'

print(list(filter(lambda n:n.isdigit(), message)))



















