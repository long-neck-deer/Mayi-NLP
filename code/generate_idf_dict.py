#############################################################################################################
# Created by qqgeogor
# https://www.kaggle.com/qqgeogor
#############################################################################################################
import pandas as pd
from pandas import DataFrame
from config import isCase
from math import exp, log, sqrt
import pickle
path = './data/'



def get_idf(df,n,smooth=1):
    idf = log((smooth + n) / (smooth + df))
    return idf



def create_idf_dict(path,smooth=1.0,inverse=False):
    K_dict = {}
    c = 0
    data_input = pd.read_csv(path)
    for index,row in data_input.iterrows():
        s1 = str(row['sen1'])
        s2 = str(row['sen2'])
        for sentence in [s1,s2]:
            for key in sentence.split(" "):
                df = K_dict.get(key,0)
                K_dict[key] = df+1
        c += 1
    n = c*2
    for key in K_dict:
        K_dict[key] = get_idf(K_dict[key] ,n,smooth=1)
    K_dict["default_idf"] = get_idf(0 ,n,smooth=10)
    return K_dict


if isCase == False:
    idf_dict = create_idf_dict(path+"train_clean.csv",inverse=False)
    pickle.dump(idf_dict,open('./feature/idf_dict.pkl','wb'))
else:
    idf_dict = create_idf_dict(path+"case.csv",inverse=False)
    pickle.dump(idf_dict,open('./feature/idf_dict.pkl','wb'))



