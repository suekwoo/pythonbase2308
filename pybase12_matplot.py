# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:44:27 2023

@author: KITCOOP
"""

#matplot 시각화 모듈
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



#한글이 가능한 폰트로 설정 : 맑은 고딕. 기본폰트:한글불가
plt.rc("font",family="Malgun Gothic")



#x축 데이터의 내용. 
subject = ["Oracle","Python","Sklearn","Tensorflow"]
#y축의 데이터값
score = [65,90,85,95]
#그래프가 그려지는 영역
fig = plt.figure()

# 그래프 영역을 분할
#ax1 : 그래프 작성 영역

ax1 = fig.add_subplot(2,1,1) #2행1열 1번째 영역
ax2 = fig.add_subplot(2,1,2) #2행1열 2번째 영역
#bar(x축의값,y축의값,가운데막대,막대그래프색상) : 막대그래프
#x축의값:range(len(subject)) : 0~3까지
#y축의값 : score :[65,90,85,95]
#align="edge"/"center"
ax1.bar(range(len(subject)),score,align="center",color="darkblue")
ax2.plot(range(len(subject)),score)
#x축의값을 숫자에서 subject의 내용으로 변경 
# rotation=45 : x축의 값 출력 각도
plt.xticks(range(len(subject)),subject,rotation=45,fontsize="small")
plt.xlabel("Subject") #x축값 설명
plt.ylabel("Score")   #y축값 설명
plt.title("Class Score")
plt.show()

###연합 그래프 작성
df = pd.read_excel("data/남북한발전전력량.xlsx")
df.info()
df
#북한지역의 발전량만 조회.
df = df.loc[5:]
df
df.info()
#전력량 (억㎾h) 컬럼 제거
#df.drop("전력량 (억㎾h)",axis=1, inplace=True) 
del df["전력량 (억㎾h)"]
df.info()
df["발전 전력별"]
#발전 전력별 컬럼을 index로 설정
df.set_index("발전 전력별",inplace=True)
df.info()
df.index
df
#전치행렬 : 행과열을 바꿈
df = df.T
df.info()
df




# 합계 컬럼을 총발전량 컬럼으로 변경하기
df = df.rename(columns={"합계":"총발전량"})
df.info()
#총발전량-1년 추가 :전년도 발전량
df.head()
#shift(1) : 총발전량의 앞의 인덱스 데이터
df["전년도발전량"] = df["총발전량"].shift(1)
df.head()
#증감율 컬럼 추가하기
# 증감율 :(현재-전년도)/전년도 * 100
#         (현재/전년도 - 1) * 100
df["증감율"]=((df["총발전량"]/df["전년도발전량"]) - 1) * 100
df.head()




###연합 그래프 작성
plt.style.available #사용 가능한 style 목록
plt.style.use("ggplot") #그래프 style 설정
plt.rc('font', family="Malgun Gothic") #한글폰트 설정
plt.rcParams['axes.unicode_minus']=False #음수표시 -설정
df[['수력','화력']] #원자력데이터 제외
#DataFrame.plot 함수 사용
#figsize : 그래프영역 크기.
#width=0.7 : 막대그래프 넓이
#stacked=False : 막대그래프를 수력, 화력 따로 표시
#ax1 : 막대그래프영역
#x축값:df.index
#y축값:df[[수력,화력]]. 막대그래프2개
ax1 = df[['수력','화력']].plot(kind='bar', figsize=(20, 10), \
                           width=0.7, stacked=False)  


#ax1 영역을 ax2와 같은 영역 설정.
#ax1,ax2 영역은 같은 영역    

ax2 = ax1.twinx()

#ax2:증감율 선그래프 작성
#df.index : 년도데이터를 x축값.
#df.증감율 : 증감율 컬럼을 y축값
#ls='--' : 선의 종료(--:댓쉬선,-:실선)
#marker='o' : 선의 마커 표시
#markersize=10 : 마커 크기 
#label='전년대비 증감율(%)' : 범례표시
ax2.plot(df.index, df.증감율, ls='--', marker='o', markersize=10, 
        color='green', label='전년대비 증감율(%)')
ax1.set_ylim(0, 200) #막대그래프 y축의 값의 범위
ax2.set_ylim(-50, 50)#선그래프  y축의 값의 범위  



ax1.set_xlabel('연도', size=20) #x축값의 설명
ax1.set_ylabel('발전량(억 KWh)') #막대그래프 y축값의 설명
ax2.set_ylabel('전년 대비 증감율(%)') #선그래프 y축값의 설명
plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30) #전체 그래프 제목
ax1.legend(loc='upper left') #범례: 왼쪽 위 위치
ax2.legend(loc='upper right') #범례: 오른쪽 위 위치

#그래프를 이미지파일로 저장.
#savefig(저장파일명,해상도,이미지크기설정)
plt.savefig("img/북한전력량.png", dpi=400, bbox_inches="tight")
plt.show() #화면에 표시.


#자동차 연비데이터의 mpg 값을 히스토그램으로 출력하기
df = sns.load_dataset("mpg")
df.info()
#DataFrame plot 히스토그램 출력
df["mpg"].plot(kind="hist")
#간격을 20개로 분리한 히스토그램 출력
#linewidth=1:막대사이간격
df["mpg"].plot(kind="hist",bins=20,color='coral',\
               figsize=(10,5),histtype='bar',linewidth=1)
plt.title("MPG 히스토그램")
plt.xlabel("mpg(연비)")


df["mpg"].min()  # 9.0
df["mpg"].max()  # 46.6


#weight,mpg 데이터의 산점도 출력하기
#DataFrame.plot(kind="scatter") : 그래프 종류
# x='mpg' : x축의 사용될 컬럼명
# y='weight' : y축의 사용될 컬럼명
# s=50 : 점의 크기지정
df.plot(kind='scatter', x='mpg', y='weight', c='coral',\
        s=50,figsize=(10, 5))


#matplot모듈을 이용하여 산점도 출력
plt.figure(figsize=(10,5)) #새로운 그래프창 
#scatter(x축데이터,y축데이터) : 그래프 종류 
#df["mpg"] : x축데이터
#df["weight"] : y축데이터
plt.scatter(df["mpg"],df["weight"],c="coral",s=20)


df[["mpg","weight"]].corr()   #correlation
df[["mpg","cylinders"]].corr()

#bubble그래프:산점도. 점의크기를 데이터의 값으로 결정
#3개의 컬럼 지정:x축:weight,y:mpg, 점의크기:cylinders
#cylinders의 데이터의 값의 종류와 갯수 조회
df["cylinders"].unique()
df["cylinders"].value_counts()
#cylinders 값을 최대값의 비율로 계산하여 데이터 생성
cylinders_size = (df["cylinders"]/df["cylinders"].max() * 100)   
cylinders_size.value_counts()
#alpha=0.7 : 점의 색을 반투명(70%)
df.plot(kind='scatter', x='weight', y='mpg', c='coral',\
        s=cylinders_size,figsize=(10, 5),alpha=0.7)

    
# 색상으로 데이터 값을 설정.
# marker="+" : 산점도 점의 모양
#cmap='magma' : matplot 모듈에서 숫자에 해당하는 색의 목록
#       viridis,inferno,magma,cividis,...
#c=df["cylinders"] : cylinders의 값에 해당하는 색을 cmap에서 선택 
df.plot(kind="scatter",x="weight",y="mpg",marker="+", figsize=(10,5),\
         cmap='magma',c=df["cylinders"],s=50,alpha=0.7)   
plt.title("산점도:mpg-weight-cylinders")
#transparent=True:투명그림으로 저장 
plt.savefig("img/scatter_transparent2.png",transparent=True)


#파이그래프
#origin 컬럼 : 제조국.[usa,japan, europe]

df_origin = df.origin.value_counts()
df_origin
type(df_origin)
df_origin.plot(kind="pie") #파이그래프 
plt.title("자동차 생산국",size=20)
plt.legend(labels=df_origin.index,loc="upper left")    

'''
autopct="%.1f%%" : 파이그래프에 비율 표시
      %.1f : 소숫점이하1자리로표시
      %%   : % 문자

startangle=90 : 기본설정 위치에서 90도로 시작위치 변경
      
'''
df_origin.plot(kind="pie",figsize=(7,5),autopct="%.1f%%",startangle=90,
               colors=['chocolate','bisque','cadetblue']) #파이그래프 
plt.title("자동차 생산국",size=20)
plt.legend(labels=df_origin.index,loc="upper left")    


'''
  labels=['USA','JAPAN','EU'] : x축의 값. 3개의 그룹명
  vert=False : 가로형태의 박스그래프.
  sym 속성  : "r*"  : 이상치 표현기호 및 색상
            r:red. b:blue .....
            *:별, s:정사각형, +:십자가, .:작은점
            o:큰점(기본값), d:다이아몬드            
'''
# 박스그래프: 두개의 그래프 출력하기
fig = plt.figure(figsize=(15,5)) #그래프출력영역,크기지정.
#그래프 출력영역을 분리
ax1 = fig.add_subplot(1,2,1) #1행2열 첫번째 그래프
ax2 = fig.add_subplot(1,2,2) #1행2열 두번째 그래프

box1 = ax1.boxplot(x=[df[df['origin']=='usa']['mpg'],
              df[df['origin']=='japan']['mpg'],
              df[df['origin']=='europe']['mpg']],
              labels=['USA','JAPAN','EU'],sym="ro")
box2 = ax2.boxplot(x=[df[df['origin']=='usa']['mpg'],
              df[df['origin']=='japan']['mpg'],
              df[df['origin']=='europe']['mpg']],
              labels=['USA','JAPAN','EU'],vert=False)
ax1.set_title("제조국자별 연비분포(수직박스플롯)")
ax2.set_title("제조국자별 연비분포(수평박스플롯)")

usadf = df[df['origin']=='usa'][['mpg']]
usadf.describe()

'''
              mpg
count  249.000000
mean    20.083534
std      6.402892
min      9.000000
25%     15.000000
50%     18.500000
75%     24.000000
max     39.000000
'''
   

#df데이터를 origin 컬럼으로 그룹화하여 그룹별 합계 출력하기
df.groupby("origin").sum()
#df데이터를 origin 컬럼으로 그룹화하여 그룹별 건수 출력하기
df.groupby("origin").count()
df.origin.value_counts()
#df데이터를 origin 컬럼으로 그룹화하여 그룹별 평균 출력하기
df.groupby("origin").mean()
#df데이터를 origin 컬럼으로 그룹화하여 그룹별 중간값 출력하기
df.groupby("origin").median()










