# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:23:03 2023

@author: KITCOOP
"""

"""
Created on Wed Mar 22 13:41:17 2023

@author: KITCOOP
"""
'''
1) pip install -U finance-datareader (anaconda prompt))
종목 코드 거래소별 전체 종목코드: 
    KRX (KOSPI, KODAQ, KONEX), 
    NASDAQ, NYSE, AMEX, S&P 500 
    가격 데이터 해외주식 가격 데이터:
  
        
AAPL(애플), AMZN(아마존), GOOG(구글) 
005930(삼성전자), 091990(셀트리온헬스케어) 
KS11(코스피지수), KQ11(코스닥지수), DJI(다우지수), 
IXIC(나스닥 지수), US500(S&P 5000) 
환율 데이터: USD/KRX (원달러 환율), 
USD/EUR(달러당 유로화 환율), 
CNY/KRW: 위엔화 원화 환율 
암호화폐 가격: BTC/USD (비트코인 달러 가격, Bitfinex), 
BTC/KRW (비트코인 원화 가격, 빗썸)

2023-08 

주가 분석 project
1) pip install -U finance-datareader   : ok
    Successfully installed finance-datareader-0.9.50
'''

import FinanceDataReader as fdr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from stockmodule  import MinMaxScaler
fdr.__version__

# 1. 데이터 수집
# 거래소 상장종목 
df_nas = fdr.StockListing('NASDAQ')
df_nas.head()
len(df_nas)

df_krx = fdr.StockListing('KOSPI')
df_krx.head()
len(df_krx)
# df = fdr.DataReader('종목코드', '시작일', '종료일')
# df = fdr.DataReader('종목코드', '시작일')  이후 전체
# df = fdr.DataReader('005930', '2022')  #년도별 자료 수집 가능

start='2022-01-01'
end='2023-07-31'

df = fdr.DataReader('005930', start, end)  #삼성

df.info()
df.head()
df.shape   #(390, 6)

'''
10일간의 데이터를 가지고 종가를 예측한다는 것은 이런 의미입니다.
6월 1일 ~ 6월 10일까지의 OHLV 데이터로 
6월 11일 종가 예측 
6월 2일 ~ 6월 11일까지의 OHLV 데이터로 
6월 12일 종가 예측
'''



