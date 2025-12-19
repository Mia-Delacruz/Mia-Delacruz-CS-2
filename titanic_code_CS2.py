
'''
Flower Box:
delacruz_mia_TITANIC.py

Description: Description goes here. 

Features: Features go here. 

Log: 1.0

Bugs: Bugs go here
'''

#this is how you open a file and loop through 

#fhand = open('mbox-short.txt')
#count = 0
#for line in fhand:
#    count = count + 1
#print('Line Count:', count)
def getGender(input):
    '''
    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 

    '''
    with open("gender_data.csv" , "w") as output:

        male_counter = 0
        female_counter = 0
        for line in input:
            row = line.strip().split(',')
            if row[5] == 'male':
                male_counter +=1
            elif row[5] == 'female':
                female_counter +=1
            #print(row[name_index])
        output.write("MALES" + "," + "FEMALES\n")
        output.write(str(male_counter) + "," + str(female_counter))
        output.write()
       
        print("TOTAL MALES: " + str(male_counter))
        print("TOTAL FEMALES: " + str(female_counter))

def getsurvivalRate(input): 
    '''
    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 

    '''
with open ('survival_data.csv', 'w') as output:
    survivalrate_counter = 0 
    average_counter = 0 
    totalpassenger_counter= 0 
    totaldead_counter = 0 

for line in input: 
    row = line.strip().split(',')
    if row [2] == 1: 
        survivalrate_counter +=1
        totalpassenger_counter +=1
    if row [2] == 0: 
        totaldead_counter +=1
        totalpassenger_counter +=1
    
    total_passengers = 2224
    total_dead = 706
    print ('1465')

def getAge(input): 
    '''
    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 
    '''
age_counter = 0 
for line in input: 
    row = line.strip().split(',')
    if row[6] == '':
        age_counter +=1
        output.write('age' + 'counter\n')
        print

def main():
    '''
 Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 

    '''
    try:
        with open('titanic.csv', 'r') as file:
            while True:
                choice = input("choose a function or 'X' to exit the program: 1. Gender")
                if choice == "1":
                    getGender(file)
    
    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")
        
    pass


def main():
    input_file = 'titanic.csv'
    with open(input_file, 'r') as infile:
        getGender(infile)

if __name__ == '__main__':
    main()




