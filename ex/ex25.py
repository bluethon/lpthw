def break_words(stuff):
	"""This function will break up words for us."""
	words =stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	pass

def print_first_word(words):
	"""Prints the first word after poping it off."""
	word =words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after poping it off."""
	word = words.pop(-1)
	print word
	pass

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	pass

def print_first_and_last_word(sentence):
	"""Prints the first and last words of the sentence."""
	word = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then print the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

sentence111 = "All good things come to those who wait."
words = break_words(sentence111)
print words

