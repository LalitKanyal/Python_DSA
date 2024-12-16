# If statement

people = 10
cats = 30

if people < cats:
    print("people are less then cats!")

if cats < people:
    print("Cats are less then people!")


from dis import dis

dis('''
    
people = 5
cats = 10
if people < cats:
    print("people are less then cats!")

''')