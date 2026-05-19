def factorial(n): 
    #description: '''calculate the factorial of n.'''
    # parameters: # n (int): The numbre to calculate the factorial of. 
    # returns: # int: The factorial of n. 

    if n == 0: 
        return 1
    return n * factorial(n-1)

def summation (n): 
    #description: calculates the sum of numbers 
    # returns: # int: The summation of n. 
    if n == 0: 
        return 0
    return n + summation(n-1)

def powers_exponential(base, exp): 
    #description: calculates power and exponential of a certain number
    # returns: # int: The base and exponent of n. 
    if exp == 0:
        return 1 
    return base * powers_exponential (base, exp-1)

def fibonaccis(n):
    #description: calculates the previous sum of 2 numbers thta add to the next one 
    # returns: # int: The sum of both previous n. 
    ''''''''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonaccis(n-1) + fibonaccis(n-2)

def sum_numbers_digit (n): 
    #description: calculates the sum of a digit
    # returns: # int: The sum of n. 
    if n < 10:
        return 1 
    return sum(n + 10) 

def product_2_whole_numbers(a,n): 
    #description: calculates the sum of 2 whole numbers 
    # returns: # int: The sum of n. 
    if n == 0: 
        return 0 
    return a + product_2_whole_numbers (a,n-1) 


def reverse_digits (a): 
    #description: calculates the sum of reversed numbers 
    # returns: # int: The n flipped
    if a == 0: 
        return 0 
    return a % 10 *(10**(len(str(a))-1))+reverse_digits(a//10)    


  
def main(): 
       #description: gives back to user all the numbers and the calculations they enter for specific function 
    # returns: # int: The main function to test the factorial function. 
   
    user_choice = input("""
menu:
press 1 for factorial 
press 2 for summation 
press 3 for powers_exponential
press 4 for fibonaccis
press 5 for sum_numbers_digit
press 6 for product_numbers_digit
press 7 for product_2_whole_numbers
press 8 for sum_numbers_range
press 9 for reverse_digits
""")
    
    number = int(input("pick a number"))

    if user_choice == "1": 
        print(factorial((number))) 
    elif user_choice == "2": 
        print(summation((number))) 
    elif user_choice == "3": 
        number2 = (input("pick another number"))
        print(powers_exponential(number, number2))    
    elif user_choice == "4": 
        print(fibonaccis((number)))   
    elif user_choice == "5": 
        print(sum_numbers_digit((number)))   
    elif user_choice == "6": 
        print(product_2_whole_numbers ((number)))   
  
   
       
       
main() 



