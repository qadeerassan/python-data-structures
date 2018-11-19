"""
-------------------------------------------------------
food_utilities.py
Utilities for working with a Food object.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2018-01-09"
-------------------------------------------------------
"""
from food import Food
from list_linked import List
from sorted_list_linked import SortedList

def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Postconditions:
        returns
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input("Name: ")
    print("Origin")
    print(Food.origins())
    origin = int(input(": "))
    s = input("Vegetarian (Y/N): ")
    # Accept a range of values for vegetarian
    is_vegetarian = s.upper() in ('Y', 'TRUE', '1', 'T', 'YES')
    calories = int(input("Calories: "))
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Preconditions:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Postconditions:
        returns
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    data = line.strip().split("|")
    food = Food(data[0], int(data[1]), data[2] == "True", int(data[3]))
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_food(file_variable)
    -------------------------------------------------------
    Preconditions:
        file_variable - a file of food data (file)
    Postconditions:
        returns
        foods - a list of food objects (list of food)
    -------------------------------------------------------
    """
    file_variable.seek(0)
    foods = []
    
    for line in file_variable:
        food = read_food(line)
        foods.append(food)
    return foods

def read_foods_linked(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_food(file_variable)
    -------------------------------------------------------
    Preconditions:
        file_variable - a file of food data (file)
    Postconditions:
        returns
        foods - a list of food objects (list of food)
    -------------------------------------------------------
    """
    file_variable.seek(0)
    foods = List()

    for line in file_variable:
        food = read_food(line)
        foods.append(food)
    return foods

def read_foods_sorted(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_food(file_variable)
    -------------------------------------------------------
    Preconditions:
        file_variable - a file of food data (file)
    Postconditions:
        returns
        foods - a list of food objects (list of food)
    -------------------------------------------------------
    """
    file_variable.seek(0)
    foods = SortedList()

    for line in file_variable:
        food = read_food(line)
        foods.append(food)
    return foods

def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Preconditions:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Postconditions:
        file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    -------------------------------------------------------
    """
    for food in foods:
        food.write(file_variable)
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        returns
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []

    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)
    return veggies


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: a = average_calories(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        returns
        a - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    tot_cal = 0
    counter = 0
    
    for f in foods:
        tot_cal += f.calories
        counter += 1
    avg = int(tot_cal / counter)

    return avg

def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Postconditions:
        returns
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    ORIGIN = ["Canadian", "Chinese", "Indian", "Ethiopian","Mexican", "Greek", "Japanese", "Italian", "American","Scottish", "New Zealand", "English"]
    origins = []
    
    for f in foods:
        if f.origin == origin:
            origins.append(f)
    
    return origins

def food_table(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: calories_by_origin(foods)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
    Postconditions:
        prints
        a table of the foods sorted by name
    -------------------------------------------------------
    """
    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")
    foods.sort()
    for i in foods:
        if i.is_vegetarian == 0:
            j = False
        else:
            j = True
        print("{:<35} {:<12} {:<10} {:<8}".format(i.name, Food.ORIGIN[i.origin], str(j), i.calories))
    return


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: avg = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Postconditions:
        returns
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    #{:[[fill]align][sign][width][,][.precision][type]}
    ORIGIN = ["Canadian", "Chinese", "Indian", "Ethiopian","Mexican", "Greek", "Japanese", "Italian", "American","Scottish", "New Zealand", "English"]
    tot_cal = 0
    counter = 0

    for f in foods:
        if f.origin == origin:
            tot_cal += f.calories
            counter += 1
    avg = int(tot_cal / counter)
    return avg

def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Preconditions:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Postconditions:
        returns
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    results = []
    
    for food in foods:
        if origin == -1 or food.origin == origin:
            if max_cals == 0 or food.calories <= max_cals:
                if is_veg == False or food.is_vegetarian == is_veg:
                    results.append(food)
    return results