import re, time
import win32gui, win32con, win32com.client

class NOXNotFoundException(Exception):
    def __init__(self):
        super(NOXNotFoundException, self)
    
    def __str__(self):
        return "cannot find NOX window."

NOX_window_rect = (-1, -1, -1, -1)
    
def setActiveCallback(hwnd, wildcard):
    '''检查所给窗口是否为需要前置的目标窗口
    '''
    global NOX_window_rect
    if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
        win32gui.BringWindowToTop(hwnd)
        # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        # 设置为当前活动窗口
        win32gui.SetForegroundWindow(hwnd)
        NOX_window_rect = win32gui.GetWindowRect(hwnd)

def activeNOX():
    '''前置NOX窗口并保存rect信息
    '''
    global NOX_window_rect
    NOX_window_rect = (-1, -1, -1, -1)
    win32gui.EnumWindows(setActiveCallback, ".*%s.*"%"夜神模拟器")
    if NOX_window_rect[0] == -1:
        raise NOXNotFoundException()
