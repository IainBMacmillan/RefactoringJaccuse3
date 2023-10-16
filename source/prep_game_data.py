import random
import time
from dataclasses import dataclass

from source.initial_data import test_data as data

TIME_TO_SOLVE = 300
MAX_ACCUSATIONS = 3
liars = data.liars
culprit = data.culprit


@dataclass
class GameClock:
    def __init__(self, duration=TIME_TO_SOLVE):
        self.start = time.time()
        self.end = self.start + duration

    def is_time_over(self) -> bool:
        return time.time() > self.end

    def display_time_remaining(self) -> None:
        minutes_left = int(self.end - time.time()) // 60
        seconds_left = int(self.end - time.time()) % 60
        print()
        print(f'Time left: {minutes_left} min, {seconds_left} sec')

    def display_time_taken(self) -> None:
        minutes_taken = int(time.time() - self.start) // 60
        seconds_taken = int(time.time() - self.start) % 60
        print()
        print(f'Good job! You solved it in {minutes_taken} min, {seconds_taken} sec.')


@dataclass
class Accusations:
    def __init__(self, max_guesses: int) -> None:
        self.count: int = max_guesses

    def is_none_left(self) -> bool:
        return True if self.count == 0 else False

    def remaining(self) -> int:
        return self.count

    def reduce(self) -> None:
        self.count -= 1


@dataclass
class DetectiveNotes:
    def __init__(self, accusations=MAX_ACCUSATIONS):
        self.notes: dict[str, str] = {
                'J': '"J\'ACCUSE!" ({accusations} accusations left)',
                'Z': 'Ask if they know where ZOPHIE THE CAT is.',
                'T': 'Go back to the TAXI.'}
        self.clue_index = 1

    def update_clues(self, local_details: dict[str:str], given_clue=None):
        if given_clue is not None:
            local_details['given_clue'] = given_clue

        for clue in local_details.values():
            if clue in data.places:
                continue
            if f'Ask about {clue}' not in self.notes.values():
                self._update_clue(clue)


    def _update_clue(self, clue):
        self.notes[str(self.clue_index)] = f'Ask about {clue}'
        self.clue_index += 1

    def display_notes(self, accusations: int = '999'):
        print()
        for key, value in self.notes.items():
            print(f' ({key}) {value}') if key != 'J' else (
                print(f' ({key}) "J\'ACCUSE!" ({accusations} accusations left)'))



def suspects_zophie_answers(thief, fibbers):
    zophie_clues = {}
    for interviewee in data.zophie_suspects:
        kind_of_clue = random.randint(1, 3)
        if kind_of_clue == 1:
            if interviewee not in fibbers:
                zophie_clues[interviewee] = thief
            elif interviewee in fibbers:
                while True:
                    zophie_clues[interviewee] = random.choice(data.suspects)
                    if zophie_clues[interviewee] != thief:
                        break
        elif kind_of_clue == 2:
            if interviewee not in fibbers:
                zophie_clues[interviewee] = data.places[data.suspects.index(thief)]
            elif interviewee in fibbers:
                while True:
                    zophie_clues[interviewee] = random.choice(data.places)
                    if zophie_clues[interviewee] != data.places[data.suspects.index(thief)]:
                        break
        elif kind_of_clue == 3:
            if interviewee not in fibbers:
                zophie_clues[interviewee] = data.items[data.suspects.index(thief)]
            elif interviewee in fibbers:
                while True:
                    zophie_clues[interviewee] = random.choice(data.items)
                    if zophie_clues[interviewee] != data.items[data.suspects.index(thief)]:
                        break
    return zophie_clues


def suspects_answers(fibbers):
    clues = {}
    for i, interviewee in enumerate(data.suspects):
        if interviewee in fibbers:
            continue

        clues[interviewee] = {}
        clues[interviewee]['debug_liar'] = False
        for item in data.items:
            if random.randint(0, 1) == 0:
                clues[interviewee][item] = data.places[data.items.index(item)]
            else:
                clues[interviewee][item] = data.suspects[data.items.index(item)]
        for suspect in data.suspects:
            if random.randint(0, 1) == 0:
                clues[interviewee][suspect] = data.places[data.suspects.index(suspect)]
            else:
                clues[interviewee][suspect] = data.items[data.suspects.index(suspect)]
    for i, interviewee in enumerate(data.suspects):
        if interviewee not in fibbers:
            continue

        clues[interviewee] = {}
        for item in data.items:
            if random.randint(0, 1) == 0:
                while True:
                    clues[interviewee][item] = random.choice(data.places)
                    if clues[interviewee][item] != data.places[data.items.index(item)]:
                        break
            else:
                while True:
                    clues[interviewee][item] = random.choice(data.suspects)
                    if clues[interviewee][item] != data.suspects[data.items.index(item)]:
                        break
        for suspect in data.suspects:
            if random.randint(0, 1) == 0:
                while True:
                    clues[interviewee][suspect] = random.choice(data.places)
                    if clues[interviewee][suspect] != data.places[data.suspects.index(suspect)]:
                        break
            else:
                while True:
                    clues[interviewee][suspect] = random.choice(data.items)
                    if clues[interviewee][suspect] != data.items[data.suspects.index(suspect)]:
                        break
    return clues
