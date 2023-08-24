# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:40:18 2023

@author: KITCOOP
"""

"""
# F9 키로 한줄또는 선택영역 실행
# 한줄 주석
"""
#   여러줄 주석

'''
   여러줄 주석
   여러줄 주석은 나중에 문자열 표현에서도 사용됨. 
'''

print('hello')
print("hello")
#여러개의 데이터 화면에 출력
print(10,20,30,40,50)
#문자열을 여러번 출력
print("abc"*3)
print('abc'*3)


#문자열+숫자 안됨.
print("학번:"+100) #오류발생
print("학번:",100)
print("학번:"+"100") #문자열간의 +연산은 가능함
print("학번:"+str(100)) #str() : 문자열로 변환
print("'안녕하세요' 라고 말했습니다.")
print('"안녕하세요" 라고 말했습니다.')


#\"
print("\"안녕하세요\" 라고 말했습니다.")
print('\'안녕하세요\' 라고 말했습니다.')

# \n : new line
print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사")


#\ 라인 연결. 다음라인도 연결된 문장.
print("동해물과 백두산이 마르고 닳도록 \
      하느님이 보우하사")
      
'''
  여러줄 주석
  문자열의 """ 표시는 여러줄 문자열 표시에 사용가능함
'''
print("""동해물과 백두산이 마르고 닳도록
 하느님이 보우하사 우리나라 만세
 무궁화 삼천리 화려강산""")
 
 
#10 20 30 출력
print(10,end="\t") 
print(20,end="\t")
print(30,end="\n") #end 속성값의 기본값 : \n.
#10,20,30 출력
print(10,end=",")
print(20,end=",")
print(30) 
 
 
 
# print("문장의 처음에 공백이 있으면 오류") #오류 
 
 
#문자열 : 문자들의 모임. 문자여러개. 문자의 배열로 인식
print("안녕하세요"[0]) #안
print("안녕하세요"[2]) #하 


#문자열의 범위를 지정하여 출력하기
#문자열[첫번째인덱스:마지막인덱스+1:증감값]
print("안녕하세요"[0:2]) #안녕. 0번인덱스부터 1번인덱스까지
print("안녕하세요"[:2]) #안녕.  처음부터 1번인덱스까지
# 처음부터 4번인덱스까지 2칸씩
print("안녕하세요"[:5:2]) #안하요. 
print("안녕하세요"[2:]) #하세요. 2번인덱스 이후 
print("안녕하세요"[::2])#안하요
print("안녕하세요"[::-1])# 뒤부터   요세하녕안  
 
len=9
#len() : 문자열의 길이
print(len("안녕하세요"))
len("안녕하세요") 


#### 자료형 : 변수선언하지 않고 사용
# 변수의 자료형은 값으로 결정됨.
n = 10
type(n)
n = 10.5
type(n)
n='안녕'
type(n)


#### 연산자 
# 산술연산자 : +,-,* , /, %, // ,**
5+7
5*7
5/7
7%5
5%7
5//7  #정수형 몫의 값
5**2  # 5*5. 제곱
5^2  # 비트연산자 (XOR)

# 문제 : 3741초가 몇시간 몇분 몇초인지 출력하기 ( 1 시간 2 분 21 초)

print(3741//3600,"시간",(3741%3600)//60,"분",\
      (3741%60),"초")
    

    
# 키보드에서 초를 입력받아 몇시간 몇분 몇초인지 출력하기
# input함수:키보드에서 입력받기.
#           문자열형태로 입력받음.


second = int(input("초를 입력하세요:"))
print(second//3600,"시간",(second%3600)//60,"분",\
      (second%60),"초")
    
#대입연산자 : =, +=, -=, *=,....
a=10
a += 10
a    
a -=5
a    
a *=2    
a

# 문자열에서 사용가능한 대입연산자 : =, +=, *=
s= "abc"
s += "d"
s
s *= 3
s    


#자연수를 입력받아 +100을한 값을 출력하기
num = int(input("자연수를 입력하세요"))
num += 100
print(num)


#형변환 함수
# int() : 정수형으로 변환
# float() : 실수형으로 변환
# str() : 문자열형으로 변환
print("num+100="+str(num))
print("num+100=",num)

#2,8,16 진수를 10진수로 변환
print(int("11",2))
print(int("11",8))
print(int("11",16))
#10진수를 2,8,16진수로 변환
print(10,"의 2진수:",bin(10))
print(10,"의 8진수:",oct(10))
print(10,"의 16진수:",hex(10))



#형식문자를 이용하여 출력하기 : 
#  %d(10진수정수)
#  %f(실수)
#  %s(문자열)
print("%d * %d = %d" % (2.0,3,6))
print("%f * %f = %f" % (2,3,6))
print("%.2f * %.2f = %.2f" % (2,3,6))
# %x,%X : 16진수 표현
print("%X" % (255))
print("%x" % (255))
print("안녕 %s!, 나도  %s" % ("홍길동","김삿갓"))



#format 함수를 이용한 출력
#{0:5d} : 첫번째값을 정수형 5자리로 출력
#{1:5d} : 두번째값을 정수형 5자리로 출력
#{2:5d} : 세번째값을 정수형 5자리로 출력
print("{0:5d}{1:5d}{2:5d}".format(100,200,300))
print("{1:5d}{2:5d}{0:5d}".format(100,200,300))

# 직접 변수이름으로 출력
a=100
b=200
print(f"{a},{b}")
print(a,b)

### 조건문 : if문
# 들여쓰기 해야함
score = 65


if score >= 90 :
    print("A학점")
    print("합격입니다.")
else : 
    if score >= 80 :
        print("B학점")
        print("합격입니다.")
    else :
       if score >= 70 :
         print("C학점")
         print("합격입니다.")
       else :
        if score >= 60 :
               print("D학점")
        else :
            print("F학점")
            
            
            
# if elif 구문
if score >= 90 :
   print("A학점")                
   print("합격입니다.")
elif score >= 80 :
   print("B학점")                
   print("합격입니다.")
elif score >= 80 :
    print("B학점")                
    print("합격입니다.")
elif score >= 60 :
   print("D학점")                
   print("합격입니다.")
else :
   print("F학점")                
   print("불합격입니다.")     


score = 70    
if(score >= 60) :
   print("합격입니다.")
   print("자격증을 받으러 오세요")   
    
# 점수가 60이상이면 PASS 60미만이면 FAIL을 출력하기
score = 65
if score >= 60 :
   print("PASS")
else :
   print("FAIL")    

if score >= 60 :
   print("PASS")
elif score < 60 :
   print("FAIL")    



# 간단한 조건식
# TRUE if 조건식 else FALSE
score = 65
print(score,"점수는",'PASS' if score>=60 else 'FAIL')       
    
    
# 반복문
#1부터 100까지의 합 구하기
num = 100
hap = 0
# range(1,num+1,증감값) : 1 ~ num까지의 숫자들
for i in range(1,num+1) :
    hap += i
print ("1부터 %d까지의 합:%d" % (num,hap))   


#1 ~ 100 까지 짝수의 합 구하기

hap=0
for i in range(1,num+1) :
    if i % 2== 0 :
       hap += i
print ("1부터 %d까지의 짝수합:%d" % (num,hap))   


hap=0
for i in range(2,num+1,2) :
    hap += i
print ("1부터 %d까지의 짝수합:%d" % (num,hap))   

#12345 반복문을 이용하여 출력하기
print(12345)

for i in range(1,6) :
    print(i,end="")


# while 조건문: 조건문의 결과가 참인 동안 반복함
num = 1
while num <= 5 :
  print(num, end="")
  num += 1      

#break : 반복문 종료
#continue : 반복문의 처음으로 제어 이동
hap = 0
for i in range(1,11) : #1 ~ 10
   if i == 5 :
       break;
   hap += i
print('hap=',hap) # 10   


hap = 0
for i in range(1,11) :
   if i == 5 :
       continue
   hap += i
print('hap=',hap)  # 50  



#1 ~ 45사이의 숫자 6개 출력하기
# 난수 생성하기
import random  #모듈 
rnum = random.randrange(1,46) #1~45까지의 임의의 수
print(rnum)

for i in range(1,7) :
    print(random.randrange(1,46),end=",")


'''
  컴퓨터가 1부터 99사이의 임의의 수를 저장하고, 
  숫자를 입력받아서 컴퓨터가 저장한 수를 맞추기.
  컴퓨터는 입력한 숫자가 정답과 비교하여 큰수,작은수 인지 출력.
  정답 입력시 입력한 횟수를 출력하기.
  1. 난수 생성.
  2. 정답을 맞추는 동안 계속 입력 받기. => while True : 
       정답이 입력되는 break
