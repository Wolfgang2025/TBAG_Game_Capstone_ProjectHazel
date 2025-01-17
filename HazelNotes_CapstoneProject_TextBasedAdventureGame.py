# Hazel Capstone Project - Text Based Adventure Game

This project is a text-based adventure game developed as part of the Software Engineering with AI capstone project. The game will feature various interactive elements, including puzzles, quests, and character interactions, all driven by text commands.

## Features

- Interactive story with multiple endings
- Puzzles and quests to solve
- Character interactions and dialogue
- Inventory management

## Getting Started

To run the game, simply execute the `Hazel_CapstoneProject_TextBasedAdventureGame.py` file in your Python environment.

## Requirements

- Python 3.x

## How to Play

1. Start the game by running the script.
2. Follow the on-screen instructions to navigate through the game.
3. Use text commands to interact with the game world.

Enjoy your adventure!

## Note

This game is a work in progress. Future updates will include more quests, characters, and interactive elements. Stay tuned for more exciting features!

### **How to Approach Your Text-Based Adventure Game Project**
Breaking the project into smaller, manageable chunks is essential. Here’s a **step-by-step plan** for a 2-week timeline with daily tasks:

---

### **Day 1: Define the Game’s Scope**
1. **What the Game Will Do**:
   - Basic movement between rooms.
   - Descriptions of rooms and directions.
   - Player actions like `go`, `look`, and `take`.

2. **What It Won’t Do** (Optional Features):
   - No need for advanced AI or complex inventories yet.

3. **Create a Rough Plan**:
   - List the key components: Rooms, Player, Items, Game Engine.

---

### **Day 2-3: Build the Core Classes**
1. **Create a `Room` Class**:
   - Attributes: `name`, `description`, `connections` (e.g., `{'north': room2}`).
   - Methods: `connect_room()`, `get_description()`.

   ```python
   class Room:
       def __init__(self, name, description):
           self.name = name
           self.description = description
           self.connections = {}

       def connect_room(self, direction, room):
           self.connections[direction] = room

       def get_description(self):
           return f"{self.name}\n{self.description}"
   ```

2. **Create a `Player` Class**:
   - Attributes: `current_room`, `inventory`.
   - Methods: `move(direction)`, `look()`.

   ```python
   class Player:
       def __init__(self, starting_room):
           self.current_room = starting_room
           self.inventory = []

       def move(self, direction):
           if direction in self.current_room.connections:
               self.current_room = self.current_room.connections[direction]
               return f"You moved {direction}."
           else:
               return "You can't go that way."
   ```

---

### **Day 4-5: Create the Game World**
1. **Set Up Rooms**:
   - Create instances of the `Room` class and connect them.

   ```python
   # Example rooms
   cave = Room("Mysterious Cave", "You find yourself in a dimly lit cave...")
   library = Room("Ancient Library", "This room is filled with old, dusty bookshelves...")
   
   # Connect rooms
   cave.connect_room("north", library)
   library.connect_room("south", cave)
   ```

2. **Set Up the Player**:
   - Place the player in the starting room.
   ```python
   player = Player(cave)
   ```

---

### **Day 6-7: Implement Player Actions**
1. **Handle Commands**:
   - Create a function to process input like `go north`, `look`, or `take`.

   ```python
   def process_command(player, command):
       parts = command.split()
       action = parts[0]
       
       if action == "go":
           if len(parts) > 1:
               direction = parts[1]
               return player.move(direction)
           else:
               return "Go where?"
       elif action == "look":
           return player.current_room.get_description()
       else:
           return "Unknown command."
   ```

2. **Test Basic Commands**:
   - Run a loop to test movement and descriptions.
   ```python
   while True:
       command = input("> ")
       print(process_command(player, command))
   ```

---

### **Day 8-9: Add Items**
1. **Create an `Item` Class**:
   - Attributes: `name`, `description`.
   - Methods: `__str__()`.

   ```python
   class Item:
       def __init__(self, name, description):
           self.name = name
           self.description = description

       def __str__(self):
           return f"{self.name}: {self.description}"
   ```

2. **Place Items in Rooms**:
   - Add an `items` attribute to `Room`.
   - Implement `take` and `drop` actions.

   ```python
   class Room:
       def __init__(self, name, description):
           self.name = name
           self.description = description
           self.connections = {}
           self.items = []

       def add_item(self, item):
           self.items.append(item)
   ```

   ```python
   def process_command(player, command):
       parts = command.split()
       action = parts[0]
       
       if action == "take":
           item_name = " ".join(parts[1:])
           for item in player.current_room.items:
               if item.name.lower() == item_name.lower():
                   player.inventory.append(item)
                   player.current_room.items.remove(item)
                   return f"You picked up {item.name}."
           return "Item not found."
       elif action == "inventory":
           return "You are carrying: " + ", ".join(str(item) for item in player.inventory)
   ```

---

### **Day 10-12: Add Challenges or Puzzles**
1. **Implement Conditional Room Access**:
   - For example, require a key to open a door.

   ```python
   class Room:
       def __init__(self, name, description, locked=False, key=None):
           self.name = name
           self.description = description
           self.connections = {}
           self.locked = locked
           self.key = key

       def unlock(self, item):
           if self.key and item.name == self.key:
               self.locked = False
               return "The room is now unlocked!"
           return "You can't unlock this room."
   ```

2. **Test Puzzles**:
   - Create a locked room and a key to solve it.

---

### **Day 13: Add Polish**
1. **Enhance Descriptions**:
   - Add dynamic descriptions based on player actions.
2. **Handle Errors Gracefully**:
   - Add messages for invalid commands or edge cases.

---

### **Day 14: Final Testing and Debugging**
1. **Play Through**:
   - Ensure all commands and transitions work as expected.
2. **Get Feedback**:
   - Ask peers or mentors to playtest your game.

---

### **Daily Breakdown**
| Day | Tasks                                                                 |
|-----|----------------------------------------------------------------------|
| 1   | Define scope and create a project plan.                              |
| 2-3 | Build core classes (`Room`, `Player`).                               |
| 4-5 | Create and connect rooms, initialize the player.                     |
| 6-7 | Implement basic player commands (`go`, `look`).                      |
| 8-9 | Add items, implement `take` and `inventory` commands.                |
| 10-12 | Add puzzles or challenges (e.g., locked doors, required items).    |
| 13  | Polish descriptions and handle errors.                              |
| 14  | Test, debug, and finalize.                                           |

---

### **Key Tips**
1. **Start Simple**: Focus on core mechanics before adding complexity.
2. **Test Daily**: Playtest your game frequently to ensure it works.
3. **Iterate**: Improve features after basic functionality is complete.
4. **Ask for Help**: Don’t hesitate to ask mentors or peers for advice.

This plan ensures you build the game step by step, without feeling overwhelmed! 😊
