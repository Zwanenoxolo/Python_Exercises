# Name: 

def calculate_product_or_sum(num1, num2):
    """
    Calculate the multiplication and sum of two numbers.
    If the product is <= 1000, return it; otherwise, return the sum.
    """
    multiplication = num1*num2
    if multiplication <=1000:
        return multiplication
    else:
        return num1+num2
    
result1 = calculate_product_or_sum(20, 30)  
result2 = calculate_product_or_sum(40, 30)  
print("Result 1:", result1)
print("Result 2:", result2)

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num  
    return total
numbers = [1, 2, 3, 4, 5]
print(sum_of_list(numbers))

def multiply_list(numbers):
    """
    Multiply all the numbers in a given list.
    """
    total = 1  
    for num in numbers:
        total *= num  
    return total
numbers = [2, 3, 4]
print(multiply_list(numbers))

def characters_at_even_indices(input_string):
    """
    Display characters at even index positions.
    """
    pass  # Replace with your code

def check_first_last_same(numbers):
    """
    Check if the first and last elements of a list are the same.
    """
    if not numbers:
        return False
    else:
       return numbers[0] == numbers[-1]
    

def numbers_divisible_by_five(numbers):
    """
    Display numbers divisible by 5 from a list.
    """
    divisble=[]
    for x in numbers:
        if x % 5==0:
            print(x)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers_divisible_by_five(numbers))
# Intermediate Exercises                                                                                                            

def count_even_odd(numbers): 
    """
    Count even and odd numbers in a list.
    """
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return even_count, odd_count
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = count_even_odd(numbers)
print("Even count:", even_count)  
print("Odd count:", odd_count) 

def skip_numbers():
    """
    Print all numbers from 0 to 6 except 3 and 6.
    """
    for num in range(7):  # Loop through numbers from 0 to 6
        if num == 3 or num == 6:
            continue  # Skip the numbers 3 and 6
        print(num)
skip_numbers()

def reverse_string(input_string):
    """
    Reverse a given string.
    """
    return input_string[::-1]
print(reverse_string("Noxolo"))

def remove_first_n_chars(input_string, n):
    """
    Remove the first n characters from a string.
    """
    return input_string[n:]
print(remove_first_n_chars("python", 2))


def max_of_three(num1, num2, num3):
    """
    Find the maximum of three numbers.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_of_three(5, 10, 15))

def fizzbuzz():
    """
    Print numbers 1 to 50 with FizzBuzz logic.
    """
    def fizzbuzz():
        """
    Print numbers 1 to 50 with FizzBuzz logic.
    """
    for i in range(1, 51):  
        if i % 3 == 0 and i % 5 == 0:  
            print("FizzBuzz")
        elif i % 3 == 0: 
            print("Fizz")
        elif i % 5 == 0:  
            print("Buzz")
        else:  
            print(i)
fizzbuzz()

# Advanced Exercises

def count_upper_lower(input_string):
    """
    Count uppercase and lowercase letters in a string.
    """
    upper_count = 0
    lower_count = 0
    
    for char in input_string:
        if char.isupper():  
            upper_count += 1
        elif char.islower():  
            lower_count += 1
    
    return upper_count, lower_count
input_string = "I am Learning Python"
upper, lower = count_upper_lower(input_string)
print(f"Uppercase letters: {upper}")  
print(f"Lowercase letters: {lower}")

def distinct_elements(numbers):
    """
    Return distinct elements from a list.
    """
    return list(set(numbers))
numbers = [1, 2, 3, 4, 1, 3,2, 5, 4]
distinct = distinct_elements(numbers)
print(distinct)  

import math

def is_prime(number):
    """
    Check if a number is prime.
    """
    if number <= 1:
        return False  
    if number == 2:
        return True  
    if number % 2 == 0:
        return False  
    
    for i in range(3,int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False  
    return True  


def factorial(number):
    """
    Find the factorial of a number.
    """
    if number < 0:
        return None  
    num = 1
    for i in range(1, number + 1):
        num *= i
    return num


def check_voting_eligibility(name, age):
    """
    Check if a person is eligible to vote.
    """
    if age >= 18:
        return f"{name} is eligible to vote."
    else:
        return f"{name} " 
print(check_voting_eligibility("Aphiwe", 11))

# Bonus Exercises

def fibonacci_sequence(n):
    """
    Print the Fibonacci sequence up to n terms.
    """
    pass  # Replace with your code

def common_elements(list1, list2):
    """
    Find common elements in two lists.
    """
    common_set = set(list1) & set(list2)
    return list(common_set)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(common_elements(list1, list2))

def is_palindrome(input_string):
    """
    Check if a string is a palindrome.
    """
    pass  # Replace with your code

def second_largest(numbers):
    """
    Find the second largest number in a list.
    """
    pass  # Replace with your code

def sum_of_digits(number):
    """
    Calculate the sum of digits in an integer.
    """
    number = abs(number) 
    ktotal_sum = 0
    while number > 0:
        total_sum += number % 10  
        number //= 10  
    
    return total_sum
    print(sum_of_digits(12345))



# Do not touch the following section *****
# Main function to test the solutions
if __name__ == "__main__":
    print("Python Practice Problems")
    print("Implement the functions and test them here!")
