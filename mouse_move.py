import time
import pyautogui
import random

import window_func
import img_match
import delay


def clickRandomPos(pos, x_move_max, y_move_max):
    x_move = random.randint(0, x_move_max)
    y_move = random.randint(0, y_move_max)
    pyautogui.moveTo(pos[0] + x_move, pos[1] + y_move)
    delay.standard_delay(0.1)
    pyautogui.click()

def clickAdventureButton():
    # 底部"冒险"按钮
    pos = img_match.findAdventureButton()

    clickRandomPos((pos[0] + 20, pos[1] + 10), 160, 30)
    delay.random_float_delay(0.3, 0.2)

def clickPrincessArena():
    # "公主竞技场"按钮
    pos = img_match.findPrincessArenaButton()

    clickRandomPos((pos[0] + 20, pos[1] + 10), 270, 90)
    delay.random_float_delay(0.3, 0.2)

def clickChangeTeamButton():
    # "防守设定"按钮
    pos = img_match.findChangeTeamButton()

    clickRandomPos((pos[0] + 20, pos[1] + 10), 150, 40)
    delay.random_float_delay(1.5, 0.2)

def clickCancelAll():
    # 点击空白区域取消所有操作
    pos = (window_func.NOX_window_rect[0] + 552, window_func.NOX_window_rect[1] + 725)
    for _ in range(5):
        clickRandomPos((pos[0] + 20, pos[1] + 4), 140, 12)
        delay.random_float_delay(0.1, 0.2)

def clickClearTeam():
    # 清空队伍
    pos = (window_func.NOX_window_rect[0] + 680, window_func.NOX_window_rect[1] + 595)
    try_times = 0
    while not img_match.isEmptyTeam():
        clickRandomPos((pos[0] + 20, pos[1] + 20), 60, 60)
        try_times += 1
        if try_times >= 10:
            raise img_match.ButtonNotFoundException("clear team")
        delay.random_float_delay(0.3, 0.2)
    delay.random_float_delay(0.3, 0.2)

def clickSelectTeam(team_id:int):
    # 选择队伍1-3
    pos = img_match.findTeamSelectButton(team_id)
    clickRandomPos((pos[0] + 20, pos[1] + 10), 90, 20)
    delay.random_float_delay(0.3, 0.2)

def clickMyTeamButton():
    # "我的队伍"按钮
    pos = img_match.findMyTeamButton()

    clickRandomPos((pos[0] + 20, pos[1] + 10), 80, 10)
    delay.random_float_delay(0.8, 0.2)

def clickPreparedPage(page_id:int):
    # "我的队伍"界面选择指定队伍页1-5
    pos = (window_func.NOX_window_rect[0] + 68 + (page_id - 1) * 191, window_func.NOX_window_rect[1] + 131)
    clickRandomPos((pos[0] + 20, pos[1] + 10), 150, 20)
    delay.random_float_delay(0.5, 0.3)

def clickReverseRank():
    # "我的队伍"界面更改排序顺序
    pos = (window_func.NOX_window_rect[0] + 1089, window_func.NOX_window_rect[1] + 137)
    clickRandomPos((pos[0] + 20, pos[1] + 10), 80, 10)
    delay.random_float_delay(0.5, 0.3)

def clickPreparedTeam(team_id:int):
    # "我的队伍"界面选择队伍1-3
    pos = (window_func.NOX_window_rect[0] + 949, window_func.NOX_window_rect[1] + 233 + (team_id - 1) * 159)
    clickRandomPos((pos[0] + 20, pos[1] + 10), 170, 40)
    delay.random_float_delay(0.5, 0.3)

def clickFinish():
    # 配队界面确认
    pos = (window_func.NOX_window_rect[0] + 1017, window_func.NOX_window_rect[1] + 608)
    clickRandomPos((pos[0] + 20, pos[1] + 10), 170, 40)
    delay.random_float_delay(0.3, 0.3)