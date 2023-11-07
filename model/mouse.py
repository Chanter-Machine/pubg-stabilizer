import time

import pydirectinput

from model.contants import c_contants
from model.equipment import getCurrentWepone, c_equipment
from model.wepon import c_wepone
from view_model import mainWindow

pydirectinput.PAUSE = 0


def changeOpen():
    c_mouse.openFlag = not c_mouse.openFlag
    print("open: {}".format(c_mouse.openFlag))
    mainWindow.global_main_window.update_mouse_control_status()



def moveMouse():
    curWepone = getCurrentWepone()
    if (curWepone.name == 'none'):
        return
    print(curWepone.name)

    basic = curWepone.basic
    speed = curWepone.speed
    startTime = round(time.perf_counter(), 3) * 1000
    if curWepone.model == 'auto':
        for i in range(curWepone.maxBullets):
            if not canFire():
                break
            holdK = 1.0
            if c_contants.hold:
                holdK = curWepone.hold
            postureK = curWepone.posture_states[c_contants.posture]
            moveSum = int(round(basic[i] * curWepone.k * holdK * postureK, 2))
            moveItem = int(round(moveSum / speed * 15, 2))
            while True:
                if moveSum > moveItem:
                    pydirectinput.move(xOffset=0, yOffset=moveItem, relative=True)
                    moveSum -= moveItem
                elif moveSum > 0:
                    pydirectinput.move(xOffset=0, yOffset=moveSum, relative=True)
                    moveSum = 0
                elapsed = (round(time.perf_counter(), 3) * 1000 - startTime)
                if not canFire() or elapsed > (i + 1) * speed + 10:
                    if moveSum > 0:
                        pydirectinput.move(xOffset=0, yOffset=moveSum, relative=True)
                    break
                time.sleep(0.01)
    else:
        for i in range(curWepone.maxBullets):
            if not canFire():
                break
            holdK = 1
            if c_contants.hold:
                holdK = curWepone.hold
            moveSum = int(round(basic[i] * curWepone.k * holdK, 2))
            i += 1
            while True:
                if (moveSum > 10):
                    pydirectinput.move(xOffset=0, yOffset=10, relative=True)
                    moveSum -= 10
                elif (moveSum > 0):
                    pydirectinput.move(xOffset=0, yOffset=moveSum, relative=True)
                    moveSum = 0
                elapsed = (round(time.perf_counter(), 3) * 1000 - startTime)
                if not canFire() or elapsed > (i + 1) * speed + 10:
                    break
                time.sleep(0.01)
            pydirectinput.click()


def handlePressed():
    if not canFire():
        return
    c_contants.pool.submit(moveMouse)


# 鼠标点击事件
def onClick(x, y, button, pressed):
    if 'left' == button.name:
        c_mouse.leftPressed = pressed
        handlePressed()
    return not c_contants.exitFlag


# 按下f12测试程序生效
def testMouse():
    gun1 = c_wepone("akm", "none", "none", "none", "none")
    gun2 = c_wepone("m416", "none", "none", "none", "none")
    c_equipment.wepone1 = gun1
    c_equipment.wepone2 = gun2
    mainWindow.global_main_window.update_equipment()
    if c_mouse.openFlag:
        for i in range(10):
            pydirectinput.moveRel(xOffset=0, yOffset=10)
            time.sleep(0.1)


# 是否可以开火
def canFire():
    return c_mouse.leftPressed and c_mouse.openFlag and not c_contants.exitFlag and not c_contants.bagOpen


class c_mouse():
    leftPressed = False
    openFlag = True

    def __init__(self):
        pass
