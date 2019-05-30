import os

def sum_of_digits(n):
    if n < 0:
        n = abs(n)

    sum = 0
    while n:
        sum += n % 10
        n = n // 10

    return sum


def to_digits(n):
    l = []
    if n < 0:
        n = abs(n)

    while n:
        b = n % 10
        n = n // 10
        l.append(b)

    return list(reversed(l))

def to_number(digits):

    number = i = 0
    for digit in list(reversed(digits)):
        number += digit * (10 ** i)
        i += 1

    return number


def count_vowels(str):
    vowels = "aeiouy"
    str = str.lower()
    count = 0
    for letter in str:
        if (letter in vowels):
            count += 1

    return count


def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    str = str.lower()
    i = 0
    for letter in str:
        if (letter in consonants):
            i += 1

    return i


def prime_number(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

def fact_digits(n):
    sum = 0

    for number in to_digits(n):
        sum += factorial(number)

    return sum

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    fib = [1,1]
    if n <= 1:
        return [1]

    while len(fib) < n:
        fib_next = fib[len(fib) - 1] + fib[len(fib) - 2]
        fib.append(fib_next)

    return fib

def fib_number(n):
    result = ''

    for number in fibonacci(n):
        result += str(number)

    return int(result)


def palindrome(obj):
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

def char_histogram(str):
    letters = []
    dict = {}

    for char in str:
        letters.append(char)
        dict[char] = letters.count(char)


    return dict
