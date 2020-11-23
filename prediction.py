# -*- coding: utf-8 -*-

#importing libraries
import cv2
import numpy as np
import traceback
import pickle
import keras
import time

def test(image):
    try:
        Xtest=[]

        model_name = 'KYC_Vgg_transfer_learning.h5'
        model2 = keras.models.load_model(model_name)#loading the saved model
        
        
        pred=(cv2.imread(image,cv2.IMREAD_GRAYSCALE))
        pred=cv2.resize(pred,(224,224))#resizing the input image
        pred=cv2.cvtColor(pred, cv2.COLOR_BGR2RGB)
        Xtest.append(pred)
        Xtest=np.array(Xtest)
        
        start = time.time()
        preds=model2.predict(Xtest, verbose=1)
        end = time.time()
        
        res=np.argmax(preds)
        
        #loading the LabelEncoder() obj 
        pkl_file = open('encoder.pkl', 'rb')
        le_depart = pickle.load(pkl_file) 
        pkl_file.close()
        
        result = le_depart.inverse_transform([res])[0]
        
        #print(f"Runtime for testing is {end - start}")
        return res,result
    except:
        print(traceback.print_exc())

#image='/home/kirankumar/Desktop/samples_53-20201119T165726Z-001/samples_53/dl/001 (1).jpg'
#print(test(image))
