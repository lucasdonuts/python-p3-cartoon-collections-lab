def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i + 1}. {dwarves[i]}")

def summon_captain_planet(calls):
    return [f"{call.capitalize()}!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    
    return False

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]

    for food in foods:
        if food in cheeses:
            return food

    return None

# Module cartoon_collections.py prints out the 7 dwarfs in a numbered list F
# Module cartoon_collections.py returns a list with the same number of elements that it was given F
# Module cartoon_collections.py capitalizes each element and adds an exclamation mark F
# Module cartoon_collections.py returns true if any calls are longer than 4 characters F
# Module cartoon_collections.py returns false if all calls are 4 characters or less F
# Module cartoon_collections.py returns the first element of the array that is cheese F
# Module cartoon_collections.py returns None if the array does not contain a type of cheese F