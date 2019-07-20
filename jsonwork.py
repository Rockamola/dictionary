#library that checks spelling of words
import difflib
from difflib import get_close_matches
import json

data = json.load(open("data.json"))
word = input("Enter word:")

def translate(w):
	w = w.lower()
	if w in data:
		return data[w] #returning word from dictionary
	elif w.title() in data:
		return data[w.title()] #returning if a capitalized word such as "Texas" is entered
	elif len(w.upper()) >1:
		return data[w.upper()]#returning if word is an acronym
	else:
		return "Word is not found in dictionary."	
# returning near match results, in case of misspelling
def compare(word, data):
	com = get_close_matches(word, data)
	if word not in data:
		return com

if word in data:
	print(translate(word))
else:
	print(compare(word, data))
	correct_word = input("Please enter the correct word:")
	if correct_word in data:
		print(translate(correct_word.lower()))
	else:
		different_word = input("Please enter a different word or the correct word:")
		print(translate(different_word))

