spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   # pass
    names=[food['name'] for food in spicy_foods]
    return names
def get_spiciest_foods(spicy_foods, min_heat = 5):
    #pass
   foods =[food for food in spicy_foods if min_heat <= food['heat_level']]
   return foods
def print_spicy_foods(spicy_foods):
    #pass
    for food in spicy_foods:
         heat_level_string = '🌶' * food['heat_level']
         print(f'{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_string}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #pass
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
           return food
    return None
    

def print_spiciest_foods(spicy_foods, min_heat = 5):
    for food in spicy_foods:
        if food['heat_level'] >= min_heat:
            heat_lev = '🌶' * food['heat_level']
            print(f'{food['name']} ({food['cuisine']}) | Heat Level: {heat_lev}')
    

def get_average_heat_level(spicy_foods):
    average = sum(food['heat_level'] for food in spicy_foods) / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    
    spicy_foods.append(spicy_food)
    return spicy_foods
# new_spicy_food = {
#      'name': 'Griot',
#         'cuisine': 'Haitian',
#         'heat_level': 10,
# }    
    
# print(create_spicy_food(spicy_foods, new_spicy_food))
    
