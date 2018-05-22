import pandas as pd
from pandas import DataFrame
from config import isCase
from feat_utils import get_count_s1_in_s2
from feat_utils import get_ratio_s1_in_s2

path = './data/'

'''
please add new stop word in list stops[]
'''

stops = ['了','啊']


def prepare_ngram_interaction(path,out):

    data_input = pd.read_csv(path)
    data_ouput = DataFrame(columns=['count_of_stop_sen1','ratio_of stop_sen1','count_of_stop_sen2','ratio_of_stop_sen2'])
    for index,row in data_input.iterrows():
        s1_ngram = str(row['sen1']).split()
        s2_ngram = str(row['sen2']).split()
        count_of_stop_sen1 = get_count_s1_in_s2(s1_ngram,stops)
        ratio_of_stop_sen1 = get_ratio_s1_in_s2(s1_ngram,stops)

        count_of_stop_sen2 = get_count_s1_in_s2(s2_ngram,stops)
        ratio_of_stop_sen2 = get_ratio_s1_in_s2(s2_ngram,stops)
        data_ouput.loc[index] = [count_of_stop_sen1,ratio_of_stop_sen1,count_of_stop_sen2,ratio_of_stop_sen2]
    data_ouput.to_csv(out)

if isCase == False:
    prepare_ngram_interaction(path+'train_clean.csv','./feature/train_clean_stop_features.csv')
    prepare_ngram_interaction(path+'test_clean.csv','./feature/test_clean_stop_features.csv')
else:
    prepare_ngram_interaction(path+'case.csv','./feature/case_clean_stop_features.csv')

