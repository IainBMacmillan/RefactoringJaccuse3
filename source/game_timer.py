import time
from dataclasses import dataclass

from source.initial_data import TIME_TO_SOLVE


@dataclass
class GameClock:
    def __init__(self, duration=TIME_TO_SOLVE):
        self.start = time.time()
        self.end = self.start + duration

    def is_time_over(self) -> bool:
        return time.time() > self.end

    def display_time_remaining(self, test: bool = True) -> None:
        print()
        if test:
            print(f' Time left: belongs to testing')
            return
        minutes_left, seconds_left = self.time_remaining()
        print(f'Time left: {minutes_left} min, {seconds_left} sec')

    def time_remaining(self):
        minutes_left = int(self.end - time.time()) // 60
        seconds_left = int(self.end - time.time()) % 60
        return minutes_left, seconds_left

    def display_time_taken(self) -> None:
        minutes_taken, seconds_taken = self.time_taken()
        print()
        print(f'Good job! You solved it in {minutes_taken} min, {seconds_taken} sec.')

    def time_taken(self):
        minutes_taken = int(time.time() - self.start) // 60
        seconds_taken = int(time.time() - self.start) % 60
        return minutes_taken, seconds_taken
