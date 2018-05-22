import pandas as pd
from pandas import DataFrame
from config import isCase

from math import exp, log, sqrt


path = './feature/'


def prepare_idf_dict(paths,smooth=1.0):
    c = 0
    idf_dict = dict()
    for path in paths:
        data = pd.read_csv(path)
        for index,row in data.iterrows():
            s1 = str(row['sen1_hash'])
            s2 = str(row['sen2_hash'])
        for key in [s1,s2]:
            df = idf_dict.get(key,0)
            df+=1
            idf_dict[key] = df
        c += 1
    n = c*2
    for key in idf_dict:
        idf_dict[key] = get_idf(idf_dict[key] ,n,smooth=1)
    idf_dict["default_idf"] = get_idf(0 ,n,smooth=1)

    return idf_dict

def get_idf(df,n,smooth=1):
    idf = log((smooth + n) / (smooth + df))
    return idf

def prepare_hash_idf(path,out,idf_dict):
    data_in = pd.read_csv(path)
    data_out = DataFrame(columns=['sen1_hash_count','sen2_hash_count'])
    for index,row in data_in.iterrows():
        s1 = str(row['sen1_hash'])
        s2 = str(row['sen2_hash'])
        s1_idf = idf_dict.get(s1,idf_dict['default_idf'])
        s2_idf = idf_dict.get(s2,idf_dict['default_idf'])
        data_out.loc[index] = [s1_idf,s2_idf]
    data_out.to_csv(out)



if isCase == False:
    idf_dict = prepare_idf_dict([path+'train_hashed.csv',path+'test_hashed.csv'])
    prepare_hash_idf(path+'train_hashed.csv',path+'train_hashed_idf.csv',idf_dict)
    prepare_hash_idf(path+'test_hashed.csv',path+'test_hashed_idf.csv',idf_dict)
else:
    idf_dict = prepare_idf_dict([path+'case_hashed.csv',path+'case_hashed.csv'])
    prepare_hash_idf(path+'case_hashed.csv',path+'case_hashed_idf.csv',idf_dict)

