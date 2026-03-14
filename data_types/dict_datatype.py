# Create a dictionary to store learner information.
my_dictionary = {
    "first": "John",
    "last": "Doe",
    "city": "New York",
    "year": 2023,
    "average": 100
}

# Access values in the dictionary.
print(my_dictionary["first"])  # Output: John
print(my_dictionary["last"])
print(my_dictionary["year"])   # Output: 2023
print(my_dictionary["city"])


car = dict(brand='Toyota', model='Camry', year=2022)
print(car)

# ======== Access values in the dictionary.
print(car["brand"])  # Output: Toyota
print(car["model"])  # Output: Camry
print(car["year"])  # Output: 2022


keys = ['a', 'b', 'c']
values = ["A for Apple", "B for banana", "C for Cat"]
my_dict = dict(zip(keys, values))
print(my_dict)

# Access values in the dictionary.
print(my_dict["a"])
print(my_dict["b"])
print(my_dict["c"])

# Create a new dictionary
electric_car = {
    "year": "2026"
}

# Updating
# update the dict with new key:value pair
electric_car['year'] = '2025'

# Adding new key:value
electric_car['model'] = 'X'
electric_car['make'] = 'Tesla'

print(electric_car)

sample_dict = {"java" : 1, "python" : 2, "nodejs" : 3}
print('BEFORE UPDATE: ',sample_dict)

sample_dict.update( nodejs = 2 )
sample_dict.update( python = 3 )

print('AFTER UPDATE: ', sample_dict)


# initialize the books and the more_books dictionaries:
books = {'Fluent Python':50, 'Learning Python':58}
more_books = {'Effective Python':40, 'Think Python':29}

# you can call the update() method on the books dictionary and pass in more_books, as shown:
books.update(more_books)
print(books) 

# Delete a key:value pair
del books["Fluent Python"]
print('AFTER DELETING: ', books)



game = {
    "health": 100,
    "points": 0,
    "level": 1,
    "pet": {
        "power_level": 9000,
        "abilities": ['jump', 'roll']
    }
}

print(game["pet"]['abilities'][1])

print(game.get('name', 'TestUser'))
# print(game['name'])

# Dict methods
print("KEYS: ",game.keys())
print("VALUES: ", game.values())
print("ITEMS: ", game.items())

# Tuples as keys in dicts
fruit_colors = {( 'apple', 'banana'): 'yellow', ('cherry', 'date'): 'red'}
print(fruit_colors[('apple', 'banana')])
