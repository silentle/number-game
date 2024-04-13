import random
oppoment_score1, oppoment_score2 = 1, 1
player_score1, player_score2 = 1, 1
information = '''这是一个叫做"10的倍数游戏"的游戏。规则是两人轮流选择自己的一个数字,然后再选择对方的一个数字,将它们相加。
                如果某一方的两个数字都是10的倍数,那么这一方获胜。
                玩家通过巧妙地选择数字,目标是使自己获得10的倍数。
                10的倍数不可被选择'''
dead_list=[[1,3],[1,8],[2,1],[2,6],[3,4],[3,9],[4,2],[4,7],[6,3],[6,8],[7,1],[7,6],[8,4],[8,9],[9,2],[9,7]]#死循环列表

def output():
    print("-"*10)
    print(f"{oppoment_score1:<9}{oppoment_score2}")
    print('\n')
    print(f"{player_score1:<9}{player_score2}")
    print("-"*10)


def user_input():
    opponent_score = input('请输入要相加的对方数字')

    while opponent_score != str(oppoment_score1) and opponent_score != str(oppoment_score2) and opponent_score != '0':
        opponent_score = input('请重新输入对方数字')
    self_score = (input('请输入要相加的己方数字'))
    while self_score != str(player_score1) and self_score != str(player_score2) and self_score != '0':
        self_score = input('请重新输入己方数字')
    return (opponent_score, self_score)


def calculate_score(self_score1, self_score2, opponent_score, self_score):
    self_score = int(self_score)
    opponent_score = int(opponent_score)
    if self_score == self_score1:
        self_score1 = (opponent_score+self_score) % 10
        print(f'用{opponent_score}加上了{self_score},得到了{self_score1}')
    elif self_score == self_score2:
        self_score2 = (opponent_score+self_score) % 10
        print(f'用{opponent_score}加上了{self_score},得到了{self_score2}')
    return (self_score1, self_score2)


def choice():
    a, b = calculate_score(oppoment_score1, oppoment_score2, random.choice(
        [player_score1, player_score2]), random.choice([oppoment_score1, oppoment_score2]))
    return (a, b)


print(information)
while True:
    output()
    opponent_score, self_score = user_input()
    print('你', end="")

    player_score1, player_score2 = calculate_score(
        player_score1, player_score2, opponent_score, self_score)
    output()
    print('对手', end="")

    oppoment_score1, oppoment_score2 = choice()

    if oppoment_score1 == 0 and oppoment_score2 == 0:
        print('你输了')
        break
    if player_score1 == 0 and player_score2 == 0:
        print('你赢了')
        break
    if 0 in [oppoment_score1, oppoment_score2] and 0 in [player_score1, player_score2] and [oppoment_score1+oppoment_score2, player_score1+player_score2]in dead_list:
        print('死循环')
        break
