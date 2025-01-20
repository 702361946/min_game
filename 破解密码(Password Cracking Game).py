# Password Cracking Game
import json
import os
import random
from datetime import datetime

config = {
    "allow_duplicate": True,  # 允许重复
    "len": 4,  # 生成长度
    "step_limit": 0,  # 步数限制
    "place_tips": True,  # 位置提示
}

# 文件配置读取
if True:
    try:
        with open('.\\game_config.json', 'r', encoding='utf-8') as f:
            file_config = json.load(f)
            for k in config.keys():
                if not k in file_config.keys():
                    file_config[k] = config[k]
            config = file_config

    except FileNotFoundError:
        print('文件配置不存在,使用程序默认配置')
        with open('.\\game_config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)

    except Exception as e:
        print(e)


def setting():
    print("当前设置")
    for _k in config.keys():
        print(f'{_k}:{type(config[_k]).__name__}:{config[_k]}')

    while True:
        print("\n输入exit返回主菜单\n输入save保存设置到文件")
        _t = input('输入要修改的键(修改后请输入save以保存设置): ').strip()

        if _t in config.keys():
            current_value = config[_t]
            print(f'当前值: {type(current_value).__name__}:{current_value}')
            new_value = input('请输入新值: ').strip()

            try:
                match type(current_value).__name__:
                    case 'int':
                        new_value = int(new_value)
                    case 'float':
                        new_value = float(new_value)
                    case 'bool':
                        if new_value.lower() in ('true', '1', 'yes'):
                            new_value = True
                        elif new_value.lower() in ('false', '0', 'no'):
                            new_value = False
                        else:
                            print('无效的布尔值输入，请输入 "true" 或 "false"')
                            continue
                    case 'str':
                        new_value = new_value

                    case _:
                        print('未知类型,请直接修改配置文件')

                config[_t] = new_value
                print(f'已更新 {_t} 的值为: {new_value}')

            except ValueError:
                print("输入值与目标类型不匹配，请重新尝试。")

        elif _t == 'exit':
            return True
        elif _t == 'save':
            if config["allow_duplicate"] is False and config['len'] > 10:
                print('请将allow_duplicate(允许重复)的值设为True,\n或将len(生成长度)设为<=10')
                continue
            config_path = os.path.join(os.getcwd(), "game_config.json")
            try:
                with open(config_path, 'w', encoding='utf-8') as _f:
                    json.dump(config, _f, indent=4)
                print('保存完成')
            except Exception as _e:
                print(f"保存配置时发生错误: {_e}")
        else:
            print('键不存在，请检查输入是否正确。')


def game():
    def build() -> dict[list[int | list]]:
        """

        :return: 返回的字典中,"key"是密钥,“user_input_time”用于记录每次用户输入的
        """
        if config['allow_duplicate'] is False and config['len'] > 10:
            input('配置错误!!!\n请删除配置文件进行重置或咨询相关人士')
            raise ValueError('(allow_duplicate and len) not (True and >10)')
        _game_values = {
            "key": [],
            "user_input_time": [],
            "step": 0,
        }
        while len(_game_values['key']) < config['len']:
            _t = str(random.randint(0, 9))
            if config['allow_duplicate'] is False:
                if _t in _game_values['key']:
                    continue
            else:
                _game_values['key'].append(_t)
        return _game_values

    def _main() -> None:
        _t = list(input(f'输入长度为{config["len"]}的密钥(范围数字0~9)'))
        if len(_t) != config['len']:
            print('长度错误')
        else:
            __t = []
            _win = 0
            for _i in range(config['len']):
                # T(True)对,F(False)错,I(in)存在
                if _t[_i] == game_values['key'][_i]:
                    __t.append(f'T{_t[_i]}')
                    _win += 1
                elif config['place_tips'] is True and _t[_i] in game_values['key']:
                    __t.append(f'I{_t[_i]}')
                else:
                    __t.append(f'F{_t[_i]}')
            print(__t)
            game_values['user_input_time'].append(__t)
            if _win == config['len']:
                raise ValueError('Game win')

    game_values = build()
    # 用raise打印胜利信息
    try:
        if not config['step_limit']:
            while True:
                _main()
        else:
            while game_values['step'] < config['step_limit']:
                _main()
            raise ValueError('Game over')

    except Exception as _e:
        print(f"\n{_e}\n")
        _end = None
        # str化目的是去除Error标签
        if str(_e) == 'Game win' or str(_e) == 'Game over':
            _end = {
                'info': str(_e),
                'step': len(game_values['user_input_time']),
                'inputs': ''
            }
            for _i in game_values['user_input_time']:
                _end['inputs'] = f"{_end['inputs']}\n{_i}"
        if _end is not None:
            with open('.\\result.txt', 'a+', encoding='utf-8') as _f:
                _f.write(f"""
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# Password Cracking Game
info:{_end["info"]}
step:{_end["step"]}
inputs:{_end["inputs"]}
""")


def main():
    while True:
        match input('输入(0)open开始游戏\n输入(1)setting进入设置\n输入(9)exit退出游戏'):
            case '0' | 'open':
                game()
            case '1' | 'setting':
                setting()
            case '9' | 'exit':
                break
            case _:
                print('未知')


if __name__ == '__main__':
    main()
