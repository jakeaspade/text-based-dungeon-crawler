## Text Monster Game
## The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.
stones = False
monster = False
choice = ''
# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 3 floors and 15 rooms total, though.
floor0 = ['empty', 'sword', 'stairs up', 'sword', 'sword']
floor1 = ['magic stones', 'monster', 'stairs down', 'sword', 'stairs up']
floor2 = ['prize', 'boss monster', 'monster', 'monster', 'stairs down']

# Items in the player's possession
inventory = []

# Player's current position in the dungeon
# The player starts in the first room on floor 0
currentFloor = 0
currentRoom = 0

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = 'ongoing'
print('If you dont know the commands, type "help"!')

while gameState == 'ongoing':
  # Describe the room the player is in
  if currentFloor == 0:
    floor = floor0
  elif currentFloor == 1:
    floor = floor1
  else:
    floor = floor2
  room = floor[currentRoom]
  if room == 'empty':
    print('You are in an empty room.')
  if room == 'stairs up':
    print('This room has stairs leading up.')
  if room == 'sword':
      print('There is a shiny sword in the middle of the room.')
  if room == 'monster':
    print('A monster blocks your path')
    monster = True  
  if room == 'stairs down':
    print('This room has stairs leading down.')
  if room == 'magic stones':
    print('This room illuminates with colorful stones floating in the middle.')
  if room == 'boss monster':
    print('A large broad purple man blocks your path!')
  if room == 'prize':
    print('A pile of gold awaits for you to take!')
    gameState = 'won'
    break
  # You need to handle describing the other cases..

  # Get command from the player
  choice = input('Command? ')

  # Respond to command
  if choice == 'help':
    print("right: go right")
    print("left: go left")
    print("up: if there are stairs going up, go up")
    print("down: if there are stairs going down, go down")
    print("grab: if there is something in the room, then grab it")
    print("fight: if there is a monster in the way, kill it (if you have a sword)")
    # Help: display all commands
    # Note that the "pass" keyword in Python is a placeholder for lines where the interpreter would normally expect to see code. If control flow reaches the line with "pass", the interpreter "passes" over the line (i.e. does nothing).
    pass
  elif choice == 'left':
    if room == 'monster':
      print('the monster stops you and kills you!')
      gameState = 'dead'
      break
    if currentRoom == 0:
      print('You cant go that way!')
    else:
      currentRoom -= 1
    # Player wants to move left
    pass
  elif choice == 'right':
    if room == 'monster':
      print('the monster stops you and kills you!')
      gameState = 'dead'
      break
    if currentRoom == 4:
      print('You cant go that way!')
    else:
      currentRoom += 1
    # Player wants to move right
    pass
  elif choice == 'up':
    if room == 'monster':
      print('the monster stops you and kills you!')
      gameState = 'dead'
      break
    if room == 'stairs up':
      currentFloor += 1
    else:
      print('there are no stairs going up here')
    # Player wants to go upstairs
    pass
  elif choice == 'down':
    if room == 'monster':
      print('the monster stops you and kills you!')
      gameState = 'dead'
      break
    if room == 'stairs down':
      currentFloor -= 1
    else:
      print('there are no stairs going down here')
    # Player wants to go downstairs
    pass
  elif choice == 'grab':
    if room == 'monster':
      print('the monster stops you and kills you!')
      gameState = 'dead'
      break
    elif len(inventory) == 3:
      print('You cannot hold anymore items!')
      pass
    else:
      if room == 'sword':
        inventory.append('sword')
        floor.pop(currentRoom)
        floor.insert(currentRoom, 'empty')
        if currentFloor == 0:
          floor0 = floor
        elif currentFloor == 1:
          floor1 = floor
        else:
          floor = floor2
      if room == 'magic stones':
        inventory.append('magic stones')
        print('You grabbed the stones!')
        floor.pop(currentRoom)
        floor.insert(currentRoom, 'empty')
        pass
       # Player wants to grab item from the room
  elif choice == 'fight':
    if room == 'monster' or room == 'boss monster':
      armed = False
      for item in inventory:
        if item == "sword":
          armed = True
      if armed == True:
        if room == 'boss monster':
          stones = False
          for item in inventory:
            if item == 'magic stones':
              stones = True
          if stones == True:
            print("Your sword becomes imbued with magical energy and smite the purple man in front of you!")
            floor2.pop(1)
            floor2.insert(1, 'empty')
          else:
            print("Your weapon seems to not effect the monster!  It kills you with one hit!")
            gameState = 'dead'
            break
        elif room == 'monster':
          print("You have slayed the monster!")
          p = 0
          for item in inventory:
            if item == 'sword':
              inventory.pop(p)
              break
            else:
              p += 1
          print('Your sword broke!')
          floor.pop(currentRoom)
          floor.insert(currentRoom, 'empty')
          if currentFloor == 0:
            floor0 = floor
          elif currentFloor == 1:
            floor1 = floor
          else:
            floor = floor2
        else:
          print('there is nothing to fight')
      else:
        print('You have been slayed!')
        gameState = 'dead'
        break
    else:
      print('There is nothing here to fight!')
  else:
    print('Command not recognized. Type "help" to see all commands.')

if gameState == 'won':
  print('You won the game! :)')
else:
  print('You lost the game. :( Maybe next time.')