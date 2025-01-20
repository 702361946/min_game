# Matching Game
# 黑白配
# 4P单人

import random
from datetime import datetime

type_dict = {
    0: '白',
    1: '黑'
}


class TYPE(object):
    def __init__(self, t_type: int = 0, score: int = 0, goal: int = 3):
        self.type = t_type
        self.score = score
        self.goal = goal


# 主程序
def main():
    print(f'回合{users["time"]}开始')

    # 打印分数并定义类型
    t = 0
    while t < len(users_name):
        users[users_name[t]].type = random.randint(0, len(type_dict) - 1)
        print(f'{users_name[t]}目前分数{users[users_name[t]].score}')
        t += 1

    # 玩家抉择
    while True:
        temp = input('0 白\n1 黑')
        try:
            temp = int(temp)
            if type_dict[temp]:
                users[users_name[0]].type = temp
                break

        except ValueError:
            print('请输入范围内的数字')
        except KeyError:
            print('范!围!内!')

    # 结果判定系列
    temp = []
    t = 0
    while t < len(users_name):
        temp.append(users[users_name[t]].type)
        t += 1

    a = temp.count(0)
    b = temp.count(1)
    if b == 0:
        t_if = 9
        print(f'均为{type_dict[0]}方,无人胜出')

    elif a == 0:
        t_if = 9
        print(f'均为{type_dict[1]}方,无人胜出')

    elif a > b:
        t_if = 0
        print(f'{type_dict[0]}方获胜')

    elif a < b:
        t_if = 1
        print(f'{type_dict[1]}方获胜')

    elif a == b:
        t_if = 9
        print('平局')

    t = 0
    while t < len(users_name):
        if users[users_name[t]].type == t_if:
            users[users_name[t]].score += 1
            print(f'{users_name[t]}加分!')

        if users[users_name[t]].score == users[users_name[t]].goal:
            users['if'] = False
            result.append(users_name[t])
            print(f'{users_name[t]}获胜')

        t += 1


if __name__ == '__main__':
    while True:
        # 初始赋值
        users = {
            'time': 0,
            'if': True
        }
        users_name = ['user', 'AI1', 'AI2', 'AI3']
        result = []

        t = 0
        while t < len(users_name):
            users[users_name[t]] = TYPE(users_name[t])
            t += 1

        while users['if']:
            users['time'] += 1
            main()

        with open('result.txt', 'a+', encoding='UTF-8') as f:
            f.write(f'\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n# Matching Game\ntime:{users['time']}\nwin:{result}\n')

        while True:
            if input('开启新游戏?(y/n)') == 'y':
                break

            else:
                exit()

