

import numpy as np
import random


def calculate_score(self_score1, self_score2, opponent_score, self_score):
    self_score = int(self_score)
    opponent_score = int(opponent_score)
    if self_score == self_score1:
        self_score1 = (opponent_score+self_score) % 10
        # print(f'用{opponent_score}加上了{self_score},得到了{self_score1}')
    elif self_score == self_score2:
        self_score2 = (opponent_score+self_score) % 10
        # print(f'用{opponent_score}加上了{self_score},得到了{self_score2}')
    return (self_score1, self_score2)


def randomchoice(state):
    oppoment_score1, oppoment_score2, player_score1, player_score2 = state
    choice_player = random.choice([player_score1, player_score2])
    choice_oppoment = random.choice([oppoment_score1, oppoment_score2])
    if choice_player == 0:
        choice_player = player_score1+player_score2
    if choice_oppoment == 0:
        choice_oppoment = oppoment_score1+oppoment_score2

    a, b = calculate_score(oppoment_score1, oppoment_score2,
                           choice_player, choice_oppoment)

    state = (a, b, player_score1, player_score2)
    # 判断胜负

    if a == 0 and b == 0:
        return ('你输了')

    if player_score1 == 0 and player_score2 == 0:
        return ('你赢了')

    if 0 in [a, b] and 0 in [player_score1, player_score2] and [a+b, player_score1+player_score2] in dead_list:
        return ('死循环')
    return (state)


dead_list = [[1, 3], [1, 8], [2, 1], [2, 6], [3, 4], [3, 9], [4, 2], [4, 7], [
    6, 3], [6, 8], [7, 1], [7, 6], [8, 4], [8, 9], [9, 2], [9, 7]]  # 死循环列表


def output(state):
    oppoment_score1, oppoment_score2, player_score1, player_score2 = state
    print("-"*10)
    print(f"{oppoment_score1:<9}{oppoment_score2}")
    print('\n')
    print(f"{player_score1:<9}{player_score2}")
    print("-"*10)


def perform_action(state, action):
    # 解包游戏状态
    opp_score1, opp_score2, player_score1, player_score2 = state

    # 4种动作
    if action == 0:
        player_choice = player_score1
        opponent_choice = opp_score1
    elif action == 1:
        player_choice = player_score1
        opponent_choice = opp_score2
    elif action == 2:
        player_choice = player_score2
        opponent_choice = opp_score1
    elif action == 3:
        player_choice = player_score2
        opponent_choice = opp_score2

    if player_choice == 0:
        player_choice = player_score1+player_score2
    if opponent_choice == 0:
        opponent_choice = opp_score1+opp_score2

    # 更新玩家得分
    player_score1, player_score2 = calculate_score(
        player_score1, player_score2, opponent_choice, player_choice)

    # 判断胜负
    if opp_score1 == 0 and opp_score2 == 0:
        return ('你输了')

    if player_score1 == 0 and player_score2 == 0:
        return ('你赢了')

    if 0 in [opp_score1, opp_score2] and 0 in [player_score1, player_score2] and [opp_score1+opp_score2, player_score1+player_score2] in dead_list:
        return ('死循环')
    return (opp_score1, opp_score2, player_score1, player_score2)


# 定义状态空间大小和动作空间大小
state_space_size = 10 * 10 * 10 * 10  # 对手两个数字和玩家两个数字的取值范围都是0-9
action_space_size = 4  # 四种动作

# 初始化Q表
Q = np.zeros((state_space_size, action_space_size))

# 定义超参数
alpha = 0.1  # 学习率
gamma = 0.9  # 折扣因子
epsilon = 0.1  # 探索率

# 定义状态转换函数


def state_transition(state, action):
    # 执行动作并返回新状态
    return perform_action(state, action)

# 定义奖励函数


def reward(state):
    if state == '你赢了':
        return 1
    elif state == '你输了':
        return -1
    elif state == '死循环':
        return -1  # 对死循环给予负奖励，以避免陷入死循环
    else:
        return 0

# 定义映射函数


def map_state_to_index(state):
    opp_score1, opp_score2, player_score1, player_score2 = state
    return opp_score1 * 1000 + opp_score2 * 100 + player_score1 * 10 + player_score2

# 训练AI


# 训练AI
num_episodes = 100000
for i in range(num_episodes):
    state = (np.random.randint(10), np.random.randint(10),
             np.random.randint(10), np.random.randint(10))  # 随机初始化状态
    print((i/num_episodes)*100, "%")  # 打印训练进度
    while True:
        # 使用ε-greedy策略选择动作
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.randint(action_space_size)  # 随机选择动作
        else:
            action = np.argmax(Q[map_state_to_index(state)])  # 选择Q值最大的动作

        # AI执行动作
        # print('AI', end="")
        new_state = state_transition(state, action)
        # 对手执行动作
        if new_state not in ['你赢了', '你输了', '死循环']:
            # print('对手', end="")

            new_state = randomchoice(new_state)
        r = reward(new_state)

        if new_state not in ['你赢了', '你输了', '死循环']:
            Q[map_state_to_index(state)][action] = Q[map_state_to_index(state)][action] + alpha * (
                r + gamma * np.max(Q[map_state_to_index(new_state)]) - Q[map_state_to_index(state)][action])

        # 更新状态
            state = new_state
            # output(state)

        # 如果游戏结束，跳出循环
        if new_state in ['你赢了', '你输了', '死循环']:
            break

# 训练完成后，可以使用Q表来选择最优策略
np.save('Q_table.npy', Q)


def choose_action(state):
    return np.argmax(Q[map_state_to_index(state)])


# 测试AI
AI_win = 0
Random_win = 0
Dead = 0
total = 0
while True:
    total+=1
    state = (1, 1, 1, 1)  # 初始状态
    #state = (np.random.randint(10), np.random.randint(10),np.random.randint(10), np.random.randint(10)) 
    while True:
    # AI执行动作
        action = choose_action(state)
        new_state = state_transition(state, action)
        # 对手执行动作
        if new_state not in ['你赢了', '你输了', '死循环']:
            new_state = randomchoice(new_state)
        # 判断胜负
        state = new_state
        if state == '你赢了':
            AI_win += 1
            break
        elif state == '你输了':
            Random_win += 1
            break
        elif state == '死循环':
            Dead += 1
            break
        state = new_state

    print(f"AI胜率{(AI_win/total)*100}%，随机胜率{(Random_win/total)*100}%，死循环率{(Dead/total)*100}%")
