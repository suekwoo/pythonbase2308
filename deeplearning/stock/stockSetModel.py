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
2) pip install tensorflow
   Successfully installed 
   astunparse-1.6.3 
   cachetools-5.3.1 
   gast-0.4.0 
   google-auth-2.22.0 
   google-auth-oauthlib-1.0.0 
   google-pasta-0.2.0 
   grpcio-1.57.0 keras-2.13.1 
   libclang-16.0.6 oauthlib-3.2.2 
   opt-einsum-3.3.0 requests-oauthlib-1.3.1 
   rsa-4.9 tensorboard-2.13.0 
   tensorboard-data-server-0.7.1 
   tensorflow-2.13.0 tensorflow-estimator-2.13.0 
   tensorflow-intel-2.13.0 
   tensorflow-io-gcs-filesystem-0.31.0 termcolor-2.3.0





'''

import FinanceDataReader as fdr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from stockmodule  import MinMaxScaler
fdr.__version__



















