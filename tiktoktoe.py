import random
import os

class Player:
    def __init__(self, board):
        self.board = board
        self.icon = ''

    def choose_icon(self):
        choose_icon = ''
        while choose_icon != 1 and choose_icon != 2:
            choose_icon = int(input('Choose your icon (1->X, 2->O): '))
        
        if choose_icon == 1:
            choose_icon = 'X'
        else:
            choose_icon = 'O'

        self.icon = choose_icon

    def choose_case(self, possible_cases):
        case_choose = ''
        while case_choose not in possible_cases:
            case_choose = str(input('Choose a case: '))
        
        self.board[case_choose] = self.icon

    def update_board(self, new_board):
        self.board = new_board

class Robot:
    def __init__(self, board):
        self.board = board
        self.icon = ''

    def choose_icon(self, icon):
        if icon == 'X':
            self.icon = 'O'
        else:
            self.icon = 'X'
    
    def update_board(self, new_board):
        self.board = new_board
    
    def choose_case(self, possible_cases):
        case_choose = ''
        case_choose = random.choice(possible_cases)
        
        self.board[case_choose] = self.icon

class Tiktoktoe_game:
    def __init__(self):
        board = {}
        for i in range(1,4):
            for j in range(1,4):
                board[str(i)+str(j)] = ''
        self.board = board
        self.player = Player(self.board)
        self.robot = Robot(self.board)
    
    def print_board(self):
        print('')
        for case in self.board:
            if '1' == case[1]:
                print('----------')
                print(f'| {self.board[case]} ',end='')
            elif '2' == case[1]:
                print(f'| {self.board[case]} |',end='')
            else:
                print(f' {self.board[case]} |')
        print('----------')
        print('')

    def update_board(self, new_board):
        self.board = new_board

    def test_win(self, icon):
        status = 0
        row_1 = 0
        row_2 = 0
        row_3 = 0
        column_1 = 0
        column_2 = 0
        column_3 = 0
        diagonal_1 = 0
        diagonal_2 = 0
        for case in self.board:
            if '1' == case[0] and self.board[case] == icon:
                row_1 += 1
                if row_1 == 3:
                    status = 1
                    return status

            if '2' == case[0] and self.board[case] == icon:
                row_2 += 1
                if row_2 == 3:
                    status = 1
                    return status

            if '3' == case[0] and self.board[case] == icon:
                row_3 += 1
                if row_3 == 3:
                    status = 1
                    return status

            if '1' == case[1] and self.board[case] == icon:
                column_1 += 1
                if column_1 == 3:
                    status = 1
                    return status

            if '2' == case[1] and self.board[case] == icon:
                column_2 += 1
                if column_2 == 3:
                    status = 1
                    return status

            if '3' == case[1] and self.board[case] == icon:
                column_3 += 1
                if column_3 == 3:
                    status = 1
                    return status
            
            if case[0] == case[1] and self.board[case] == icon:
                diagonal_1 += 1
                if diagonal_1 == 3:
                    status = 1
                    return status
            
            if case[0] + case[1] == 4 and self.board[case] == icon:
                diagonal_2 += 1
                if diagonal_2 == 3:
                    status = 1
                    return status

    def print_possible_cases(self):
        possible_cases = [case for case in self.board if self.board[case] == '']
        print(possible_cases)
        return possible_cases
             
    def init_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.player.choose_icon()
        self.robot.choose_icon(self.player.icon)
        test_win = 0
        if random.randint(1,2) == 1:
            while test_win == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_board()
                possible_cases = self.print_possible_cases()
                self.player.choose_case(possible_cases)
                self.update_board(self.player.board)
                self.robot.update_board(self.player.board)
                os.system('cls' if os.name == 'nt' else 'clear')

                if self.test_win(self.player.icon) == 1:
                    return 'You win!'

                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_board()
                possible_cases = self.print_possible_cases()
                self.robot.choose_case(possible_cases)
                self.update_board(self.robot.board)
                self.player.update_board(self.robot.board)
                os.system('cls' if os.name == 'nt' else 'clear')

                if self.test_win(self.player.icon) == 1:
                    return 'You loose!'
        else:
            while test_win == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_board()
                possible_cases = self.print_possible_cases()
                self.robot.choose_case(possible_cases)
                self.update_board(self.robot.board)
                self.player.update_board(self.robot.board)
                os.system('cls' if os.name == 'nt' else 'clear')

                if self.test_win(self.player.icon) == 1:
                    return 'You loose!'

                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_board()
                possible_cases = self.print_possible_cases()
                self.player.choose_case(possible_cases)
                self.update_board(self.player.board)
                self.robot.update_board(self.player.board)
                os.system('cls' if os.name == 'nt' else 'clear')

                if self.test_win(self.player.icon) == 1:
                    return 'You win!'
        

game = Tiktoktoe_game()

print(game.init_game())








