# Rock, Paper, Scissors
# 石头剪刀布
# 3P单人

import random
from datetime import datetime

type_dict = {
    0: '石头',
    1: '布',
    2: '剪刀'
}

users_default = {
    'time': 1,
    'if': True
}


class USERS(object):
    def __init__(self, name: str, score: int = 0, goal: int = 3):
        users[name] = {
            'name': name,
            'score': score,
            'goal': goal
        }
        users_name.append(name)


def main():
    print(f'回合{users['time']}开始')
    t = 0
    while t < len(users_name):
        print(f'{users_name[t]}目前的score是{users[users_name[t]]['score']}')
        t += 1

    while True:
        temp = input(f'你要出?\n0 {type_dict[0]}\n1 {type_dict[1]}\n2 {type_dict[2]}')
        try:
            temp = int(temp)
            if type_dict[temp]:
                a = temp
                break

        except ValueError:
            print('请输入范围内的数字!')

        except KeyError:
            print('范！围！内!')

    b = random.randint(0, len(type_dict) - 1)
    c = random.randint(0, len(type_dict) - 1)
    print(f'{users_name[1]}出{type_dict[b]}')
    print(f'{users_name[2]}出{type_dict[c]}')

    # 结果判定
    if a == b and a == c and b == c:
        print('三个完全相同,跳过')

    elif a != b and a != c and b != c:
        print('三个完全不同,跳过')

    elif a == b != c:
        if (a == 1 and c == 0) or (a == 2 and c == 1) or (a == 0 and c == 2):
            users[users_name[0]]['score'] += 1
            users[users_name[1]]['score'] += 1
            print(f'{users_name[0]}和{users_name[1]}赢了,加一分')

        elif (a == 0 and c == 1) or (a == 1 and c == 2) or (a == 2 and c == 0):
            users[users_name[2]]['score'] += 1
            print(f'{users_name[0]}和{users_name[1]}输了,{users_name[2]}加一分')

    elif a == c != b:
        if (a == 1 and b == 0) or (a == 2 and b == 1) or (a == 0 and b == 2):
            users[users_name[0]]['score'] += 1
            users[users_name[2]]['score'] += 1
            print(f'{users_name[0]}和{users_name[2]}赢了,加一分')

        elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
            users[users_name[1]]['score'] += 1
            print(f'{users_name[0]}和{users_name[2]}输了,{users_name[1]}加一分')

    elif b == c != a:
        if (b == 1 and a == 0) or (b == 2 and a == 1) or (b == 0 and a == 2):
            users[users_name[1]]['score'] += 1
            users[users_name[2]]['score'] += 1
            print(f'{users_name[1]}和{users_name[2]}赢了,加一分')

        elif (b == 0 and a == 1) or (b == 1 and a == 2) or (b == 2 and a == 0):
            users[users_name[0]]['score'] += 1
            print(f'{users_name[1]}和{users_name[2]}输了,{users_name[0]}加一分')

    # score判定
    t = 0
    while t < len(users_name):
        if users[users_name[t]]['score'] == users[users_name[t]]['goal']:
            print(f'{users_name[t]}赢了')
            result.append(users_name[t])
            users['if'] = False

        t += 1

if __name__ == '__main__':
    while True:
        # 初始赋值
        if True:
            users = users_default
            users_name = []
            result = []
            users['time'] = 0
            USERS('user')
            USERS('AI1')
            USERS('AI2')

        print('hello')
        while users['if']:
            main()
            users['time'] += 1

        with open('result.txt', 'a+', encoding='UTF-8') as f:
            f.write(f'\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n# RPS\ntime:{users['time']}\nwin:{result}\n')

        while True:
            temp = input('再来一局?(y/n)')
            if temp == 'y':
                users['if'] = True
                break

            elif temp == 'n':
                exit()

            else:
                print('请输入正确的值')