'''    
rnum = random.randrange(1,100) #1~99까지의 임의의 수

cnt = 0
while True :
    a = int(input("숫자를 입력하세요"))
    cnt += 1
    if a > rnum :
        print(a,"보다 작은수입니다.")
    elif a < rnum :    
        print(a,"보다 큰수입니다.")
    else :
        print("정답입니다.")
        print("%d번만에 정답을 맞췄습니다." % (cnt))
        break


#중첩반복문
i,j=0,0  #초기화 방식
for i in range(2,10) :  # 2 ~ 9
    print("%5d단" % i)
    for j in range(2,10) : # 2 ~ 9
        print("%2d X %2d = %3d" % (i,j,(i*j)))
    print()   


'''
1. 직각 삼각형 출력하기

*
**
***
****
*****

'''

h=5
### 1 ####
for i in range(1,h+1) :
   for j in range(1,i+1) :
       print("*",end="")
   print()    

### 2 ####
for i in range(1,h+1) :
   print("*"*i)   


'''
2. 역 직각 삼각형 출력하기

*****
****
***
**
*
'''
for i in range(h,0,-1) :
   print("*"*i)
   

'''
3. 역 직각 삼각형 출력하기
           
*****    
 ****      
  ***      
   **      
    *      
'''  
h=5  
for i in range(h,0,-1) :
   print(" " * (h-i),end="") 
   print("*"*i)



'''
4. 직각 삼각형 출력하기
         
    *     
   **     
  ***      
 ****      
