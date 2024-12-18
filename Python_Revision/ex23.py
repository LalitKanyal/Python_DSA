# Lists example

ten_players = "Michael George Donald Xi Kim Angela Modi"

ten_players_list = ten_players.split(' ')

print(f"Wait! there are only {len(ten_players_list)} players, we need {11-len(ten_players_list)} more players, Let me add remaining {11-len(ten_players_list)} players")
reserved_players_list = ["Elon", "Georgia", "Kamala", "Joe", "Dustbin", "Rishi", "Putin", "Zelensky"]

# what if i use for loop
for x in ten_players_list:
    print(x)
# results 7 players

# while loop

while len(ten_players_list) !=11:
    next_player = reserved_players_list.pop()
    print(f"Next Player to be added in team is: {next_player}")
    ten_players_list.append(next_player)
    print(f"There are {len(ten_players)} players now.")

print(f"The complete list is: {ten_players_list}")

# find a string element in the list

if "modi" or "Modi" in ten_players_list:
    print(f"Captain is: Modi")
else:
    print("No captain selected right now!")

# find string element with index() method

try:
    captain = ten_players_list.index("Modi")
    print(f"Captain found at index: {captain}")
    print(f"Captain is: {ten_players_list[captain]}")
except ValueError:
    print("Not found!")

# make list a string

print(' '.join(ten_players_list))
print(', '.join(ten_players_list))

# sort ascending order
# look here >
print(ten_players_list.sort())
# returns None bacuase Python modifies the list in place (it does not create or return a new sorted list).
# remember The sort() method returns None.

ten_players_list.sort()
# this sort method returns None while sorting the original list we specified

print(ten_players_list)
# prints modified (sorted) list

# sort descending order
ten_players_list.reverse()
print(ten_players_list)