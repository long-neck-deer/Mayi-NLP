import pandas as pd
from pandas import DataFrame
from math import sqrt
from config import isCase
from feat_utils import get_jaccard
from feat_utils import get_dice
from feat_utils import get_count_s1_in_s2
from feat_utils import get_ratio_s1_in_s2
from feat_utils import get_count_of_sen
from feat_utils import get_count_of_unique_sen
from feat_utils import get_ratio_of_unique_sen
from feat_utils import get_count_of_digit
from feat_utils import get_ratio_of_digit
path = './feature/'

# stops = set(["http","www","img","border","home","body","a","about","above","after","again","against","all","am","an",
# "and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't",
# "cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from",
# "further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers",
# "herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its",
# "itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought",
# "our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such",
# "than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're",
# "they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were",
# "weren't","what","what's","when","when's""where","where's","which","while","who","who's","whom","why","why's","with","won't","would",
# "wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves" ])

def prepare_ngram_interaction(path,out,ngram='unigram'):
    data_input = pd.read_csv(path)
    data_ouput = DataFrame(columns=['jaccard_'+ngram,
                                    'dice_'+ngram,
                                    'count_s1_in_s2_'+ngram,
                                    'ratio_s1_in_s2_'+ngram,
                                    'count_of_sen1_'+ngram,
                                    'count_of_sen2_'+ngram,
                                    'count_of_unique_sen1_'+ngram,
                                    'count_of_unique_sen2_'+ngram,
                                    'ratio_of_unique_sen1_'+ngram,
                                    'ratio_of_unique_sen2_'+ngram,
                                    'count_of_digit_sen1_'+ngram,
                                    'count_of_digit_sen2_'+ngram,
                                    'ratio_of_digit_sen1_'+ngram,
                                    'ratio_of_digit_sen2_'+ngram])
    for index,row in data_input.iterrows():
        s1_ngram = str(row['sen1_%s'%ngram]).split()
        s2_ngram = str(row['sen2_%s'%ngram]).split()

        jaccard = get_jaccard(s1_ngram,s2_ngram)
        dice = get_dice(s1_ngram,s2_ngram)

        count_s1_in_s2 = get_count_s1_in_s2(s1_ngram,s2_ngram)
        ratio_s1_in_s2 = get_ratio_s1_in_s2(s1_ngram,s2_ngram)

        count_of_sen1 = get_count_of_sen(s1_ngram)
        count_of_sen2 = get_count_of_sen(s2_ngram)


        count_of_unique_sen1 = get_count_of_unique_sen(s1_ngram)
        count_of_unique_sen2 = get_count_of_unique_sen(s2_ngram)

        ratio_of_unique_sen1 = get_ratio_of_unique_sen(s1_ngram)
        ratio_of_unique_sen2 = get_ratio_of_unique_sen(s2_ngram)

        count_of_digit_sen1 = get_count_of_digit(s1_ngram)
        count_of_digit_sen2 = get_count_of_digit(s2_ngram)
        
        ratio_of_digit_sen1 = get_ratio_of_digit(s1_ngram)
        ratio_of_digit_sen2 = get_ratio_of_digit(s2_ngram)
                        
        data_ouput.loc[index] = [jaccard,
                                dice,
                                count_s1_in_s2,
                                ratio_s1_in_s2,
                                count_of_sen1,
                                count_of_sen2,
                                count_of_unique_sen1,
                                count_of_unique_sen2,
                                ratio_of_unique_sen1,
                                ratio_of_unique_sen2,
                                count_of_digit_sen1,
                                count_of_digit_sen2,
                                ratio_of_digit_sen1,
                                ratio_of_digit_sen2]
    data_ouput.to_csv(out,index=False)
        

if isCase ==False:
    prepare_ngram_interaction(path+'train_unigram.csv',path+'train_unigram_features.csv',ngram='unigram')
    prepare_ngram_interaction(path+'test_unigram.csv',path+'test_unigram_features.csv',ngram='unigram')

    prepare_ngram_interaction(path+'train_bigram.csv',path+'train_bigram_features.csv',ngram='bigram')
    prepare_ngram_interaction(path+'test_bigram.csv',path+'test_bigram_features.csv',ngram='bigram')
else:
    prepare_ngram_interaction(path+'case_unigram.csv',path+'case_unigram_features.csv',ngram='unigram')
    prepare_ngram_interaction(path+'case_bigram.csv',path+'case_bigram_features.csv',ngram='bigram')