*****      

'''
   
for i in range(1,h+1,1) :
   print(" " * (h-i),end="") 
   print("*"*i)
   
##### 문자열 함수 
'''
  len(문자열) : 문자열의 길이
  문자열.count(문자) : 문자열에서 문자의 갯수 리턴
  문자열.find(문자) : 문자열에서 문자의 위치 리턴
                     문자가 없는 경우 -1 리턴
  문자열.index(문자) : 문자열에서 문자의 위치 리턴
                     문자가 없는 경우 오류 발생
'''

a = "hello"
#a 문자열에서 l문자의 갯수 출력하기
cnt = 0
#len(a) : a문자열의 길이 5
for i in range(len(a)) : # 0 ~ 4까지값
    if a[i] == 'l' :
        cnt += 1
print(a,"에서 l 문자의 갯수:",cnt)  

print(a,"에서 l 문자의 갯수:",a.count('l'))  
print(a,"에서 a 문자의 갯수:",a.count('a'))  #0

#a 문자열에서 l문자의 위치(인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l'))  #2
print(a,"에서 l 문자의 위치:",a.index('l')) #2
 
#a 문자열에서 3번인덱스 부터 l문자의 위치(인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l',3))  #3
print(a,"에서 l 문자의 위치:",a.index('l',3)) #3
#a 문자열에서 3번인덱스 부터 o문자의 위치(인덱스) 출력하기
print(a,"에서 o 문자의 위치:",a.find('o',3))  #4
print(a,"에서 o 문자의 위치:",a.index('o',3)) #4




#a 문자열에서 4번인덱스 부터 l문자의 위치(인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l',4))  #-1
print(a,"에서 l 문자의 위치:",a.index('l',4)) #오류


#a 문자열에서 a문자의 위치(인덱스) 출력하기
print(a,"에서 a 문자의 위치:",a.find('a'))  #-1
print(a,"에서 a 문자의 위치:",a.index('a')) #오류. 예외처리필요


#문자열의 종류 알려주는 함수
ss = '123'
ss = 'Aa123'
ss = 'Aa'
ss = 'AA'
ss = 'aa'
ss = '     '
ss = '  aa   '
ss = '  Aa   '


if ss.isdigit() :
    print(ss,": 숫자")
if ss.isalpha() :
    print(ss,": 문자")
if ss.isalnum() :
    print(ss,": 문자 또는 숫자")
if ss.isupper() :
    print(ss,": 대문자")
if ss.islower() :
    print(ss,": 소문자")
if ss.isspace() :
    print(ss,": 공백")


'''
   print(값) : 화면에 출력하기
   print(값1,값2) : 값을 여러개 출력
   print("{0:d}{1:2d}...".format(값1,값2,...))  형식문자 이용하여 출력
   print("%2d,%3d" % (값1,값2)) : 형식문자 이용하여 값을 여러개 출력
   print(f"{변수1} {변수2}") : 변수에 해당하는 값을 출력
   print(""" 문자열 """) : 여러줄 문자열
   
   문자열 : 문자들의 모임. 인덱스(첨자)를 사용가능
   "문자열"[시작인덱스:종료인덱스+1:증감값]
      시작인덱스 생략시 : 0번부터시작
      종료인덱스 생략시 : 마지막문자까지
      증감값 생략시 : 1씩 증가 
      
   조건문 : if else, if elif else , True if 조건식 else False   

   반복문 : for 변수 in 범위 , while 조건식  
           범위 : range(초기값,종료값+1,증감식)
           break,continue
   조건문,반복문 : 들여쓰기에 주의.         
   
   문자열 함수
     len(문자열) : 문자열의 길이
     문자열.count(문자) : 문자열에서 문자의 갯수 리턴
     문자열.find(문자) : 문자열에서 문자의 위치 리턴  문자가 없는 경우 -1 리턴
     문자열.index(문자) : 문자열에서 문자의 위치 리턴 문자가 없는 경우 오류 발생
     문자열.isdigit() : 숫자?
     문자열.isalpha() : 문자?
     문자열.isalnum() : 숫자또는문자?
     문자열.isupper() : 대문자?
     문자열.islower() : 소문자?
     문자열.isspace() : 공백 ?
'''
