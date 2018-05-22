import pandas as pd
from pandas import DataFrame
from ngram import getUnigram
from config import isCase


path = './data/'
path_feature = './feature/'

def prepare_unigram(path,out):
    data_input = pd.read_csv(path)
    data_ouput = DataFrame(columns=['sen1_unigram','sen2_unigram'])
    for index,row in data_input.iterrows():
        s1 = str(row['sen1']).split()
        s2 = str(row['sen2']).split()
        s1 = ' '.join(getUnigram(s1))
        s2 = ' '.join(getUnigram(s2))
        data_ouput.loc[index] = [s1,s2]
    data_ouput.to_csv(out)

if isCase == False:
    prepare_unigram(path+'train_clean.csv',path_feature+'train_unigram.csv')
    prepare_unigram(path+'test_clean.csv',path_feature+'test_unigram.csv')
else:
    prepare_unigram(path+'case.csv','./feature/case_unigram.csv')
