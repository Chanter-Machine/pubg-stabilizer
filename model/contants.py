from concurrent.futures import ThreadPoolExecutor
import json

class c_contants():
    isAuthorized = False
    # 程序退出标记
    exitFlag = False
    #背包打开标记
    bagOpen = False
    #屏息标记
    hold = False
    #姿势 0默认 1下蹲 2趴下
    posture = 0
    pool = ThreadPoolExecutor(max_workers=10)

    # 读取JSON文件
    with open('./resource/config.json', 'r') as file:
        data = json.load(file)

    guns = data

    keyboard_listener = None
    mouse_listener = None
    def __init__(self):
        pass
