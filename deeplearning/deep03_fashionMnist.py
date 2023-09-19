# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:26:51 2023

@author: KITCOOP
"""

from tensorflow.keras.datasets.fashion_mnist  import load_data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from PIL import Image
from keras.models import load_model
from sklearn.metrics import \
    classification_report,confusion_matrix

#1.수집 2.전처리 
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape,x_test.shape) #(60000, 28, 28) (10000, 28, 28)
class_names=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
         'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
y_train[:10] #[9, 0, 0, 3, 0, 2, 7, 2, 5, 5]
x_train[0]

#2-1이미지 데이터 정규화
x_trainS = x_train/255 #minmax 정규화 (x-min)/(max-min)
x_testS = x_test/255
#레이블을 onehot인코딩하기
y_trainS = to_categorical(y_train)
y_testS = to_categorical(y_test)

#검증데이터 생성 : 학습 중간에 평가를 위한 데이터  
#검증데이터 분리. (훈련:검증)=(7:3)
x_trainS,x_valS, y_trainS,y_valS = \
  train_test_split(x_trainS,y_trainS,test_size=0.3,random_state=777)
x_trainS.shape
x_valS.shape

#3 model setting

#model1 모델 구성하기
model1 = Sequential()  #모델 생성
model1.add(Flatten(input_shape = (28, 28)))
model1.add(Dense(64,activation="relu"))
model1.add(Dense(32,activation="relu"))
model1.add(Dense(10,activation="softmax")) #0 ~ 9 10개
model1.summary()
model1.compile(optimizer="adam", loss='categorical_crossentropy',
              metrics=['acc'])

#학습하기   0.8658
history=model1.fit(x_trainS,y_trainS,epochs=10,batch_size=127,
                  validation_data=(x_valS,y_valS)) 



#model2 모델 구성하기
model2 = Sequential()  #모델 생성
model2.add(Flatten(input_shape = (28, 28)))
model2.add(Dense(256,activation="relu"))
model2.add(Dense(128,activation="relu"))
model2.add(Dense(64,activation="relu"))
model2.add(Dense(32,activation="relu"))
model2.add(Dense(10,activation="softmax")) #0 ~ 9 10개
model2.summary()
model2.compile(optimizer="adam", loss='categorical_crossentropy',
              metrics=['acc'])

#학습하기   0.8824
history=model2.fit(x_trainS,y_trainS,epochs=10,batch_size=127,
                  validation_data=(x_valS,y_valS)) 


model1.evaluate(x_testS,y_testS)  
#[0.39575517177581787, 0.858299970626831]
model2.evaluate(x_testS,y_testS)  
#[0.3700970411300659, 0.8726000189781189]























