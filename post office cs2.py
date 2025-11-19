'''
author: Delacruz, Mia
sources: Mr.Campell, Assignment sheet
Bugs: I had to make sure post was in front of the word type due to the code not working from it becuase type is a key word 
Log: 1.0
'''

def main(): 
    '''
    ask user what data they want to use 
    enter split function for data 
    set length data equal to 0
    set height data equal to 1
    set thickness data equal to 2
    set zip 1 to 3
    set zip 2 to 4
    from zone is equal to zip 1
    to zone is equal to zip 2
    set total distance equal to zone_to - zone_from
    enter l,h,w post type 
    '''
    data = input('what is your data')
    data = data.split(',')
    length = float (data[0])
    height = float(data[1])
    thickness = float(data[2])
    zip_1 = int(data[3])
    zip_2 = int(data[4])

    print ('the variable length is' + str(length))
    print ('the variable height is' + str(height))
    print ('the variable thickness is' + str(thickness))
    print ('the variable zip_1 is' + str(zip_1))
    print ('the variable zip_2 is' + str(zip_2))
    

    zone_from = zone(zip_1)
    zone_to = zone(zip_2) 

    total_distance = zone_to - zone_from
    print(total_distance)

    type = get_mailtype(length,height,thickness)

    cost = get_cost( type, total_distance)

    print(cost)

def zone(zip):
    '''
    Args: zip numbers 
    if zip is less and equal to length with and height return 
    do same thing for all other zipcodes and return each after
    '''
    output = 0 
    if zip >= 1 and zip <= 6999:
        return 1 
    elif zip >= 7000 and zip <= 19999 :
        return 2
    elif zip >= 20000 and zip <= 35999:
        return 3 
    elif zip >= 36000 and zip <= 62999:
        return 4 
    elif zip >= 36000 and zip <= 84999:
        return 5
    elif zip >= 85000 and zip <= 99999:
        return 6 

def get_mailtype(l,h,w): 
    '''
    post type equal to ''
    package area formula for w and h
    enter all if and elif statements for l,h,w + different types of packages to mail 
    and accurate nummbers coherant with each value 
    if none apply package is unmailable 
    return post type to user 
    '''
    post_type = ''
    package_area = l + 2*(w+h) 

    if l > 3.5 and l < 4.25 and h > 3.5 and  h < 6 and w > .007 and w <.016:
        post_type = ('postcard')
    elif l > 4.5 and l < 6 and h > 6 and  h < 11.5 and w > .007 and w <.015:
         post_type = ('large post card')
    elif l > 3.5 and l < 6.125 and h > 5 and  h < 11.5 and w > .016 and w <.25:
          post_type = ('envelope')
    elif l > 6.125 and l < 24 and h > 11 and  h < 18 and w > .25 and w <.5:
           post_type = ('large envelope')
    elif package_area > 84 < 130: 
         post_type = 'package'
    elif package_area > 84 < 130: 
         post_type = 'large package'
    else:
         post_type = 'unmailable'
    return  post_type

def get_cost(post_type,distance): 
    '''
   function: get_cost
   description: calculate cost on zones and mail type
   args: 
   post_type (str): type of mail 
   zones(int): zone diff
    print ('the variable length is' + str(length))
   returns: float: shipping cost 
    '''
    get_cost 
    if post_type == 'postcard': 
        cost = .2 + .03 * distance
    elif post_type == 'large post card': 
        cost = .37 + .03 * distance 
    elif post_type == 'envelope':
        cost = .37 + .04 * distance
    elif post_type == 'large envelope':
        cost = .60 + .05 * distance
    elif post_type == 'package': 
        cost = 2.95 + .25 * distance
    elif post_type == 'large package':
        cost = 3.95 + .35 * distance
    return cost

main()