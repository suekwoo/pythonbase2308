# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:39:27 2023

@author: KITCOOP
"""
import pandas as pd
#범주형 : 값의 범위 가지고 있는 자료형.
#         값의 크기와 상관없는 단수한 범위를 의미. 통계데이터 필요없음
age = pd.Series([26,42, 27, 25, 20,  20, 21, 22, 23, 25]) 
stu_class = pd.Categorical([1,1,2,2,2,3,3,4,4,4]) #정수형 범주 데이터
gender=pd.Categorical(['F','M','M','M','M','F','F','F','M','M'])
c_df = pd.DataFrame({'age':age,'class':stu_class,'gender':gender})
c_df.info()
c_df.describe()
c_df
#class 컬럼을  범주형 => 정수형
c_df["class"] = c_df["class"].astype("int")
c_df.info()
c_df.describe()