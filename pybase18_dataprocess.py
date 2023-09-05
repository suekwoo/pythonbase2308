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


















