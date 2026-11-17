# QuestForge - A Text Adventure Engine

rooms = {
    "village": {
        "description": "You are in a quiet village. A forest lies to the north.",
        "exits": {"north": "forest"}
    },
    "forest": {
        "description": "You are in a mysterious forest. A cave lies to the east.",
        "exits": {"south": "village", "east": "cave"}
    },
    "cave": {
        "description": "You found a hidden cave! A treasure chest sits in the center.",
        "exits": {"west": "forest"}
    }
}


def describe_room(location):
    """Return the description of the player's current room."""
    return rooms[location]["description"]


def move_player(location, direction):
    """Move the player if the requested exit exists."""
    exits = rooms[location]["exits"]

    if direction not in exits:
        return location, "You cannot go that way."

    new_location = exits[direction]
    return new_location, describe_room(new_location)


def play_game():
    """Start the QuestForge text adventure."""
    location = "village"

    print("Welcome to QuestForge!")
    print(describe_room(location))
    print("Type north, south, east, or west to move.")
    print("Type quit to leave the game.")

    while True:
        command = input("\nWhere would you like to go? ").lower().strip()

        if command == "quit":
            print("Thanks for playing QuestForge!")
            break

        location, message = move_player(location, command)
        print(message)

        if location == "cave":
            print("Congratulations! You discovered the hidden cave!")
            break
