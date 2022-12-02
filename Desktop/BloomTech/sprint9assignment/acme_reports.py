import random
from acme import Product 

# Useful to use with random.sample or random.choice to generate names
adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def name():
    rand_adj = random.choice(adjectives)
    rand_nouns = random.choice(nouns) 
    return rand_adj + ' ' + rand_nouns

def price():
    return random.randint(5,100)

def weight():
    return random.randint(5,100)

def flammability():
    return random.uniform(0.0,2.5)

def product_tuple():
    return (name(), price(), weight(), round(flammability(), 1))

# ====================================

def generate_products(num_products=30):
    product_list = []
    for item in range(num_products):
        product_list.append(product_tuple())
    
    return product_list

# ====================================

def generate_names_list(num_products=30):
    names_list = []
    for item in range(num_products):
        names_list.append(product_tuple()[0])
    
    return names_list

def unique_val_of_names():
    num_of_unique = len(set(generate_names_list()))
    
    return num_of_unique

# ====================================

def generate_price_list(num_products=30):
    price_list = []
    for item in range(num_products):
        price_list.append(product_tuple()[1])
    
    return price_list

def avg_price_of_prods():
    return sum(generate_price_list()) / len(generate_price_list())

# ====================================

def generate_weight_list(num_products=30):
    weight_list = []
    for item in range(num_products):
        weight_list.append(product_tuple()[2])
    
    return weight_list

def avg_weight_of_prods():
    return sum(generate_weight_list()) / len(generate_weight_list())

# ====================================

def generate_flam_list(num_products=30):
    flam_list = []
    for item in range(num_products):
        flam_list.append(product_tuple()[3])
    
    return flam_list

def avg_flam_of_prods():
    return sum(generate_flam_list()) / len(generate_flam_list())

# ====================================

def inventory_report():
    return(unique_val_of_names(),
    round(avg_price_of_prods(), 1),
    round(avg_weight_of_prods(), 1),
    round(avg_weight_of_prods(), 1),
    round(avg_flam_of_prods(), 1))

print(generate_flam_list())
print(avg_flam_of_prods())
print(inventory_report())

# print(inventory_report(generate_products()))

# def unique_val():
#     num_of_unique = len(set(generate_products()))
#     return num_of_unique

# print(unique_val())



