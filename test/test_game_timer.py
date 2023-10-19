from time import sleep
from source.game_timer import GameClock


def test_timer_still_running():
    time_to_solve = 2  # seconds
    timer: GameClock = GameClock(time_to_solve)
    assert not timer.is_time_over()


def test_timer_past_end():
    time_to_solve = 2  # seconds
    timer: GameClock = GameClock(time_to_solve)
    assert not timer.is_time_over()
    sleep(time_to_solve)
    assert timer.is_time_over()


def test_time_remaining():
    time_to_solve = 15  # seconds
    timer: GameClock = GameClock(time_to_solve)
    sleep(10)
    min, sec = timer.time_remaining()
    timer.display_time_remaining(test=False)
    timer.display_time_remaining(test=True)
    assert min == 0 and sec == 4


def test_time_taken():
    time_to_solve = 15  # seconds
    timer: GameClock = GameClock(time_to_solve)
    sleep(10)
    min, sec = timer.time_taken()
    assert min == 0 and sec == 10
