# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:17:40 2023

@author: KITCOOP
"""

#### 파일 읽기
'''
  open("파일명",파일모드,[인코딩])
  인코딩:파일의 저장방식. 기본값:cp949형식
  파일코드
    r :읽기
    w :쓰기. 기존의 파일의 내용을 무시. 새로운 내용으로 추가
    a :쓰기. 기존의 파일의 내용에 추가
    t : text 모드. 기본값
    b : 이진모드. binary모드. 이미지,동영상....   
'''
#파일 읽기
infp = open("C:\\Users\\KITCOOP\\python2308\\pybase07_re.py", "rt", encoding="UTF-8")
while True:
    instr = infp.readline() #한줄씩 읽기
    if instr == None or instr == '' :
        break
    print(instr, end="")
infp.close()


#파일 쓰기 :콘솔에 내용을 입력 받아 파일로  저장 하기
#현재 폴더에 data/data.txt에 저장한다

outfp = open ("data/data.txt", "w", encoding="UTF-8")
while True :
    outstr = input("내용입력 =>")
    if outstr == '':
        break
    outfp.writelines(outstr+"\n")
outfp.close()

'''
  readline() : 한줄씩 읽기
  read()     : 버퍼의 크기만큼 한번 읽기
  readlines() : 한줄씩 한번에 읽어서 줄별로 리스트로 리턴
'''

# data.txt 파일을 읽어서 화면에 출력하기
infp = open("data/data.txt","r",encoding="UTF-8")

while True :
    instr = infp.readline() #한줄씩 읽기
    if instr == None or instr == "" :
        break
    print(instr,end="")
infp.close()    

infp = open("data/data.txt","r",encoding="UTF-8")
print(infp.read())
infp.close()

infp = open("data/data.txt","r",encoding="UTF-8")
print(infp.readlines())
infp.close()


#이미지 파일 읽어 복사하기
#apple.gif 파일을 읽어서 apple2.gif로 복사하기

infp = open("data/apple.gif", "rb" )
outfp = open("data/apple2.gif", "wb")

while True:
    indata = infp.read()
    if not indata : #파일의 끝 EOF(End of File)
       break 
    outfp.write(indata)
infp.close()
outfp.close()







