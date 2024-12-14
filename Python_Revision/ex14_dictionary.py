# Dictionaries

# Key/Value Structures

email = {
    "From": "mailfromgoogle@gmail.com",
    "To": "mailtoyou@gmail.com",
    "Subject": "Not amazing offer for you!!!!"
}

print(email["From"])
print(email["To"])
print(email["Subject"])

# Combine List with data objects

messages = [
    {"to": 'Ray', "from": 'Ben', "message": 'Hey!!'},
    {"to": 'Ben', "from": 'Ray', "message": 'Hi!!'},
    {"to": 'Max', "from": 'Muller', "message": 'Yo!!'},
    {"to": 'Muller', "from": 'Max', "message": 'What\s up!!'},
]

print(messages[0]['to'])
print(messages[1]['message'])