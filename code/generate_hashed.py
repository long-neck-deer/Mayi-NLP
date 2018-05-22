import pandas as pd
from pandas import DataFrame
from config import isCase


path = "./data/"
path_to = "./feature/"


def prepare_hash(path,out):
    data_input = pd.read_csv(path)
    data_ouput = DataFrame(columns=['sen1_hash','sen2_hash'])
    for index,row in data_input.iterrows():
        s1 = str(row['sen1'])
        s2 = str(row['sen2'])
        hash1 = hash(s1)
        hash2 = hash(s2)
        data_ouput.loc[index] = [hash1,hash2]
    data_ouput.to_csv(out,index=False)
 
if isCase == False:
    prepare_hash(path+'train_clean.csv',path_to+'train_hashed.csv')
    prepare_hash(path+'test_clean.csv',path_to+'test_hashed.csv')
else:
    prepare_hash(path+'case.csv',path_to+'case_hashed.csv')

