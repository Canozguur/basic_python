import random

class RunTest:

    def __init__(self):
        self.memory = []
        for i in range(100000):
            map = self.random_game()  # This function is creating games
            if map == None :
                continue
            board, situation = self.check_game(map)
            if [board, situation] in self.memory :
                continue
            else:
                self.memory.append([board, situation])
        result = self.data_analyse(self.memory)
        print(result)
        for i in result['Games']:
            for j in i:
                print(*j)
            print(20*'*')

    def data_analyse(self,datas):

        situations = {'X':0,'O':0,'TIE':0,'Games':[]}
        timer = 0
        for data in datas:

            situation = data[1]

            if situation == 'X':
                situations['X'] += 1
                situations['Games'].append(data[0])
            if situation == 'O':
                situations['O'] += 1
                situations['Games'].append(data[0])
            if situation == 'TIE':
                situations['TIE'] += 1

            timer += 1

        return situations

    def check_game(self,data):
        print(data)
        board = data
        # data is just return data and second one returns winner
        if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
            print('1')
            return data, board[0][0]
        elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
            print('2')
            return data, board[1][0]
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
            print('3')
            return data, board[2][0]
        elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
            print('4')
            return data, board[0][0]
        elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
            print('5')
            return data, board[0][1]
        elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
            print('6')
            return data, board[0][2]
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            print('7')
            return data, board[0][0]
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            print('8')
            return data, board[0][2]
        else:
            return data, 'TIE'

    def random_game(self):
        board_game = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0],]


        for _ in range(100):
            memory = []
            total_X = 0
            total_O = 0
            num = 4
            for _ in range(num):
                num += 1
                selected = random.choice(['X', 'O'])
                x = random.choice([0, 1, 2])
                y = random.choice([0, 1, 2])
                for k in memory:
                    if k == [y, x]:
                        continue
                memory.append([y,x])
                board_game[y][x] = selected
            for j in board_game:
                for z in j:
                    if z == 'X':
                        total_X +=1
                    if z == 'O':
                        total_O += 1
            if total_X == total_O + 1 and self.check_game2(board_game) == True:
                return board_game

    def check_game2(self,map):
        board = map
        listt =[]
        if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
            print('1')
            one = board[0][0]
            listt.append(one)
        if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
            print('2')
            two = board[1][0]
            listt.append(two)

        if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
            print('3')
            three = board[2][0]
            listt.append(three)

        if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
            print('4')
            four = board[0][0]
            listt.append(four)

        if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
            print('5')
            five = board[0][1]
            listt.append(five)

        if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
            print('6')
            six = board[0][2]
            listt.append(six)
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            print('7')
            seven = board[0][0]
            listt.append(seven)
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            print('8')
            eight = board[0][2]
            listt.append(eight)

        else:
            nine= 'TIE'
            listt.append(nine)

        if len(listt) == 1:
            return True
        else:
            return False

RunTest()



