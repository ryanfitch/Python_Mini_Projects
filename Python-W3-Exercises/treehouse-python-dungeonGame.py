import random

def generate_cells( x, y ):
  cells = []
  for i in list(range(x)):
    for j in list(range(y)):
      cells.append((i, j))
  return cells

CELLS = generate_cells( 3, 3 )

def draw_map( player ):
  print(' _ _ _')
  title = '|{}'

  for idx, cell in enumerate( CELLS ):
    if idx in [0, 1, 3, 4, 6, 7]:
      if cell == player:
        print( title.format( 'X' ), end='' )
      elif cell in history:
        print( title.format( '.' ), end='' )
      else:
        print( title.format( '_' ), end='' )
    else:
      if cell == player:
        print( title.format( 'X|') )
      elif cell in history:
        print( title.format( '.|') )
      else:
        print( title.format( '_|' ) )


def get_locations():
  #monster = random location
  # door = random location
  # start = random location
  # if monster, door, or start are same, pick something else
  # return monster, door, start
  n = 0
  start_locs = []
  cellscpy = CELLS[:]
  a_cell = ()
  while n < 3:
    a_cell = random.choice( cellscpy )
    cellscpy.remove( a_cell )
    start_locs.append( a_cell )
    n += 1
  return tuple(start_locs)

def move_player( player, move ):
  # get player's current loc
  # if move is LEFT, y -1
  # if move is RIGHT y +1
  # if move is UP x - 1
  # if move is DOWN x + 1
  x, y = player
  if move in get_moves( player ):
    if move == 'LEFT':
      y = y - 1
    elif move == 'RIGHT':
      y = y + 1
    elif move == 'UP':
      x = x - 1
    elif move == 'DOWN':
      x = x + 1
    player = x, y
  else:
    print('Not a valid move.')
  return player


def get_moves( player ):
  MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # if player's y is 0, remove LEFT
  # if player's x is 0, remove UP
  # if player's y is 2, remove RIGHT
  # if player's x is 2, remove DOWN
  x, y = player
  if x == 0:
    MOVES.remove('UP')
  if x == 2:
    MOVES.remove('DOWN')
  if y == 0:
    MOVES.remove('LEFT')
  if y == 2:
    MOVES.remove('RIGHT')
  return MOVES

monster, door, start = get_locations()
history = []
history. append( start )
player = start

while True:
  print("Welcome to the dungeon!")
  print("You're currently in room {}".format( player ) ) # fill with player pos
  draw_map( player )
  print("You can move {}". format( get_moves( player ) ) ) # fill with available moves
  print("Enter QUIT to quit")

  move = input("> ")
  move = move.upper()

  if move == 'QUIT':
    break
  else:
    player = move_player( player, move )
    history.append( player )
    if player == door:
      print('Winner!')
      break
    if player == monster:
      print('You were eaten :(')
      break
  # if it's a good move, change player pos
  # if a bad move, alert player but do not change pos
  # if new player position is the door they win
  # if new player position is the monster they lose
  # otherwise continue