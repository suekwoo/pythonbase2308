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







