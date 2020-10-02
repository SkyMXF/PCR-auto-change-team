import os
from python_imagesearch import imagesearch
import pyautogui

import delay
import window_func

template_dir = "aimImg"

class ButtonNotFoundException(Exception):
    def __init__(self, button_subs="unknown button"):
        super(ButtonNotFoundException, self)
        self.button_subs = str(button_subs)
    
    def __str__(self):
        return "Button not found: %s"%(self.button_subs)

def findAdventureButton():
    aim_dir = os.path.join(template_dir, "adventure")
    pos = imagesearch.imagesearcharea(os.path.join(aim_dir, "adventure.png"), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3])
    if pos[0] == -1:
        pos = imagesearch.imagesearcharea(os.path.join(aim_dir, "adventure2.png"), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3])
    if pos[0] == -1:
        # 在"冒险"按钮被选中时，会以0.75s左右的频率上下跳动，有可能一次检测不到
        delay.standard_delay(1.0)
        pos = imagesearch.imagesearcharea(os.path.join(aim_dir, "adventure2.png"), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3])
    
    if pos[0] == -1:
        raise ButtonNotFoundException("adventure")
    pos = (pos[0] + window_func.NOX_window_rect[0], pos[1] + window_func.NOX_window_rect[1])
    return pos

def findPrincessArenaButton():
    pos = imagesearch.imagesearcharea(os.path.join(template_dir, "princessArena.png"), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3])
    
    if pos[0] == -1:
        raise ButtonNotFoundException("princess arena")
    pos = (pos[0] + window_func.NOX_window_rect[0], pos[1] + window_func.NOX_window_rect[1])
    return pos

def findChangeTeamButton():
    pos = imagesearch.imagesearcharea(os.path.join(template_dir, "changeTeamButton.png"), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3])
    
    if pos[0] == -1:
        raise ButtonNotFoundException("change team")
    pos = (pos[0] + window_func.NOX_window_rect[0], pos[1] + window_func.NOX_window_rect[1])
    return pos

def findMyTeamButton():
    pos = imagesearch.imagesearcharea(os.path.join(template_dir, "myTeam.png"), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3])
    
    if pos[0] == -1:
        raise ButtonNotFoundException("my team")
    pos = (pos[0] + window_func.NOX_window_rect[0], pos[1] + window_func.NOX_window_rect[1])
    return pos

def findTeamSelectButton(team_id: int):
    aim_dir = os.path.join(template_dir, "teamSelect")
    pos = imagesearch.imagesearcharea(os.path.join(aim_dir, "%d.png"%(team_id)), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3], precision=0.9)
    if pos[0] == -1:
        pos = imagesearch.imagesearcharea(os.path.join(aim_dir, "%s_s.png"%(team_id)), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3], precision=0.9)
    
    if pos[0] == -1:
        raise ButtonNotFoundException("select team %d"%team_id)
    pos = (pos[0] + window_func.NOX_window_rect[0], pos[1] + window_func.NOX_window_rect[1])
    return pos

def isEmptyTeam():
    pos = imagesearch.imagesearcharea(os.path.join(template_dir, "emptyTeam.png"), window_func.NOX_window_rect[0], window_func.NOX_window_rect[1], window_func.NOX_window_rect[2], window_func.NOX_window_rect[3])
    return pos[0] != -1
