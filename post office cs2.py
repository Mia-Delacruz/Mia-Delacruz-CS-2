def zip_code (zip):
    if zip > 1 and zip < 6999:
        return 1 
    elif zip > 7000 and zip < 19999 :
        return 2
    elif zip > 20000 and zip < 35999:
        return 3 
    elif zip > 36000 and zip < 62999:
        return 4 
    elif zip > 36000 and zip < 84999:
        return 5
    elif zip > 85000 and zip < 99999:
        return 6

def main (): 
    length = input ('what is your data')
    data = data.split(',')
    length = data [0]
    height = data [1]
    thickness = data [2]
    zip_1 = data [3]
    zip_2 = data [4]
    size_tracked = 0 
    print ('if variable length is'+ str(height))
    print ('if varibale height is'+ str(height))
    print ('if variable thickness'+ str(height))

    zip_from = zip_code(zip_1)
    print(zip_from)


main()
#if (3.5 <= length <= 4.25) (3.5 <= height <= 6) (.007 <= thickness <= .015):

