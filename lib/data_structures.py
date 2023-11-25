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
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names
    

new_list = get_names(spicy_foods)
print(new_list)

def get_spiciest_foods(spicy_foods):
    dict_list = []
    for food in spicy_foods:
        heat_level = food["heat_level"]
        if heat_level > 5:
            dict_list.append(food)
    return dict_list        


result = get_spiciest_foods(spicy_foods)
print(result)            
def print_spicy_foods(spicy_foods):
    # Define a mapping between heat levels and emojis
    heat_level_emojis = {
        1: "🌶",
        2: "🌶🌶",
        3: "🌶🌶🌶",
        4: "🌶🌶🌶🌶",
        5: "🌶🌶🌶🌶🌶",
        6: "🌶🌶🌶🌶🌶🌶",
        7: "🌶🌶🌶🌶🌶🌶🌶",
        8: "🌶🌶🌶🌶🌶🌶🌶🌶",
        9: "🌶🌶🌶🌶🌶🌶🌶🌶🌶",
        10: "🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶",
    }

    # Iterate through each dictionary in the spicy_foods list
    for food in spicy_foods:
        # Construct the output string
        output_string = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis[food['heat_level']]}"

        # Print the output string
        print(output_string)
print_spicy_foods(spicy_foods)
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None     

result = get_spicy_food_by_cuisine(spicy_foods,'Thai')
print(result)
def print_spiciest_foods(spicy_foods):
    heat_level_emojis = {
        1: "🌶",
        2: "🌶🌶",
        3: "🌶🌶🌶",
        4: "🌶🌶🌶🌶",
        5: "🌶🌶🌶🌶🌶",
        6: "🌶🌶🌶🌶🌶🌶",
        7: "🌶🌶🌶🌶🌶🌶🌶",
        8: "🌶🌶🌶🌶🌶🌶🌶🌶",
        9: "🌶🌶🌶🌶🌶🌶🌶🌶🌶",
        10: "🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶",
    }

    # Iterate through each dictionary in the spicy_foods list
    for food in spicy_foods:
        # Check if the heat level is greater than 5
        if food['heat_level'] > 5:
            # Construct the output string
            output_string = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis[food['heat_level']]}"

            # Print the output string
            print(output_string)



print_spiciest_foods(spicy_foods)
def get_average_heat_level(spicy_foods):
      # Check if the list is not empty to avoid division by zero
    if not spicy_foods:
        return 0

    # Calculate the total heat level
    total_heat = sum(food['heat_level'] for food in spicy_foods)

    # Calculate the average heat level
    average_heat = total_heat / len(spicy_foods)

    # Round to the nearest integer
    return round(average_heat)

result = get_average_heat_level(spicy_foods)
print(result) 

def create_spicy_food(spicy_foods, new_food):
    # Create a copy of the original list to avoid modifying it directly
    modified_spicy_foods = spicy_foods.copy()

    # Add the new food to the list
    modified_spicy_foods.append(new_food)

    return modified_spicy_foods

# Example test
def test_create_spicy_food():
    # Original list of spicy foods
    original_spicy_foods = [
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

    # New spicy food to be added
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }

    # Call the function
    new_spicy_foods = create_spicy_food(original_spicy_foods, new_food)

    # Assert the modified list is as expected
    assert new_spicy_foods == [
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
        {
            "name": "Griot",
            "cuisine": "Haitian",
            "heat_level": 10,
        },
    ]

# Run the test
test_create_spicy_food()
