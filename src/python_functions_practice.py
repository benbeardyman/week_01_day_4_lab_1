def return_10():
    return 10

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def length_of_string(string):
    return len(string)

def join_string(str_a, str_b):
    return str_a + str_b

def add_string_as_number(a, b):
    return int(a) + int(b)


# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# def number_to_full_month_name(i):
#     return months[i - 1]

# def number_to_short_month_name(i):
#     return months[i - 1][0:3]

import datetime

def number_to_full_month_name(i):
    x = datetime.datetime(2022, i, 1)
    return x.strftime("%B")

def number_to_short_month_name(i):
    x = datetime.datetime(2022, i, 1)
    return x.strftime("%b")


def volume_of_cube(x):
    return x**3

def reversed_string(a):
    return a[::-1]

def far_to_cel(temp):
    return (temp - 32) * 5/9


