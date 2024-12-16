# Decision Making

print("""
You entering in a room with two door. You have a hen and cake.
Do you want to go through door 1 or door 2?""")

door = input("> ")

if door == "1":
    print("A leopard eating Aloo Parantha.")
    print("What do you do?")
    print("1. Take away the Parantha.")
    print("2. Tease the leopard.")

    leopard = input("> ")

    if leopard == "1":
        print("Leopard ate your hen and cake. Over!")
    elif leopard == "2":
        print("Leopard ate you. Over!")
    else:
        print(f"Nice choice {leopard}, Leopard ran away.")

elif door == "2":
    print("Your friends are celebrating new year.")
    print("What do you do?")
    print("1. Join them and cut the cake")
    print("2. Join them and cook the chicken")
    print("3. Leave them and celebrate alone")

    celebration = input ("> ")

    if celebration == "1" or celebration == "2":
        print("Your friends are thanking you for treat")
        print("After that you went to home")
    else:
        print("You cut the cake alone and left the hen in forest.")
        print("You went home and slept.")
else:
    print("You didn't entered through any door:) Smart Huh!!")