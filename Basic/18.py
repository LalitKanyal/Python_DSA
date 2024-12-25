'''
Prefix "Is" String Modifier

Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

'''

def string_checker(stringg):

    if len(stringg) >= 2 and stringg[:2] == "Is":
        return stringg
    
    else:
        return "Is " + stringg
        

print(string_checker("he sleeping?"))
print(string_checker("Is he coding?"))