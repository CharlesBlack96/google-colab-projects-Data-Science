import pandas as pd
import numpy as np
import random


adjectives = ['blue','large','grainy',
'substantial','potent','thermonuclear']
nouns = ['food','house','tree','bicycle',
'toupee','phone']

def random_phrase():
    adj = random.choice(adjectives)
    noun = np.random.choice(nouns)
    return adj + ' ' + noun

# print(random_phrase())

def random_float(min_val,max_val):
    return random.uniform(min_val,max_val)

# print(random_float(2,4))
# print(random_float(3,7))

def random_bowling_score():
    return random.randint(0,300)

# print(random_bowling_score())

def silly_tuple():
    return (random_phrase(), round(random_float(1,5), 1), random_bowling_score())

# print(silly_tuple())
# print(silly_tuple())
# print(silly_tuple())

def silly_tuple_list(num_tuples):
    tuple_list = []
    for item in range(num_tuples):
        tuple_list.append(silly_tuple())
    return tuple_list

# print(silly_tuple_list(5))

test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
null_df = pd.DataFrame(np.array([[1,np.nan,3],[np.nan,5,6],[7,8,np.nan]]))


def null_count(df):
    return df.isnull().sum().sum()

# print(null_count(test_df))
# print(null_count(null_df))

def train_test_split(df, frac=0.8):
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test

# print(train_test_split(test_df))



def randomize(df, seed):
    return df.sample(frac=1.0, random_state=seed)

# print(randomize(test_df, 9))

address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
                                        '8394 Kim Meadow\nDarrenVille, AK 27389', 
                                        '379 cain Plaza\nJosephsberg, WY 06332', 
                                        '5803 Tina Hill\nAudreychester, VA 97036']})


def addy_split(addy_series):

    df = pd.DataFrame()
    
    city_list = []
    state_list = []
    zip_list = []

    for addy in addy_series:
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[1]
        zip = second_half.split()[2]

        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip)

    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list

    return df


print(addy_split(address_df['address']))


def abbr_2_st(state_series, abbr_2_st=True):
    pass

def list_2_series(list_2_series, df):
    pass

def rm_doutlier(df):
    pass

def split_dates(date_series):
    pass