states = {
    "AP":"Andhra Pradesh",
    "AR":"Arunachal Pradesh",
    "AS":"Assam",
    "BR":"Bihar",
    "CH":"Chhattisgarh",
    "GA":"Goa",
    "GJ":"Gujarat",
    "HR":"Haryana",
    "HP":"Himachal Pradesh",
    "JH":"Jharkhand",
    "KA":"Karnataka",
    "KL":"Kerala",
    "MP":"Madhya Pradesh",
    "MH":"Maharashtra",
    "MN":"Manipur",
    "ML":"Meghalaya",
    "MZ":"Mizoram",
    "NL":"Nagaland",
    "OR":"Odisha",
    "PB":"Punjab",
    "RJ":"Rajasthan",
    "SK":"Sikkim",
    "TN":"Tamil Nadu",
    "TS":"Telangana",
    "TR":"Tripura",
    "UP":"Uttar Pradesh",
    "UK":"Uttarakhand",
    "WB":"West Bengal"
}

ut = {
    "AN":"Andaman and Nicobar Islands",
    "CG":"Chandigarh",
    "DNHDD":"Dadra and Nagar Haveli and Daman and Diu",
    "DL":"Delhi",
    "JK":"Jammu and Kashmir",
    "LA":"Ladakh",
    "LD":"Lakshadweep",
    "PY":"Puducherry",
}

cities = {
    "Hy": "Hyderabad",
    "No": "Noida",
    "Bg": "Bengaluru"
}

# add more cities
cities['Kr'] = "Karnataka",
cities['Chandigarh'] = "CG"

print(cities)

# print out some cities
print("-" * 100)
print("Karnataka state has: ", cities["Kr"])

# print out some states
print("-" * 100)
print("UK stands for: ", states["UK"])
print("TG stands for: ", states["TS"])

# use states then cities dictionary
print("-" * 100)
print("LPU is located in: ", ut[cities["Chandigarh"]])

# print every state name
print("-" * 100)
for abbr, state in list(states.items()):
    print(f"{abbr} stands for {state}")

# items method of dictionary
print("-" * 100)
print(cities.items())
# dict_items([('Hy', 'Hyderabad'), ('No', 'Noida'), ('Bg', 'Bengaluru'), ('Kr', ('Karnataka',)), ('Chandigarh', 'CG')])


