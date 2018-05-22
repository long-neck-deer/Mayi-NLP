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
path_out = './feature/'


print "Generate sen idf stats features"
idf_dict = pickle.load(open('./feature/idf_dict.pkl','rb'))

def mean(x):
    return sum(x)/float(len(x))

def median(x):
    len_2 = int(len(x)/2)
    return x[len_2]

def std(x):
    mean_x = mean(x)
    s = 0.0
    for xx in x:
        s+=(xx-mean_x)**2
    s/=len(x)
    s = sqrt(s)
    return s


def create_idf_stats_features(path,idf_dict,out):
    data_in = pd.read_csv(path)
    data_out = DataFrame(columns=[
        'min_s1_idfs',
        'max_s1_idfs',
        'mean_s1_idfs',
        'median_s1_idfs',
        'std_s1_idfs',
        'min_s2_idfs',
        'max_s2_idfs',
        'mean_s2_idfs',
        'median_s2_idfs',
        'std_s2_idfs'
    ])
    for index,row in data_in.iterrows():
        s1 = str(row['sen1'])
        s2 = str(row['sen2'])
        s1_idfs = [idf_dict.get(key,idf_dict['default_idf']) for key in s1.split(" ")]
        s2_idfs = [idf_dict.get(key,idf_dict['default_idf']) for key in s2.split(" ")]

        min_s1_idfs = min(s1_idfs)
        max_s1_idfs = max(s1_idfs)
        mean_s1_idfs = mean(s1_idfs)
        median_s1_idfs = median(s1_idfs)
        std_s1_idfs = std(s1_idfs)

        min_s2_idfs = min(s2_idfs)
        max_s2_idfs = max(s2_idfs)
        mean_s2_idfs = mean(s2_idfs)
        median_s2_idfs = median(s2_idfs)
        std_s2_idfs = std(s2_idfs)
        data_out.loc[index] = [
            min_s1_idfs,
            max_s1_idfs,
            mean_s1_idfs,
            median_s1_idfs,
            std_s1_idfs,
            min_s2_idfs,
            max_s2_idfs,
            mean_s2_idfs,
            median_s2_idfs,
            std_s2_idfs
        ]
    data_out.to_csv(out)  
if isCase == False:
    create_idf_stats_features(path+'train.csv',idf_dict,path_out+'train_idf_stats_features.csv')
    create_idf_stats_features(path+'test.csv',idf_dict,path_out+'test_idf_stats_features.csv')
else:
    create_idf_stats_features(path+'case.csv',idf_dict,path_out+'case_idf_stats_features.csv')

