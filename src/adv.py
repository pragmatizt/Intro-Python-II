from room import Room
from player import Player
from item import Item, Food, Egg, Ramen

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
rock = Item("rock", "This is a rock.")
sandwich = Food("sandwich", "This is a delicious sandwich.", 100)
egg = Egg()
ramen = Ramen()

# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name: "), room['outside'])
player.items.append(rock)
player.items.append(sandwich)
player.items.append(egg)
print(player.current_room)

player.eat(rock)
player.eat(sandwich)
player.eat(egg)
player.eat(ramen)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
valid_directions = ("n", "s", "e", "w")
while True:
    cmd = input("\n~~> ")
    if cmd == "q":
        print("Goodbye!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "i":
        player.print_inventory()
    else:
        print("I did not understand that command")