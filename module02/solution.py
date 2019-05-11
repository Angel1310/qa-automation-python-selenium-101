import os


def num_add(a, b):
	result = a + b
	return result

def num_sub(a, b):
	result = a - b
	return result

def num_mul(a, b):
	result = a * b
	return result

def num_div(a, b):
	result = float(a) / float(b)
	return result

def num_floor(a, b):
	result = a // b
	return result

def num_rem(a, b):
	result = a % b
	return result

IS_TRUE = True
IS_FALSE = False

PANCAKE_INGREDIENTS = {
	"flour": 2,
	"eggs": 4,
	"milk": 200,
	"butter": False,
	"salt": 0.001 }

def ingredient_exists(ingr, dict):
	if dict.has_key(ingr):
		return IS_TRUE
	else:
		return IS_FALSE

def fatten_pancakes(dict):
	dict_copy = dict.copy()
	dict_copy['eggs'] = 6
	dict_copy['butter'] = True
	return dict_copy

def add_sugar(dict):
	new_dict = dict.copy()
	new_dict['sugar'] = 1
	return new_dict

def remove_salt(dict):
	new_dict = dict.copy()
	new_dict.pop("salt")
	return new_dict

FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def add_fibonacci(lst):
	fib = lst[len(lst) - 1] + lst[len(lst) - 2]
	lst.append(fib)
	return lst

def fib_exists(lst, n):
	if(n in lst):
		return True
	else:
		return False

def which_fib(lst,n):
		return lst.index(n)+1
