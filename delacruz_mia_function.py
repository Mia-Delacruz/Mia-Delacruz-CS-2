
def count_vowels (s):                                                   
    vc = 0                                                              
    vowels = list ('aeiouAEIOU')                                        

    for char in s:                                                      
        if char in vowels:                                              
            vc = vc +1                                                  
    return vc                                                          
\
    '''
    vowels = "aeiou" 
    subtotals = {v: s.lower () .count (v) for v in vowels}
    total = sum ('subtotals.values' () )
    Return = total, 'subtotals'

    text = "Hello, this is a sample sentence." 
    total, subtotals = 'count_vowels'

    print (f"Total vowels: {total}")
    print ("Subtotal for each vowel:",subtotals)

    '''

'''
    Counts total vowels in a string and provides a subtotal for each vowel. 

    Args:
     Input string

    Returns:
        Total count of vowels and a dictionary with individual vowel counts.
    '''



def count_consonants (name): 
    cc = 0 
    vowels = list ( 'aeiouAEIOU')

    for char in vowels:
        cc= cc + 1

        return cc


def reverse(name):
   return name [::-1] 


def main():
    name = input("Hello user, please enter your name.")
    print("Welcome {name}")

    output = count_vowels('name')
    print (output)


main()