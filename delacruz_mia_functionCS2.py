import random 

def split_string(string):
    parts = []
    current = ""
    
    for char in string:
        if char == " ":
            parts.append(current)
            current = ""
        else:
            current += char
    parts.append(current)
    return parts
def get_first(fullname):
    names = split_string(fullname)
    return names[0]
def get_middle(fullname):
    names = split_string(fullname)
    return ' '.join(names[1:-1])
def last_name(fullname):
    names = split_string(fullname)
    return names[-1]
def get_initials(fullname):
    '''
    '''
    initials = ''
    #use split_string to split fullname into a list
    
    for name in list:
        #add first letter of name to initials
     return initials
def get_random(string):
    '''
    '''
    #turn string into a list of letters
    #use random.shuffle to scramble the list
    #use join to put the scrambled list back into a string and return
def count_vowels(string):  
    '''
    Counts total vowels in a string and provides a subtotal for each vowel. 

    Args:
     Input string

    Returns:
        Total count of vowels and a dictionary with individual vowel counts.
    '''                                                 
    vc = 0                                                              
    vowels = list('aeiouAEIOU')                                        

    for char in string:                                                      
        if char in vowels:                                              
            vc += 1                                                  
    return vc             
'''
    Counts total consonants in a string and provides a subtotal for each consonant. 

    Args:
     Input string

    Returns:
        Total count of consonants and a dictionary with individual consonant counts.
 '''       

def count_consonants(string): 
    cc = 0 
    consonants = list('bcdfghjklmnopqrstvwxyzBCDFGHJKLMNOPQRSTUVWXYZ')

    for char in string:
          if char in consonants:                                              
                cc += 1                                                  
          return cc                                                          

def reverse_string(string): 
    return string[::-1]
def hyphen (name):
    return '-' in name
def palindrome (name): 
    return name == reverse_string(name)
def lowercase(string): 
    upper_string = ""

    for letter in string: 
        if ord(letter) > 64 and ord(letter) < 91:
            num = ord(letter)
            num += 32
            letter = chr(num) 
        upper_string += letter 
    return upper_string 
def uppercase(string): 
    lower_string = ""

    for letter in string: 
        if ord(letter) > 96 and ord(letter) < 123:
            num = ord(letter)
            num -= 32
            letter = chr(num) 
        lower_string += letter 
    return lower_string 

def main ():
    name = input("Hello user, please enter your name. ")
    print("Welcome {name}")

    while True:
        number = input('''pick a function:
                        1. Reverse and Display 
                        2. Count Vowels 
                        3. Count consonants 
                        4. Return first name 
                        5. Return last name 
                        6. Return middle name 
                        7. Return boolean if last name contains a hyphen 
                        8. Function to convert to lowercase
                        9. Function to convert to uppercase  
                        10.create random name
                        11.return boolean if first name is palindrome
                        12.return first name as sorted array of characters
                        13.build menu (bonus)
                        14.make initials from name
                        15.return boolean if name contains a title
                        16.make own bonus
                        17.secret bonus
        ''')

        if number == '1':
            print(reverse_string(name))
        elif number == 2:
            print(count_vowels(name))
        elif number == 3:
            print(count_consonants(name))
        elif number == 4: 
            print(get_first(name))
        elif number == 5:
            print(last_name(name))
        elif number == 6: 
            print(get_middle(name))
        elif number == 7:
            print(hyphen(name))
        elif number == 8: 
            print(lowercase(name))
        elif number == 9: 
            print(uppercase(name))
        elif number == 10:
            print(get_random(name))
        elif number == 11:
            print(palindrome(name))
        elif number == 14: 
            print(get_initials(name))
        
main()