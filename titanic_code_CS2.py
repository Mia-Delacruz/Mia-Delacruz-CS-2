
'''
Flower Box:
delacruz_mia_TITANIC.py
date: Fri 1/30

Description: for each function user gets to see real data applicable to those on the titanic and survival rates
Features: graph  

Log: 1.0

Bugs: none
'''
def display_rows(file): 
    '''
    Args:
        vairable(type): Description of variable. list [float] list a specific row example: gender, pclass, price etc 
    Returns:
        variable(type): displays certain row from titanic csv  
    Raises:
        Error: none 

    '''
    next(file)
    i = 0

    for row in file: 
        row = row.strip().split(',')
        print(row)
        i += 1
        
        if i == 10:
            break

def get_survival_rate(file): 
    '''
    Args:
        vairable(type): Displays list from row to calculate survival rate.
    Returns:
        variable(type): Displays the survival rate of passengers and how many passed. 
    Raises:
        Error: none 

    '''
    survived = 0 
    total = 0 
    file.seek(0)
    next(file)

    for line in file: 
        row = line.strip().split(',')

        if row [1] == "1": 
            survived +=1
        total += 1
        
    print(f"Total Passengers: {total}")
    print(f"Survived: {survived}")
    print(f"Died: {total-survived}")
    print(f"Survival Rate: {survived/total*100:.2f}%")

def get_gender_data(file):
    '''
    Args:
        vairable(type): displays list from the gender row of female and males.
    Returns:
        variable(type): returns the average of female survived versus men survived on the titanic   
    Raises:
        Error: none 
    '''
    file.seek(1)
    male_counter = 0
    male_survived = 0
    female_counter = 0
    female_survived = 0

    file.seek(0)
    next(file)

    for line in file:
        row = line.strip().split(',')

        if row[5] == "male":
            male_counter += 1

            if row[1] == "1":
                male_survived += 1
        elif row[5] == "female":
            female_counter += 1

            if row[1] == "1":
                female_survived += 1

    print(f"Total Males: {male_counter}")
    print(f"Male Survival Rate: {male_survived/male_counter*100:.2f}%")
    print(f"Total Females: {female_counter}")
    print(f"Female Survival Rate: {female_survived/female_counter*100:.2f}%")

def get_age_data(file): 
    '''
    Args:
        vairable(type): uses row 6 and 1 as list to calculate 
    Returns:
        variable(type): retrurns the average age a passenger survived or passed and probability .  
    Raises:
        Error: none
    '''

    min_age = 200
    min_passenger = ''
    max_age = 0
    max_passenger = ''
    age_survived = []
    age_died = []

    file.seek(0)
    next(file)

    for line in file: 
        row = line.strip().split(',')

        if row[6] == '':
            continue

        if float(row[6]) > max_age:
            max_age = float(row[6])
            max_passenger = row[4] + row[3]
        elif float(row[6]) < min_age:
            min_age = float(row[6])
            min_passenger = row[4] + row[3]

        if row[1] == "1":
            age_survived.append(float(row[6]))
        else:
            age_died.append(float(row[6]))

    print(f"Min age: {min_passenger} at {min_age}")
    print(f"Max age: {max_passenger} at {max_age}")
    print(f"Average age of passengers: {(sum(age_died)+sum(age_survived))/(len(age_died)+len(age_survived)):.2f}")
    print(f"Average age of survived passengers: {sum(age_survived)/len(age_survived):.2f}")
    print(f"Average age of died passengers: {sum(age_died)/len(age_died):.2f}")

def get_class_data(file): 
    '''
    Args:
        vairable(type):  uses row 1 and 2 and list to determine class survival 
    Returns:
        variable(type): returns probablitly of how gender and class affected survival and difference between women 
        in upperclass versus men in lower class probability to survive the titanic.  
    Raises:
        Error: none 

    '''
    fares = 0
    total = 0
    class1_total = 0
    class2_total = 0
    class3_total = 0
    class1_survived = 0
    class2_survived = 0
    class3_survived = 0
    class1_fares = 0
    class2_fares = 0
    class3_fares = 0

    file.seek(0)
    next(file)

    for line in file: 
        row = line.strip().split(',')
        fares += float(row[10])
        total += 1

        if row[2] == "1":
            class1_total += 1
            class1_fares += float(row[10])
            
            if row[1] == "1":
                class1_survived += 1
        elif row[2] == "2":
            class2_total += 1
            class2_fares += float(row[10])
            
            if row[1] == "1":
                class2_survived += 1
        elif row[2] == "3":
            class3_total += 1
            class3_fares += float(row[10])
            
            if row[1] == "1":
                class3_survived += 1
    
    print(f"Average Fare: ${fares/total:.2f}")
    print(f"Class 1 Total: {class1_total}")
    print(f"Class 1 Survived: {class1_survived}")
    print(f"Class 1 Average Fare: ${class1_fares/class1_total:.2f}")
    print(f"Class 1 Survival Rate: {class1_survived/class1_total*100:.2f}%")
    print()
    print(f"Class 2 Total: {class2_total}")
    print(f"Class 2 Survived: {class2_survived}")
    print(f"Class 2 Average Fare: ${class2_fares/class2_total:.2f}")
    print(f"Class 2 Survival Rate: {class2_survived/class2_total*100:.2f}%")
    print()
    print(f"Class 3 Total: {class3_total}")
    print(f"Class 3 Survived: {class3_survived}")
    print(f"Class 3 Average Fare: ${class3_fares/class3_total:.2f}")
    print(f"Class 3 Survival Rate: {class3_survived/class3_total*100:.2f}%")

def main():
    '''
    Args:
        vairable(type): uses entire gender csv and titanic csv and rows to determine specfic data to user 
    Returns:
        variable(type): returns data from all functions above   
    Raises:
        Error: none
    '''
    filename = 'titanic.csv'
    
    try:
        with open(filename, 'r') as file:
            while True:
                choice = input("choose a function or 'X' to exit the program: 0. Display 10 rows, 1. Surival Rates, 2. Gender Breakdown, 3. Age Breakdown")
                
                if choice == "0":
                    display_rows(file)
                elif choice == "1":
                    get_survival_rate(file)
                elif choice == "2":
                    get_gender_data(file)
                elif choice == "3":
                    get_age_data(file)
                elif choice == "4":
                    get_class_data(file)
    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")
        
if __name__ == '__main__':
    main()
