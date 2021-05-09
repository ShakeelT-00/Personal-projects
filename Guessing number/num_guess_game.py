import random


class guess_num_game:

    def __init__(self, in_num1, in_num2):
        self.first_num = in_num1
        self.second_num = in_num2
        self.guess_num = random.randint(self.first_num, self.second_num)

    def get_guess_num(self):
        return self.guess_num

    def set_first_num(self, in_num1):
        self.first_num = in_num1

    def set_second_num(self, in_num2):
        self.second_num = in_num2

    def get_first_num(self):
        return self.first_num

    def get_second_num(self):
        return self.second_num
