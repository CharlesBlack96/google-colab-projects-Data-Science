import pandas as pd
import numpy as np
import random

#part 2 functions
adjectives = ['blue','large','grainy',
'substantial','potent','thermonuclear']
nouns = ['food','house','tree','bicycle',
'toupee','phone']



def random_phrase():
    adj = random.choice(adjectives)
    noun = np.random.choice(nouns)
    
    
    #random_index = random.randint(0, len(nouns)-1)
    #noun = nouns[random_index]
    #works the same as above code

    #random.sample(nouns, 1)[0] #['house']

    return adj + '' + noun

# print(random_phrase())
# print(random_phrase())
# print(random_phrase())
#once we found these printed what we wanted we comment 
# them out so they dont show when we test our other functions down below
    


def random_float(min_val,max_val):
    return random.uniform(min_val,max_val)

# print(random_float(2,4))
# print(random_float(2,4))
# print(random_float(2,4))


def random_bowling_score():
    return random.randint(0, 300)

# print(random_bowling_score())
# print(random_bowling_score())
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


#part 3 functions

test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
null_df = pd.DataFrame(np.array([[np.nan,2,3],[np.nan,5,6],[7,np.nan,9]]))

def null_count(df):
    return df.isnull().sum().sum()

# print(null_count(test_df))
# print(null_count(null_df))

def train_test_split(df, frac=0.8):
    train = df.sample(frac=frac) #train dataset will be a random 80% split of original df
    test = df.drop(train.index) #all the rest in test dataset
    return train, test

# print(train_test_split(test_df))

def randomize(df, seed):
    randomized_df =  df.sample(frac=1.0, random_state=seed)
    return randomized_df

# print(randomize(test_df, 10))
address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
                                        '8394 Kim Meadow\nDarrenVille, AK 27389', 
                                        '379 cain Plaza\nJosephsberg, WY 06332', 
                                        '5803 Tina Hill\nAudreychester, VA 97036']})

def addy_split(addy_series):
    #dlank df
    df = pd.DataFrame()

    #lists to add 
    city_list = []
    state_list = []
    zip_list = []

    for addy in addy_series:
        #find values in staring
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[-2]
        zip = second_half.split()[2]
    # add stings to list
        city_list.append(city)
        state_list.append(state)
        zip_list.append[zip]

    #add the lists as new columns on the df
    df['city'] = city_list
    df['state'] = state_list 
    df['zip'] = zip_list

    return df

# print(addy_split(address_df['address']))

    def addr_2_st(state_series, abbr_2_st=True):
        state_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


    def abbrev_replace(abbrev):
        return state_dict[abbrev]

    def state_replace(state_name):
        reverse_state_dict = dict((v,k)for k, v in state_dict.items())
        return reverse_state_dict[abbrev]

    if abbr_2_st:
        return state_series.apply(abbrev_replace)
    else:
        return state_series.apply(state_replace)

addy_states = addy_split(address_df['address'])['state']    


print(abbr_2_st(abbr_2_st(addy_states)))


def list_2_series(list_2_series, df):
    pass

def rm_outlier(df):
    pass

def split_dates(date_series):
    pass

