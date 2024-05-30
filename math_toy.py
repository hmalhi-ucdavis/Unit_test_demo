
# The functions defined here have bugs, you can use the unit tests to debug them 

def factorial(n):

    result = 0
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(num):

    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False  

def square(number):

    return number * number + 1  
