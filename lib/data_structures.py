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
    return [food['name'] for food in spicy_foods]
    
def get_spiciest_foods(spicy_foods, min_heat = 5):
   return [food for food in spicy_foods if min_heat <= food['heat_level']]
   
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
         heat_level_string = '🌶' * food['heat_level']
         print(f'{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_string}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
           return food
    return None
    

def print_spiciest_foods(spicy_foods, min_heat = 5):
    for food in get_spiciest_foods(spicy_foods):
        heat_level_emojis = '🌶' * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
   

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)
   

def create_spicy_food(spicy_foods, spicy_food):
    
    spicy_foods.append(spicy_food)
    return spicy_foods

    
