import random
import time

import window_func
import mouse_move
import img_match
import delay

DEFAULT_EXCEPTION = img_match.ButtonNotFoundException

def refresh_rank():
    window_func.activeNOX()
    delay.standard_delay(1.0)
    img_match.window_rect = window_func.NOX_window_rect

    mouse_move.clickCancelAll()
    retry_wrapper(mouse_move.clickAdventureButton, DEFAULT_EXCEPTION, 2)
    retry_wrapper(mouse_move.clickPrincessArena, DEFAULT_EXCEPTION, 5)

prev_team_page = -1
def change_team():
    global prev_team_page

    window_func.activeNOX()
    delay.standard_delay(1.0)
    img_match.window_rect = window_func.NOX_window_rect

    mouse_move.clickCancelAll()
    retry_wrapper(mouse_move.clickAdventureButton, DEFAULT_EXCEPTION, 2)
    retry_wrapper(mouse_move.clickPrincessArena, DEFAULT_EXCEPTION, 5)
    retry_wrapper(mouse_move.clickChangeTeamButton, DEFAULT_EXCEPTION, 20)

    # clear team
    mouse_move.clickSelectTeam(1)
    mouse_move.clickClearTeam()
    mouse_move.clickSelectTeam(2)
    mouse_move.clickClearTeam()
    mouse_move.clickSelectTeam(3)
    mouse_move.clickClearTeam()
    
    # random team info
    team_page_id = random.randint(2, 5)
    while team_page_id == prev_team_page:
        team_page_id = random.randint(2, 5)
    prev_team_page = team_page_id
    rankReverse = False # True if random.random() >= 0.5 else False
    switch12 = True if random.random() >= 0.5 else False
    time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print("[%s]Team page %d, rank reverse %s, switch 1 and 2 %s..."%(time_str, team_page_id, str(rankReverse), str(switch12)))

    # change team
    mouse_move.clickSelectTeam(1)
    retry_wrapper(mouse_move.clickMyTeamButton, DEFAULT_EXCEPTION, 2)
    mouse_move.clickPreparedPage(team_page_id)
    if rankReverse:
        mouse_move.clickReverseRank()
    team_id = 2 if switch12 else 1
    mouse_move.clickPreparedTeam(team_id)

    mouse_move.clickSelectTeam(2)
    retry_wrapper(mouse_move.clickMyTeamButton, DEFAULT_EXCEPTION, 2)
    mouse_move.clickPreparedPage(team_page_id)
    if rankReverse:
        mouse_move.clickReverseRank()
    team_id = 1 if switch12 else 2
    mouse_move.clickPreparedTeam(team_id)

    mouse_move.clickSelectTeam(3)
    retry_wrapper(mouse_move.clickMyTeamButton, DEFAULT_EXCEPTION, 2)
    mouse_move.clickPreparedPage(team_page_id)
    if rankReverse:
        mouse_move.clickReverseRank()
    team_id = 3
    mouse_move.clickPreparedTeam(team_id)

    mouse_move.clickFinish()

def retry_wrapper(func, exception, max_retry_times):
    retry_times = 0
    finished, e = try_once(func, exception)
    while not finished:
        retry_times += 1
        if retry_times > max_retry_times:
            raise e
        finished, e = try_once(func, exception)

def try_once(func, exception):
    try:
        func()
    except exception as e:
        return False, e
    return True, exception()

if __name__ == "__main__":

    while True:
        for _ in range(3):
            try:
                time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                print("[%s]Check rank..."%(time_str))
                retry_wrapper(refresh_rank, DEFAULT_EXCEPTION, 2)
            except DEFAULT_EXCEPTION as e:
                print(e)
            finally:
                delay.random_float_delay(5.0, float_region=1.0)
        
        try:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            print("[%s]Change team..."%(time_str))
            retry_wrapper(change_team, DEFAULT_EXCEPTION, 2)
        except DEFAULT_EXCEPTION as e:
            print(e)
        finally:
            delay.random_float_delay(5.0, float_region=1.0)
    