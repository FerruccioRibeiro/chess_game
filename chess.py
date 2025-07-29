import time
import os
# Desenhos
def print_chess_start_screen():
    print(r"""
               ██████████████
               █░░░░░░░░░░░░█
               █░░░░░░░░░░░░█
               █░░░░░░░░░░░░█
               ██████████████
                   ██  ██
                   ██  ██
                   ██  ██
               ██████████████
               █░░░░░░░░░░░░█
               █░░░░░░░░░░░░█
               █░░░░░░░░░░░░█
               █░░░░░░░░░░░░█
               █░░░░░░░░░░░░█
               ██████████████

            ╔════════════════════╗
            ║     CHESS GAME     ║
            ╚════════════════════╝

         Press Enter to initiate...
    """)
    input()

def print_game_over_screen(player_name):
    print(fr"""
               ██████████████
               █░░░░░░░░░░░░█
               █░░  ☠️   ☠️  ░░█
               █░░    ▄▄▄    ░░█
               █░░   ████   ░░█
               █░░   ▀▀▀▀   ░░█
               █░░░░░░░░░░░░░█
               ██████████████

           ╔════════════════════╗
           ║      YOU LOSE      ║
           ╚════════════════════╝

        Sorry, {player_name}. Better luck next time...
    """)

# Moviments
## Diagonal
def left_down(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    while (ord('a') <= ord(position[0]) - cont) and (1 <= int(position[1]) - cont):
        left_down = f'{chr(ord(position[0]) - cont)}{int(position[1]) - cont}'
        if ('W' == table[left_down][1] and color == 'B') or ('B' == table[left_down][1] and color == 'W'):
            eat_moviments.append(left_down)
            break
        elif ('   ' in table[left_down]):
            free_moviments.append(left_down)
            if more_t_one == False:
                break
        else:
            break
        cont += 1
    
    return eat_moviments, free_moviments

def right_down(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    while (ord('h') >= ord(position[0]) + cont) and (1 <= int(position[1]) - cont):
        right_down = f'{chr(ord(position[0]) + cont)}{int(position[1]) - cont}'
        if ('W' == table[right_down][1] and color == 'B') or ('B' == table[right_down][1] and color == 'W'):
            eat_moviments.append(right_down)
            break
        elif ('   ' in table[right_down]):
            free_moviments.append(right_down)
            if more_t_one == False:
                break
        else:
            break
        cont += 1
    
    return eat_moviments, free_moviments

def left_up(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    while (ord('a') <= ord(position[0]) - cont) and (8 >= int(position[1]) + cont):
        left_up = f'{chr(ord(position[0]) - cont)}{int(position[1]) + cont}'
        if('B' == table[left_up][1] and color == 'W') or ('W' == table[left_up][1] and color == 'B'):
            eat_moviments.append(left_up)
            break
        elif ('   ' in table[left_up]):
            free_moviments.append(left_up)
            if more_t_one == False:
                break
        else:
            break
        cont += 1

    return eat_moviments, free_moviments

def right_up(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    while (ord('h') >= ord(position[0]) + cont) and (8 >= int(position[1]) + cont):
        right_up = f'{chr(ord(position[0]) + cont)}{int(position[1]) + cont}'
        if ('B' == table[right_up][1] and color == 'W') or ('W' == table[right_up][1] and color == 'B'):
            eat_moviments.append(right_up)
            break
        elif ('   ' in table[right_up]):
            free_moviments.append(right_up)
            if more_t_one == False:
                break
        else:
            break
        cont += 1

    return eat_moviments, free_moviments

## Up or down
def down(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()    
    while (1 <= int(position[1]) - cont): 
        down = f'{chr(ord(position[0]))}{int(position[1]) - cont}'
        if table[down] == '   ':
            free_moviments.append(down)
            if more_t_one == False:
                break
        elif ('B' == table[down][1] and color == 'W') or ('W' == table[down][1] and color == 'B'):
            eat_moviments.append(down)
            break
        else:
            break
        cont += 1
    
    return eat_moviments, free_moviments

def up(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    while (8 >= int(position[1]) + cont):
        up = f'{chr(ord(position[0]))}{int(position[1]) + cont}'
        if table[up] == '   ':
            free_moviments.append(up)
            if more_t_one == False:
                break
        elif ('B' == table[up][1] and color == 'W') or ('W' == table[up][1] and color == 'B'):
            eat_moviments.append(up)
            break
        else:
            break
        cont += 1

    return eat_moviments, free_moviments

# Left and right
def left(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    while (ord('a') <= ord(position[0]) - cont):
        left = f'{chr(ord(position[0]) - cont )}{int(position[1])}'
        if table[left] == '   ':
            free_moviments.append(left)
            if more_t_one == False:
                break
        elif ('B' == table[left][1] and color == 'W') or ('W' == table[left][1] and color == 'B'):
            eat_moviments.append(left)
            break
        else:
            break
        cont += 1

    return eat_moviments, free_moviments

def right(position, table, color, cont, eat_list, free_list, more_t_one = False):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    while (ord('h') >= ord(position[0]) + cont):
        right = f'{chr(ord(position[0]) + cont)}{int(position[1])}'
        if table[right] == '   ':
            free_moviments.append(right)
            if more_t_one == False:
                break
        elif ('B' == table[right][1]  and color == 'W') or ('W' == table[right][1]  and color == 'B'):
            eat_moviments.append(right)
            break
        else:
            break
        cont += 1

    return eat_moviments, free_moviments

# L moviment
def l_moviment_up_left(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('a') <= ord(position[0]) - 1) and (8 >= int(position[1]) + 2):
        l_moviment_up_left = f'{chr(ord(position[0]) - 1)}{int(position[1]) + 2}'
        if table[l_moviment_up_left] == '   ':
            free_moviments.append(l_moviment_up_left)
        elif ('B' == table[l_moviment_up_left][1] and color == 'W') or ('W' == table[l_moviment_up_left][1] and color == 'B'):
            eat_moviments.append(l_moviment_up_left)

    return eat_moviments, free_moviments

def l_moviment_up_right(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('h') >= ord(position[0]) + 1) and (8 >= int(position[1]) + 2):
        l_moviment_up_right = f'{chr(ord(position[0]) + 1)}{int(position[1]) + 2}'
        if table[l_moviment_up_right] == '   ':
            free_moviments.append(l_moviment_up_right)
        elif ('B' == table[l_moviment_up_right][1] and color == 'W') or ('W' == table[l_moviment_up_right][1] and color == 'B'):
            eat_moviments.append(l_moviment_up_right)
    
    return eat_moviments, free_moviments

def l_moviment_right_up(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('h') >= ord(position[0]) + 2) and (8 >= int(position[1]) + 1):
        l_moviment_right_up = f'{chr(ord(position[0]) + 2)}{int(position[1]) + 1}'
        if table[l_moviment_right_up] == '   ':
            free_moviments.append(l_moviment_right_up)
        elif ('B' == table[l_moviment_right_up][1] and color == 'W') or ('W' == table[l_moviment_right_up][1] and color == 'B'):
            eat_moviments.append(l_moviment_right_up)

    return eat_moviments, free_moviments

def l_moviment_right_down(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('h') >= ord(position[0]) + 2) and (1 <= int(position[1]) - 1):
        l_moviment_right_down = f'{chr(ord(position[0]) + 2)}{int(position[1]) - 1}'
        if table[l_moviment_right_down] == '   ':
            free_moviments.append(l_moviment_right_down)
        elif ('B' == table[l_moviment_right_down][1] and color == 'W') or ('W' == table[l_moviment_right_down][1] and color == 'B'):
            eat_moviments.append(l_moviment_right_down)

    return eat_moviments, free_moviments

def l_moviment_down_right(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('h') >= ord(position[0]) + 1) and (1 <= int(position[1]) - 2):
        l_moviment_down_right = f'{chr(ord(position[0]) + 1)}{int(position[1]) - 2}'
        if table[l_moviment_down_right] == '   ':
            free_moviments.append(l_moviment_down_right)
        elif ('B' == table[l_moviment_down_right][1] and color == 'W') or ('W' == table[l_moviment_down_right][1] and color == 'B'):
            eat_moviments.append(l_moviment_down_right)

    return eat_moviments, free_moviments

def l_moviment_down_left(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('a') <= ord(position[0]) - 1) and (1 <= int(position[1]) - 2):
        l_moviment_down_left = f'{chr(ord(position[0]) - 1)}{int(position[1]) - 2}'
        if table[l_moviment_down_left] == '   ':
            free_moviments.append(l_moviment_down_left)
        elif ('B' == table[l_moviment_down_left][1] and color == 'W') or ('W' == table[l_moviment_down_left][1] and color == 'B'):
            eat_moviments.append(l_moviment_down_left)

    return eat_moviments, free_moviments

def l_moviment_left_down(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('a') <= ord(position[0]) - 2) and (1 <= int(position[1]) - 1):
        l_moviment_left_down = f'{chr(ord(position[0]) - 2)}{int(position[1]) - 1}'
        if table[l_moviment_left_down] == '   ':
            free_moviments.append(l_moviment_left_down)
        elif ('B' == table[l_moviment_left_down][1] and color == 'W') or ('W' == table[l_moviment_left_down][1] and color == 'B'):
            eat_moviments.append(l_moviment_left_down)

    return eat_moviments, free_moviments

def l_moviment_left_up(position, table, color, eat_list, free_list):
    eat_moviments = eat_list.copy()
    free_moviments = free_list.copy()
    if (ord('a') <= ord(position[0]) - 2) and (8 >= int(position[1]) + 1):
        l_moviment_left_up = f'{chr(ord(position[0]) - 2)}{int(position[1]) + 1}'
        if table[l_moviment_left_up] == '   ':
            free_moviments.append(l_moviment_left_up)
        elif ('B' == table[l_moviment_left_up][1] and color == 'W') or ('W' == table[l_moviment_left_up][1] and color == 'B'):
            eat_moviments.append(l_moviment_left_up)

    return eat_moviments, free_moviments

# Piece object
class Piece:
    def __init__(self, table, color, number):
        self.type = '' # K -> king, Q -> queen, T -> tower, B -> bishop, H -> horse, P -> pawn
        self.color = color # B -> black, W -> white
        self.number = number
        
        self.table = table
        self.position = ''

    def list_moviments(self):
        self.free_moviments = []
        self.eat_moviments = []

        # Restart variables
        self.cont = 1

    def do_moviment(self, new_position):
        if self.position != '':
            self.table[self.position] = '   '
        self.position = new_position
        self.table[new_position] = self.name

    def update_board(self, new_table):
        self.table = new_table

# Pawn object
class Pawn(Piece):
    def __init__(self, table, color, number):
        Piece.__init__(self, table, color, number)
        self.type = 'P'
        self.name = self.type+self.color+str(self.number)
        if self.color == 'B':
            self.position = chr(96 + self.number)+'7'
        else:
            self.position = chr(96 + self.number)+'2'
        
        self.table[self.position] = self.name

    def list_moviments(self):
        Piece.list_moviments(self)
        # Eat pieces in diagonal
        if self.color ==  'B':
            self.eat_moviments, _= left_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
            self.eat_moviments, _= right_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
            if '7' in self.position:
                _, self.free_moviments = down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
                if len(self.free_moviments) != 0:
                    _, self.free_moviments = down(self.free_moviments[0], self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
            else:
                _, self.free_moviments = down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
        
        else:
            self.eat_moviments, _= left_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
            self.eat_moviments, _= right_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
            if '2' in self.position:
                _, self.free_moviments = up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
                if len(self.free_moviments) != 0:
                    _, self.free_moviments = up(self.free_moviments[0], self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
            else:
                _, self.free_moviments = up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)

        return self.eat_moviments, self.free_moviments
    
    def became_another_piece(self):
        choose = ''
        while choose not in ['Q', 'T', 'B', 'H']:
            choose = str(input('Which piece do you want to became? (Q -> queen, T -> tower, B -> bishop, H -> horse)'))
        max_number = 0
        for x in list(self.table.values()):
            if choose in x:
                if max_number < int(x[2]):
                    max_number = int(x[2])       
        self.number = max_number+1

        if choose == 'Q':
            self.__class__ = Queen
            self.type = choose
            self.name = self.type+self.color+str(self.number)
        elif choose == 'T':
            self.__class__ = Tower
            self.type = choose
            self.name = self.type+self.color+str(self.number)
        elif choose == 'B':
            self.__class__ = Bishop
            self.type = choose
            self.name = self.type+self.color+str(self.number)
        elif choose == 'H':
            self.__class__ = Horse
            self.type = choose
            self.name = self.type+self.color+str(self.number)

# King object
class King(Piece):
    def __init__(self, table, color, number=1):
        Piece.__init__(self, table, color, number)
        self.type = 'K'
        self.number = number
        self.name = self.type+self.color+str(self.number)
        if self.color == 'B':
            self.position = chr(96 + 5)+'8'
        else:
            self.position = chr(96 + 5)+'1'
        
        self.table[self.position] = self.name

    def list_moviments(self):
        Piece.list_moviments(self)
        
        # Diagonal
        self.eat_moviments, self.free_moviments = left_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = right_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = left_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = right_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
        
        # Up or down
        self.eat_moviments, self.free_moviments = up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)

        # Left or right
        self.eat_moviments, self.free_moviments = left(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = right(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments)

        return self.eat_moviments, self.free_moviments    
    
# Queen object
class Queen(Piece):
    def __init__(self, table, color, number=1):
        Piece.__init__(self, table, color, number)
        self.type = 'Q'
        self.number = number
        self.name = self.type+self.color+str(self.number)
        if self.color == 'B':
            self.position = chr(96 + 4)+'8'
        else:
            self.position = chr(96 + 4)+'1'

        self.table[self.position] = self.name

    def list_moviments(self):
        Piece.list_moviments(self)
        
        # Diagonal
        self.eat_moviments, self.free_moviments = left_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = right_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = left_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = right_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        
        # Up or down
        self.cont = 1
        self.eat_moviments, self.free_moviments = up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)

        # Left and right
        self.cont = 1
        self.eat_moviments, self.free_moviments = left(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = right(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)

        return self.eat_moviments, self.free_moviments  

# Tower object
class Tower(Piece):
    def __init__(self, table, color, number=1):
        Piece.__init__(self, table, color, number)
        self.type = 'T'
        self.number = number
        self.name = self.type+self.color+str(self.number)
        if self.number == 1:
            cases = 1
        else:
            cases = 8
        if self.color == 'B':
            self.position = chr(96+cases)+'8'
        else:
            self.position = chr(96+cases)+'1'

        self.table[self.position] = self.name

    def list_moviments(self):
        Piece.list_moviments(self)
        
         # Up or down
        self.cont = 1
        self.eat_moviments, self.free_moviments = up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)

        # Left and right
        self.cont = 1
        self.eat_moviments, self.free_moviments = left(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = right(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)

        return self.eat_moviments, self.free_moviments  

# Bishop object
class Bishop(Piece):
    def __init__(self, table, color, number=1):
        Piece.__init__(self, table, color, number)
        self.type = 'B'
        self.number = number
        self.name = self.type+self.color+str(self.number)
        if self.number == 1:
            cases = 3
        else:
            cases = 6
        if self.color == 'B':
            self.position = chr(96+cases)+'8'
        else:
            self.position = chr(96+cases)+'1'

        self.table[self.position] = self.name

    def list_moviments(self):
        Piece.list_moviments(self)
        
        # Diagonal
        self.eat_moviments, self.free_moviments = left_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = right_down(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = left_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)
        self.cont = 1
        self.eat_moviments, self.free_moviments = right_up(self.position, self.table, self.color, self.cont, self.eat_moviments, self.free_moviments, more_t_one = True)

        return self.eat_moviments, self.free_moviments  

# Horse object
class Horse(Piece):
    def __init__(self, table, color, number=1):
        Piece.__init__(self, table, color, number)
        self.type = 'H'
        self.number = number
        self.name = self.type+self.color+str(self.number)
        if self.number == 1:
            cases = 2
        else:
            cases = 7
        if self.color == 'B':
            self.position = chr(96+cases)+'8'
        else:
            self.position = chr(96+cases)+'1'

        self.table[self.position] = self.name

    def list_moviments(self):
        Piece.list_moviments(self)
        
        self.eat_moviments, self.free_moviments = l_moviment_up_left(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = l_moviment_up_right(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = l_moviment_right_up(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = l_moviment_right_down(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = l_moviment_down_right(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = l_moviment_down_left(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = l_moviment_left_down(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)
        self.eat_moviments, self.free_moviments = l_moviment_left_up(self.position, self.table, self.color, self.eat_moviments, self.free_moviments)

        return self.eat_moviments, self.free_moviments  

# Player
class Player:
    def __init__(self, number, color):
        self.name = 'player_' + str(number)
        self.color = color
        self.round = 1
        self.list_pieces = []

    def update_round(self, round):
        self.round = round

# Game
class Game:
    def __init__(self):
        letras = list('abcdefgh')
        numeros = list(range(1,9))
        numeros.reverse()
        position = [f'{i}{j}' for j in numeros for i in letras]
        self.table = {pos: '   ' for pos in position}

        self.rodada = 1
        self.player_1 = Player(1,'B')
        self.player_2 = Player(2, 'W')
        self.pawns = {}
        for color in ['B', 'W']:
            for i in range(1,9):
                self.pawns[color+str(i)] = Pawn(self.table, color, i)
                self.update_board(self.pawns[color+str(i)].table)
        
        self.kings = {}
        for color in ['B', 'W']:
            self.kings[color+str(1)] = King(self.table, color, 1)
            self.update_board(self.kings[color+str(1)].table)

        self.queens = {}
        for color in ['B', 'W']:
            self.queens[color+str(1)] = Queen(self.table, color, 1)
            self.update_board(self.queens[color+str(1)].table)

        self.bishops = {}
        for color in ['B', 'W']:
            for i in range(1,3):
                self.bishops[color+str(i)] = Bishop(self.table, color, i)
                self.update_board(self.bishops[color+str(i)].table)

        self.towers = {}
        for color in ['B', 'W']:
            for i in range(1,3):
                self.towers[color+str(i)] = Tower(self.table, color, i)
                self.update_board(self.towers[color+str(i)].table)

        self.horses = {}
        for color in ['B', 'W']:
            for i in range(1,3):
                self.horses[color+str(i)] = Horse(self.table, color, i)
                self.update_board(self.horses[color+str(i)].table)

    def print_board(self):
        print('===============================================================')
        for pos in self.table:
            if 'a' in pos:
                if self.table[pos] == pos:
                    print('||   ', end='     ')
                else:
                    print(f'||{self.table[pos]}', end='     ')
            elif 'h' in pos:
                if self.table[pos] == pos:
                    print('   ||')
                else:
                    print(f'{self.table[pos]}||')
            else:
                if self.table[pos] == pos:
                    print('   ', end='     ')
                else:
                    print(f'{self.table[pos]}', end='     ')
        print('===============================================================')
    
    def print_moviments(self, eat_moviments, free_moviments):
        print('===============================================================')
        for pos in self.table:
            if 'a' in pos:
                if pos not in eat_moviments and pos not in free_moviments:
                    print('||   ', end='     ')
                elif pos in eat_moviments:
                    print(f'|| E ', end='     ')
                else:
                    print(f'|| F ', end='     ')
            elif 'h' in pos:
                if pos not in eat_moviments and pos not in free_moviments:
                    print('   ||')
                elif pos in eat_moviments:
                    print(f' E ||')
                else:
                    print(f' F ||')
            else:
                if pos not in eat_moviments and pos not in free_moviments:
                    print('   ', end='     ')
                elif pos in eat_moviments:
                    print(f' E ', end='     ')
                else:
                    print(f' F ', end='     ')
        print('===============================================================')
    
    def update_board(self, new_table):
        self.table = new_table

    def update_pieces_board(self, new_table):
        list_pieces = [self.kings, self.queens, self.towers, self.bishops, self.horses, self.pawns]
        for list_specific_pieces in list_pieces:
            for piece in list_specific_pieces:
                list_specific_pieces[piece].update_board(new_table)

    def check(self, not_this = None):
        list_pieces = [self.queens, self.towers, self.bishops, self.horses, self.pawns]
        for list_specific_pieces in list_pieces:
            for piece in list_specific_pieces:
                if not_this == None or not_this != list_specific_pieces[piece].name:
                    eat_list, _= list_specific_pieces[piece].list_moviments()
                    for case in eat_list:
                        if 'K' in self.table[case]:
                            return [list_specific_pieces[piece].name, self.table[case]]
        return [None,'']

    def check_mate(self):
        aux_list_eat = []
        aux_list_free = []
        possible_scape_eat = {}
        possible_scape_free = {}
        atacker, king_check = self.check()

        if king_check != '':
            list_pieces = [self.kings, self.queens, self.towers, self.bishops, self.horses, self.pawns]
            for list_specific_pieces in list_pieces:
                for piece in list_specific_pieces:
                    if list_specific_pieces[piece].color == king_check[1]:
                        aux_position = list_specific_pieces[piece].position
                        eat_list, free_list = list_specific_pieces[piece].list_moviments()
                        
                        for mov in eat_list:
                            aux_peca = self.table[mov]
                            if aux_peca == atacker:
                                not_this = atacker
                            else:
                                not_this = None
                            list_specific_pieces[piece].do_moviment(mov)
                            self.update_board(list_specific_pieces[piece].table)
                            self.update_pieces_board(list_specific_pieces[piece].table)
                            if self.check(not_this=not_this)[1] == '':
                                aux_list_eat.append(mov)
                            
                            list_specific_pieces[piece].do_moviment(aux_position)
                            self.table[mov] = aux_peca
                            self.update_board(list_specific_pieces[piece].table)
                            self.update_pieces_board(list_specific_pieces[piece].table)


                        for mov in free_list:
                            list_specific_pieces[piece].do_moviment(mov)
                            self.update_board(list_specific_pieces[piece].table)
                            self.update_pieces_board(list_specific_pieces[piece].table)
                            if self.check()[1] == '':
                                aux_list_free.append(mov)

                            list_specific_pieces[piece].do_moviment(aux_position)
                            self.update_board(list_specific_pieces[piece].table)
                            self.update_pieces_board(list_specific_pieces[piece].table)
                        
                        possible_scape_eat[list_specific_pieces[piece].name] = aux_list_eat.copy()
                        possible_scape_free[list_specific_pieces[piece].name] = aux_list_free.copy()
                        aux_list_eat.clear()
                        aux_list_free.clear()

        return possible_scape_eat, possible_scape_free

    def round(self, player):
        print(f'Player: {player.name}, color: {player.color}')
        choose_moviment = ''
        _, king_check = self.check()
        list_pieces = [self.kings, self.queens, self.towers, self.bishops, self.horses, self.pawns]
        while choose_moviment == '':
            if king_check != '':
                choose_piece = ''
                scape_eat_list, scape_free_list = self.check_mate()
                for piece in scape_eat_list.keys():
                    if len(scape_eat_list[piece]) != 0 or len(scape_free_list[piece]) != 0:
                        check_mate = False
                        break
                    else:
                        check_mate = True
                if check_mate:
                    return king_check
                for piece in scape_eat_list.keys():
                    if (len(scape_eat_list[piece]) != 0 or len(scape_free_list[piece]) != 0):
                        self.print_board()
                        self.print_moviments(scape_eat_list[piece], scape_free_list[piece])
                        print(f'Piece: {piece}')
                        print(f'Eat  cases: {scape_eat_list[piece]}')
                        print(f'Free cases: {scape_free_list[piece]}')
                    
                while choose_piece not in scape_eat_list.keys():
                    choose_piece = input('Choose a piece: ')

                while choose_moviment not in scape_eat_list[choose_piece] and choose_moviment not in scape_free_list[choose_piece]:
                    choose_moviment = input('Choose a moviment: ')

                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Player: {player.name}, color: {player.color}')
                if choose_moviment in scape_eat_list[choose_piece]:
                    for specific_list_pieces in list_pieces:
                        if specific_list_pieces[list(specific_list_pieces.keys())[0]].type == self.table[choose_moviment][0]:
                            specific_list_pieces.pop(self.table[choose_moviment][1:3])
                    player.list_pieces.append(self.table[choose_moviment])
                
                found = False
                for list_specific_pieces in list_pieces:
                    for piece in list_specific_pieces:
                        if list_specific_pieces[piece].name == choose_piece:
                            list_specific_pieces[piece].do_moviment(choose_moviment)
                            self.update_board(list_specific_pieces[piece].table)
                            self.update_pieces_board(self.table)
                            self.print_board()
                            found = True
                            break 
                    if found:
                        break

            else:   
                choose_piece = ''
                correct_color = False
                while choose_piece not in list(self.table.values()) or correct_color == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'Player: {player.name}, color: {player.color}')
                    self.print_board()
                    time.sleep(1)
                    choose_piece = input('Choose your piece in table: ')
                    if choose_piece[1] == player.color:
                        correct_color = True
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Player: {player.name}, color: {player.color}')
                for list_specific_pieces in list_pieces:
                    if list_specific_pieces[list(list_specific_pieces.keys())[0]].type == choose_piece[0]:
                        for piece in list_specific_pieces:
                            if list_specific_pieces[piece].name == choose_piece:
                                eat_list, free_list = list_specific_pieces[piece].list_moviments()
                                time.sleep(1)
                                if len(eat_list) == 0 and len(free_list) == 0:
                                    print('No moviments avaible')
                                    time.sleep(1)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f'Player: {player.name}, color: {player.color}')
                                else:
                                    while choose_moviment not in eat_list and choose_moviment not in free_list:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(f'Player: {player.name}, color: {player.color}')
                                        self.print_board()
                                        self.print_moviments(eat_list, free_list)
                                        print(f'Eat  cases: {eat_list}')
                                        print(f'Free cases: {free_list}')
                                        time.sleep(1)
                                        choose_moviment = input('Choose a moviment: ')

                                    time.sleep(1)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f'Player: {player.name}, color: {player.color}')
                                    if choose_moviment in eat_list:
                                        for specific_list_pieces in list_pieces:
                                            if specific_list_pieces[list(specific_list_pieces.keys())[0]].type == self.table[choose_moviment][0]:
                                                specific_list_pieces.pop(self.table[choose_moviment][1:3])

                                        player.list_pieces.append(self.table[choose_moviment])
                                    list_specific_pieces[piece].do_moviment(choose_moviment)
                                    break
                            self.update_board(list_specific_pieces[piece].table) 
                        break
        self.update_pieces_board(self.table)
              
    def init_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_chess_start_screen()

        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            end_point = ''
            end_point = self.round(self.player_1)
            if end_point != '' and end_point != None:
                break

            os.system('cls' if os.name == 'nt' else 'clear')
            
            end_point = self.round(self.player_2)
            if end_point != '' and end_point != None:
                break

        self.print_board()
        players = [self.player_1, self.player_2]
        for player in players:
            if player.color == end_point[1]:
                looser = player.name
                break
        print_game_over_screen(looser)
 
game = Game()
game.init_game()


