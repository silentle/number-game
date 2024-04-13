import random


class Player:
    def __init__(self, lefthand=1, righthand=1):
        self.lefthand = lefthand
        self.righthand = righthand

    def calculate_score(self, opponent_score, self_score):
        if self_score == self.lefthand:
            self.lefthand = (opponent_score + self_score) % 10
            print(f'用{opponent_score}加上了{self_score},得到了{self.lefthand}')
        elif self_score == self.righthand:
            self.righthand = (opponent_score + self_score) % 10
            print(f'用{opponent_score}加上了{self_score},得到了{self.righthand}')

    def get_lefthand(self):
        return self.lefthand

    def get_righthand(self):
        return self.righthand


def user_input(computer):
    opponent_score = input('请输入要相加的对方数字: ')

    while opponent_score not in [str(computer.get_lefthand()), str(computer.get_righthand()), '0']:
        if computer.get_lefthand() != 0:
            print(f'请重新输入对方数字，你只能输入{computer.get_lefthand()}')
            if computer.get_righthand() not in [computer.get_lefthand(), 0]:
                print(f'或{computer.get_righthand()}: ')
        else:
            print(f'请重新输入对方数字，你只能输入{computer.get_righthand()}: ')

        opponent_score = input()

    self_score = input('请输入要相加的己方数字: ')
    while self_score not in [str(user.get_lefthand()), str(user.get_righthand()), '0']:
        if user.get_lefthand() != 0:
            print(f'请重新输入己方数字，你只能输入{user.get_lefthand()}')
            if user.get_righthand() not in [user.get_lefthand(), 0]:
                print(f'或{user.get_righthand()}: ')
        else:
            print(f'请重新输入己方数字，你只能输入{user.get_righthand()}: ')
        self_score = input()

    return int(opponent_score), int(self_score)


def print_board(computer, user):#打印计分板
    print("-" * 10)
    print(f"{computer.get_lefthand():<9}{computer.get_righthand()}")
    print('\n')
    print(f"{user.get_lefthand():<9}{user.get_righthand()}")
    print("-" * 10)


def computer_choice(computer, user):#随机选择
    self_score = random.choice(
        [computer.get_lefthand(), computer.get_righthand()])
    opponent_score = random.choice([user.get_lefthand(), user.get_righthand()])
    computer.calculate_score(opponent_score, self_score)


information = '''这是一个叫做"10的倍数游戏"的游戏。规则是两人轮流选择自己的一个数字,然后再选择对方的一个数字,将它们相加。
如果某一方的两个数字相加的结果是10的倍数,那么这一方获胜。
玩家通过巧妙地选择数字,目标是使自己获得10的倍数。'''

print(information)

user = Player()
computer = Player()

print_board(computer, user)

while True:
    opponent_score, self_score = user_input(computer)
    print('你', end="")
    user.calculate_score(opponent_score, self_score)
    print_board(computer, user)

    if user.get_lefthand() == 0 and user.get_righthand() == 0:
        print('你赢了')
        break

    print('对手', end="")
    computer_choice(computer, user)
    print_board(computer, user)

    if computer.get_lefthand() == 0 and computer.get_righthand() == 0:
        print_board(computer, user)
        print('你输了')
        break
