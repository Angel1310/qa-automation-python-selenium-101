''' Module03'''

def sum_of_digits(digit_sum):
    ''' sum digits '''

    digit_sum = abs(digit_sum)

    result_sum = 0
    while digit_sum:
        result_sum += digit_sum % 10
        digit_sum = digit_sum // 10

    return result_sum


def to_digits(num_to_d):
    ''' to digits '''


    num_to_d = abs(num_to_d)
    list_digits = []
    while num_to_d:
        list_digits.append(num_to_d % 10)
        num_to_d = num_to_d // 10

    return list(reversed(list_digits))


def to_number(digits):
    ''' to n '''
    number = i = 0
    for digit in reversed(digits):
        number += digit * (10 ** i)
        i += 1

    return number


def count_vowels(input_word):
    '''count vowels '''
    vowels = "aeiouy"
    input_word = input_word.lower()
    count = 0
    for letter in input_word:
        if letter in vowels:
            count += 1

    return count


def count_consonants(input_word):
    '''count consonants '''
    consonants = "bcdfghjklmnpqrstvwxz"
    input_word = input_word.lower()
    i = 0
    for letter in input_word:
        if letter in consonants:
            i += 1

    return i


def prime_number(p_num):
    ''' to prime number '''
    for i in range(2, p_num):
        if (p_num % i) == 0:
            return False

    return True

def fact_digits(to_fact):
    '''return factorial of digits of number'''
    result_sum = 0

    for number in to_digits(to_fact):
        result_sum += factorial(number)

    return result_sum

def factorial(to_fact):
    '''return factorial of a number'''
    if to_fact == 0 or to_fact == 1:
        return 1
    else:
        return to_fact * factorial(to_fact - 1)

def fibonacci(to_fib):
    '''return list with fibonacci number'''
    fib = [1, 1]
    if to_fib <= 1:
        return [1]

    while len(fib) < to_fib:
        fib_next = fib[len(fib) - 1] + fib[len(fib) - 2]
        fib.append(fib_next)


    return fib

def fib_number(to_fib):
    '''fibonacci number'''
    result = ''

    for number in fibonacci(to_fib):
        result += str(number)

    return int(result)


def palindrome(obj):
    '''check for palindrome '''
    first = 0
    last = -1
    string = str(obj)
    count = len(string) // 2
    while first < count:
        if string[first] != string[last]:
            return False
        first += 1
        last -= 1

    return True

def char_histogram(word):
    '''histogram'''
    letters = []
    word_dict = {}

    for char in word:
        letters.append(char)
        word_dict[char] = letters.count(char)


    return word_dict
