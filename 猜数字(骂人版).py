import random

name = input('you name?')
print(f'hello {name}')


def game(game_time):
    int0 = random.randint(0, 9999)
    int1 = random.randint(int0 + 1, 10000)
    why = random.randint(int0, int1)
    while True:
        print(f'此次范围{int0}至{int1}')
        user = input('猜一个')
        try:
            user = int(user)
            game_time += 1
        except Exception:
            input('你个傻逼,输个数字都不会!')
            exit(1)

        if user == why:
            if game_time <= random.randint(10, 50):
                print(f'{name}猜对了,用了{game_time}轮')
            else:
                print(f'{name}这个傻逼,竟然用了{game_time}轮')

            break

        elif user > why:
            if user <= int1:
                print('大啦')
                int1 = user
            elif user > int1:
                input('告诉你范围了你还猜范围外的')
                exit(1)

        elif user < why:
            if user >= int0:
                print('小啦')
                int0 = user
            elif user < int0:
                input('告诉你范围了你还猜范围外的')
                exit(1)


while True:
    temp = input('\n0 开始\n9 退出\n')
    if temp == '0':
        game(0)
    elif temp == '9':
        exit(0)
    else:
        input('你个傻逼,连数字都不会输是吧！')
        exit(1)
