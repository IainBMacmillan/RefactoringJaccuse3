from time import sleep
from unittest import mock
from io import StringIO
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
    time_to_solve = 5  # seconds
    timer: GameClock = GameClock(time_to_solve)
    sleep(time_to_solve - 2)
    min, sec = timer.time_remaining()
    assert min == 0 and sec == 1


def test_time_taken():
    time_to_solve = 15  # seconds
    timer: GameClock = GameClock(time_to_solve)
    sleep(10)
    min, sec = timer.time_taken()
    assert min == 0 and sec == 10


@mock.patch('source.game_timer.GameClock.time_remaining', return_value=[4, 30])
def test_patch_time_remaining(mock_write):
    time_to_solve = 5  # seconds
    timer: GameClock = GameClock(time_to_solve)
    min, sec = timer.time_remaining()
    assert min == 4 and sec == 30


@mock.patch('test.test_game_timer.GameClock.display_time_remaining', return_value='Time left for patch testing')
def test_time_remaining_to_cache(mock_write):
    listen = StringIO()
    time_to_solve: int = 3  # seconds
    timer: GameClock = GameClock(time_to_solve)
    listen.write(timer.get_time_remaining())
    actual = listen.getvalue()
    listen.close()
    assert actual == 'Time left for patch testing'
    print(f' answer = {actual}')
