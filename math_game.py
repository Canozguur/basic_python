import random


class Game:

    def __init__(self):
        self.play = True
        self.score = 0
        self.wrong_answer = 0
        print("SELECT QUESTION TYPE\n1) Addition\n2) Subtraction\n3) Division\n4) Multiplication")
        self.question_type = int(input(""))
        self.question_num = 0
        while self.play:
            self.levels()
            print(f"Your New SCORE is {self.score}")

    def levels(self):
        if self.question_type == 1:
            x, y = self.questions_maker()
            self.answer = x + y
            self.ask_question(x, y, "+")

        elif self.question_type == 2:
            x, y = self.questions_maker()
            self.answer = x - y
            self.ask_question(x, y, "-")

        elif self.question_type == 3:
            x, y = self.questions_maker()
            self.answer = int(x / y)
            self.ask_question(x, y, "/")

        elif self.question_type == 4:
            x, y = self.questions_maker()
            self.answer = x * y
            self.ask_question(x, y, "*")

    def questions_maker(self):
        self.question_num+=1
        if self.question_num <= 5:
            x = random.randint(0, 25)
            y = random.randint(0, 25)
            self.score_point = 1
            return x, y

        elif self.question_num > 5 and self.question_num <= 10:
            x = random.randint(25, 100)
            y = random.randint(25, 100)
            self.score_point = 2
            return x, y
        elif self.question_num > 10 and self.question_num <= 15:
            x = random.randint(100, 200)
            y = random.randint(100, 200)
            self.score_point = 4
            return x, y
        else:
            self.play = False
            print(f"CONGRATULATIONS!!!\nYOUR SCORE IS {self.score}")
    def ask_question(self, x, y, type):
        print(f"{self.question_num}) {x} {str(type)} {y} = X")
        self.user_answer = int(input("What is the answer of X"))
        if self.user_answer == self.answer:
            self.score += self.score_point
        else:
            self.score -= 0.5
            self.wrong_answer += 1
            if self.wrong_answer == 3:
                print("TOO MANY WRONG ANSWER!!!")
                print(f"Your SCORE is {self.score}")
                self.play = False
            elif self.wrong_answer < 3:
                self.ask_question(x, y, type)


Game()
