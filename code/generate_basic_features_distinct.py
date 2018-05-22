import pandas as pd
from pandas import DataFrame
from math import sqrt
from config import isCase
from feat_utils import get_count_of_sen

from config import path
path = './feature/'


def prepare_ngram_interaction(path,out,ngram='unigram'):
    data_in = pd.read_csv(path)
    data_out = DataFrame(columns=['count_of_sen1_'+ngram,'count_of_sen2_'+ngram])
    for index,row in data_in.iterrows():
        s1_ngram = str(row['sen1_distinct_%s'%ngram]).split()
        s2_ngram = str(row['sen2_distinct_%s'%ngram]).split()

        count_of_sen1 = get_count_of_sen(s1_ngram)
        count_of_sen2 = get_count_of_sen(s2_ngram)
        data_out.loc[index] = [count_of_sen1,count_of_sen2]
    data_out.to_csv(out)

if isCase == False:
    prepare_ngram_interaction(path+'train_distinct_unigram.csv',path+'train_distinct_unigram_features.csv',ngram='unigram')
    prepare_ngram_interaction(path+'test_distinct_unigram.csv',path+'test_distinct_unigram_features.csv',ngram='unigram')
    prepare_ngram_interaction(path+'train_distinct_bigram.csv',path+'train_distinct_bigram_features.csv',ngram='bigram')
    prepare_ngram_interaction(path+'test_distinct_bigram.csv',path+'test_distinct_bigram_features.csv',ngram='bigram')
else:
    prepare_ngram_interaction(path+'case_distinct_unigram.csv',path+'case_distinct_unigram_features.csv',ngram='unigram')
    prepare_ngram_interaction(path+'case_distinct_bigram.csv',path+'case_distinct_bigram_features.csv',ngram='bigram')

