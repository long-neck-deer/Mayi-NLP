from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt
from random import random,shuffle
import pickle
import sys
from feat_utils import get_jaccard
from feat_utils import get_dice
from feat_utils import get_count_s1_in_s2
from feat_utils import get_ratio_s1_in_s2
from feat_utils import get_count_of_sen
from feat_utils import get_count_of_unique_sen
from feat_utils import get_ratio_of_unique_sen
from feat_utils import get_count_of_digit
from feat_utils import get_ratio_of_digit
from config import isCase
path = './feature/'


def prepare_ngram_interaction(path,out,ngram='distinct_unigram'):
    print path
    c = 0
    start = datetime.now()
    with open(out, 'w') as outfile:
        outfile.write('sen_%s_min,sen_%s_max\n'% (ngram,ngram))
        for row in DictReader(open(path), delimiter=','): 
            if c%100000==0:
                print 'finished',c
            s1_ngram = str(row['sen1_%s'%ngram]).split()
            s2_ngram = str(row['sen2_%s'%ngram]).split()

            count_of_sen1 = get_count_of_sen(s1_ngram)
            count_of_sen2 = get_count_of_sen(s2_ngram)
            count_of_sen_min = min(count_of_sen1,count_of_sen2)
            count_of_sen_max = max(count_of_sen1,count_of_sen2)
            

            outfile.write('%s,%s\n' % (
                count_of_sen_min,
                count_of_sen_max,
                ))
            c+=1
        end = datetime.now()
    print 'times:',end-start

if isCase == False:
    prepare_ngram_interaction(path+'train_distinct_unigram.csv',path+'train_distinct_unigram_minmax_features.csv',ngram='distinct_unigram')
    prepare_ngram_interaction(path+'test_distinct_unigram.csv',path+'test_distinct_unigram_minmax_features.csv',ngram='distinct_unigram')

    prepare_ngram_interaction(path+'train_distinct_bigram.csv',path+'train_distinct_bigram_minmax_features.csv',ngram='distinct_bigram')
    prepare_ngram_interaction(path+'test_distinct_bigram.csv',path+'test_distinct_bigram_minmax_features.csv',ngram='distinct_bigram')
else:
    prepare_ngram_interaction(path+'case_distinct_uigram.csv',path+'case_distinct_uigram_minmax_features.csv',ngram='distinct_uigram')
    prepare_ngram_interaction(path+'case_distinct_bigram.csv',path+'case_distinct_bigram_minmax_features.csv',ngram='distinct_bigram')
