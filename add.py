import json

my_dict = dict()
key = input("Enter the word:")
value = input("Enter the definition:")

# Get previous data
with open("data.json", mode = "r") as old_dict:
    my_dict = json.load(old_dict)

my_dict[key] = value

# Write to file
with open("data.json", mode = "w") as new_dict:
	(json.dump(my_dict, new_dict))
