# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:35:51 2023

@author: KITCOOP
"""

#파일 읽기
import pandas as pd
chipo = pd.read_csv("data/chipotle.tsv",sep="\t")
chipo.info()
'''
데이터 속성 설명
order_id : 주문번호
quantity : 아이템의 주문수량
item_name : 주문한 아이템의 이름
choice_description : 주문한 아이템의 상세 선택 옵션
item_price : 주문 아이템의 가격 정보
'''

#chipo 데이터의 행열의 갯수 출력하기
chipo.shape
#컬럼명
chipo.columns
#인덱스명
chipo.index
# order_id 주문번호이므로, 숫자형 분석의 의미가 없다.
# order_id  컬럼의 자료형을 문자열로 변경하기
chipo["order_id"] = chipo["order_id"].astype(str)
chipo.info()
#판매상품명과 상품의 갯수 출력하기
chipo["item_name"].unique()
len(chipo["item_name"].unique())
#item_price 컬럼을 실수형 변경



chipo["item_price"] = \
chipo["item_price"].str.replace("$","").astype(float)
chipo.info()
#ex01)주문금액 합계
hap=chipo["item_price"].sum()
hap

#ex02) 주문건수
len(chipo["order_id"].unique())
cnt=len(chipo.groupby("order_id"))
cnt

#ex03) 주문당평균금액
hap/cnt
chipo.groupby("order_id")["item_price"].sum().mean()


#ex04) 50달러 이상 주문한 주문번호
chipo.groupby("order_id")["item_price"].sum()
order_id_tot = chipo.groupby("order_id").sum()
order_id_tot
result = order_id_tot[order_id_tot["item_price"]>=50]
result
len(result)
list(result.index)


#ex05) 50달러 이상 주문한 주문정보
chipo_50 = chipo[chipo["order_id"].isin(result.index)]
chipo_50.info()

chipo_51 = chipo.groupby("order_id")\
        .filter(lambda x : sum(x["item_price"]) >=50 )

chipo_51.info()

#ex06) item_name 별 단가를 조회하기
price_one = chipo.groupby("item_name")["item_price"]
price_one
type(price_one)  #pandas.core.groupby.generic.SeriesGroupBy
len(price_one)   

for key, item in price_one :
    print (key, "=", len(item))
    print(item)
    
price_min = chipo.groupby("item_name").min()["item_price"]
price_min

#ex07) 단가의 분포를 히스토그램으로 출력하기
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")
plt.hist(price_min)
plt.ylabel("상품갯수")
plt.title("상품단가 분포")

price_min.plot(kind = "hist")
plt.ylabel("상품갯수")
plt.title("상품단가 분포")


#ex08) 주문당 금액이 가장 높은 5건의 주문 총수량을 조회하기
price5 = chipo.groupby("order_id").sum()\
              .sort_values(by="item_price", ascending=False)[:5]
price5        
price5.index

#ex09) 주문당 금액이 가장 높은 5건의 주문 정보 조회하기
chipo_5 = chipo[chipo["order_id"].isin(price5.index)]\
            [["order_id", "item_name", "quantity", "item_price"]]
chipo_5

#ex10) Chicken Bowl 몇번 주문되었는지 출력하기
chipo_chicken = chipo[chipo["item_name"]=='Chicken Bowl']
len(chipo_chicken)  #726
len(chipo_chicken.groupby("order_id"))  #615

chipo_chicken = chipo_chicken.drop_duplicates(['item_name', 'order_id'])
len(chipo_chicken)  #615

###################
#  전세계 음주 데이터 분석하기 : drinks.csv
import pandas as pd
drinks = pd.read_csv("data/drinks.csv")
drinks.info()
'''
  country : 국가명
  beer_servings : 맥주소비량
  spirit_servings : 음료소비량
  wine_servings : 와인소비량   
  total_litres_of_pure_alcohol : 순수 알콜량
  continent : 대륙명
'''
drinks.head()

# 변수 = 컬럼 = 피처
# 상관계수 : 두연속적인 데이터의 상관관계 수치
# 피어슨 상관계수 : 기본. 
beer_wine_corr=\
    drinks[["beer_servings","wine_servings"]].corr()
beer_wine_corr
beer_wine_corr=drinks[["beer_servings","wine_servings"]]\
    .corr(method="pearson")
beer_wine_corr
# 켄달 상관계수 : 샘플 사이즈가 작은 경우.
#               동률데이터의 확율이 높은 경우
beer_wine_corr=drinks[["beer_servings","wine_servings"]]\
    .corr(method="kendall")
beer_wine_corr
# 스피어만 상관계수 : 정규화가 되지 않는 데이터에 많이 사용
beer_wine_corr=drinks[["beer_servings","wine_servings"]]\
    .corr(method="spearman")
beer_wine_corr

drinks.columns
cols = drinks.columns[1:-1]
cols
corr = drinks[cols].corr()
corr
corr.values
#상관계수 시각화하기
#히트맵을 이용하여 시각화 하기
import seaborn as sns
cols_view = ["beer","spirit","wine","alcohol"]
sns.set(font_scale=1.5) #글자크기.
hm=sns.heatmap(corr.values,  #데이터
                cbar=True,   #색상맵
                annot=True,  #데이터값표시
                square=True, #히트맵을 사각형으로 출력
                yticklabels=cols_view, #y축 표시 라벨
                xticklabels=cols_view) #x축 표시 라벨

#seaborn 모듈의 산점도을 이용하여 시각화 하기
sns.pairplot(drinks[cols])
plt.show()

#회귀그래프 작성하기
sns.regplot\
 (x="beer_servings",y="total_litres_of_pure_alcohol",
  data=drinks)
 
#각 변수의 결측값 갯수 조회하기
drinks.info()
drinks.isnull().sum() 
#대륙별 국가수 조회하기
drinks["continent"].value_counts()  #각 value별 합계
drinks["continent"].value_counts(dropna=False)  #null 포함
drinks.groupby("continent").count()["country"]
#continent 컬럼의 결측값을 OT로 변경하기
#fillna : 결측값을 다른 값으로 치환함수
drinks["continent"]=drinks["continent"].fillna("OT")
drinks.info()

import matplotlib.pyplot  as plt

# 대륙별 국가의 갯수를 파이그래프로 출력하기
sns.set(font_scale=1)
#tolist() : 리스트로 형변환
labels = drinks['continent'].value_counts().index.tolist()
labels
#'AF', 'EU', 'AS', 'OT', 'OC', 'SA'
explode = (0, 0, 0, 0.1, 0, 0) 
plt.pie(drinks['continent'].value_counts(), #데이터값
    labels=labels,                     #라벨명. 대륙명
    autopct='%.0f%%',  #비율표시. %.0f : 소숫점이하 없음. %%:%문자
    explode=explode,  #파이의 위치지정. 0.1 : 1/10만큼 밖으로 표시
    shadow=True)
plt.title('null data to \'OT\'')

# 1 대륙별 total_litres_of_pure_alcohol 섭취량 평균

cont_mean = drinks.groupby("continent")["total_litres_of_pure_alcohol"].mean()
cont_mean
total_mean = drinks["total_litres_of_pure_alcohol"].mean()
total_mean

drinks.info()
import numpy as np
plt.rc("font",family="Malgun Gothic")

# 2 대륙명 : x축의 라벨
continents=cont_mean.index.tolist()
continents
continents.append("Mean")
x_pos = np.arange(len(continents))

#y축 데이터 : 대륙별 평균값
alcohol = cont_mean.tolist()
alcohol
alcohol.append(total_mean)


#그래프화
#plt.bar : 막대그래프
#bar_list : 막대그래프의 막대 목록
bar_list =plt.bar(x_pos, alcohol, align='center',alpha=0.5)
bar_list
#bar_list[len(continents) - 1] : bar_list[6] 막대
#set_color('r') : 색상 설정. r:red 
bar_list[len(continents) - 1].set_color('r') #7번째 막대색 red로 설정

plt.xticks(x_pos, continents)
plt.ylabel('total_litres_of_pure_alcohol') #y축설명
plt.title('대륙별 평균알콜 섭취랑') #제목
plt.show()

'''
대륙별 beer_servings의 평균를 막대그래프로 시각화
가장 많은 맥주를 소비하는 대륙(EU)의 막대의 색상을 빨강색("r")으로 변경하기 
전체 맥주 소비량 평균을 구해서 막대그래프에 추가
평균선을 출력하기. 평균 막대 색상은 노랑색 ("y")
평균선은 검정색("k--")
'''
# 1 대륙별 맥주 소비량 평균

bear_mean = drinks.groupby("continent").beer_servings.mean()
bear_mean
total_beer = drinks.beer_servings.mean()
total_beer

# 2 대륙명 : x축의 라벨
continents=bear_mean.index.tolist()
continents
continents.append("Mean")
x_pos = np.arange(len(continents))

#y축 데이터 : 대륙별 평균값
alcohol = bear_mean.tolist()
alcohol
alcohol.append(total_beer)


#그래프화
#plt.bar : 막대그래프
#bar_list : 막대그래프의 막대 목록
bar_list =plt.bar(x_pos, alcohol, align='center',alpha=0.5)
bar_list
#bar_list[len(continents) - 1] : bar_list[6] 막대
#set_color('r') : 색상 설정. r:red 
bar_list[len(continents) - 1].set_color('y') #6번 막대색 red로 설정
bar_list[2].set_color('r') #2번 막대색 red로 설정
plt.plot([0,6], [total_beer, total_beer], 'k--')
plt.xticks(x_pos, continents)
plt.ylabel('맥주 소비량') #y축설명
plt.title('대륙별 맥주 섭취랑') #제목
plt.show()

#대한민국은 얼마나 술을 독하게 마시는 나라인가?
#total_servings : 전체 주류 소비량 컬럼 추가
drinks["total_servings"] =\
    drinks["beer_servings"] + \
    drinks["spirit_servings"] +\
    drinks["wine_servings"]

#alcohol_rate : 알콜비율 (알콜섭취량/전체주류소비량) 추가
drinks["alcohol_rate"] = \
    drinks["total_litres_of_pure_alcohol"]/drinks["total_servings"]

drinks.info()
#alcohol_rate 컬럼에 결측값 존재.
#전체주류소비량이 0인 경우 불능 => 결측값
#alcohol_rate 컬럼의 값이 결측값인 레코드 조회하기

#1. alcohol_rate null인 index 구하기
drinks["alcohol_rate"].isnull()
alcoholnull = drinks[drinks["alcohol_rate"].isnull()]
alcoholnull
#2. alcohol_rate 컬럼의 결측값을 0을 치환하기
drinks["alcohol_rate"]=drinks["alcohol_rate"].fillna(0)
drinks.info()


#alcohol_rate의 값으로 내림차순 정렬하기. alcohol_rate_rank 저장
alcohol_rate_rank=drinks.sort_values(by="alcohol_rate", ascending=False)\
                [["country","alcohol_rate"]]

alcohol_rate_rank


alcohol_rate_rank.head()
alcohol_rate_rank.shape

alcohol_rate_rank.country.tolist().index("South Korea")
alcohol_rate_rank.head(15)

#국가명목록
country_list = alcohol_rate_rank.country.tolist()


#1. x축값
x_pos = np.arange(len(country_list))

#2. y축값
rank=alcohol_rate_rank.alcohol_rate.tolist()

#막대그래프 
# bar_list : 막대 목록
bar_list = plt.bar(x_pos, rank)

#대한민국 막대의 색을 red로 변경
korea_rank = country_list.index("South Korea")
bar_list[korea_rank].set_color('r')
plt.ylabel('alcohol rate')
plt.title('liquor drink rank by contry')
plt.axis([0, 200, 0, 0.3]) #xy축범위:[x축값의시작,x축값의종료,y축값의시작,y축값의종료]

#korea_serving_rate : 대한민국 전체 술소비량 데이터. y축값

korea_alcohol_rate = alcohol_rate_rank[ alcohol_rate_rank['country']=='South Korea']\
    ['alcohol_rate'].values[0]
korea_alcohol_rate     #0.0593939393939394


plt.annotate('South Korea : ' + str(korea_rank + 1)+"번째", 
          xy=(korea_rank, korea_alcohol_rate), 
          xytext=(korea_rank + 10, korea_alcohol_rate+0.1 ),
          arrowprops=dict(facecolor='red', shrink=0.05))
plt.show()

#--------------------------------------------------

import pandas as pd
import numpy as np
#서울 구별 CCTV 정보 데이터 읽기
CCTV_Seoul = pd.read_csv("data/01. CCTV_in_Seoul.csv")
CCTV_Seoul.info()



#서울 경찰서별 범죄율 정보 데이터 읽기
crime_Seoul = pd.read_csv('data/02. crime_in_Seoul.csv',
                          thousands=',', encoding='cp949')


crime_Seoul.info()

#전국 경찰서 위치 데이터 읽기
police_state = pd.read_csv('data/경찰관서 위치.csv', encoding='cp949')
police_state.info()








