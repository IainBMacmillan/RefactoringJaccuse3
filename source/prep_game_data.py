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

    def display_time_remaining(self, test: bool = True) -> None:
        print()
        if test:
            print(f' Time left: belongs to testing')
            return
        minutes_left = int(self.end - time.time()) // 60
        seconds_left = int(self.end - time.time()) % 60
        print(f'Time left: {minutes_left} min, {seconds_left} sec')

    def display_time_taken(self) -> None:
        minutes_taken = int(time.time() - self.start) // 60
        seconds_taken = int(time.time() - self.start) % 60
        print()
        print(f'Good job! You solved it in {minutes_taken} min, {seconds_taken} sec.')


@dataclass
class Accusations:
    def __init__(self, max_guesses: int = MAX_ACCUSATIONS) -> None:
        self.count: int = max_guesses
        self.accused: list = []

    def is_none_left(self) -> bool:
        return True if self.count == 0 else False

    def remaining(self) -> int:
        return self.count

    def add_an_accused(self, innocent) -> None:
        if self.count > 0:
            self.accused.append(innocent)
            self.count -= 1

    def was_accused(self, suspect) -> bool:
        return True if suspect in self.accused else False

    @staticmethod
    def display_wrongly_accused() -> None:
        print('You have accused the wrong person, Detective!')
        print('They will not help you with anymore clues.')
        print('You go back to your TAXI.')

    @staticmethod
    def display_previously_accused() -> None:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')


@dataclass
class DetectiveNotes:
    def __init__(self, accusations=MAX_ACCUSATIONS):
        self.notes: dict[str, str] = {
                'J': f'"J\'ACCUSE!" ({accusations} accusations left)',
                'Z': f'Ask if they know where ZOPHIE THE CAT is.',
                'T': f'Go back to the TAXI.'}
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


def suspects_zophie_answers(data):
    zophie_clues = {}
    for interviewee in data.zophie_suspects:
        kind_of_clue: list[str] = random.choice([data.suspects, data.places, data.items])
        zophie_clues[interviewee] = select_zophie_response(data.liars, interviewee, data.culprit, kind_of_clue)
    return zophie_clues


def select_zophie_response(fibbers, interviewee, thief, clues_type: list[str] = None) -> str:
    if interviewee not in fibbers:
        return clues_type[data.suspects.index(thief)]
    elif interviewee in fibbers:
        while True:
            selection = random.choice(data.items)
            if selection != clues_type[data.suspects.index(thief)]:
                return selection


def suspects_answers(fibbers):
    clues: dict[str, dict[str, str]] = {}
    for interviewee in data.suspects:
        clues[interviewee] = {}
        if interviewee not in fibbers:
            for item in data.items:
                clues[interviewee][item] = select_honest_clues_answers(item, data.suspects, data.items)
            for suspect in data.suspects:
                clues[interviewee][suspect] = select_honest_clues_answers(suspect, data.items, data.suspects)
        elif interviewee in fibbers:
            for item in data.items:
                clues[interviewee][item] = select_liar_clues_answers(item, data.suspects, data.items)
            for suspect in data.suspects:
                clues[interviewee][suspect] = select_liar_clues_answers(suspect, data.items, data.suspects)
    return clues


def select_liar_clues_answers(item, clue_list, index_list) -> str:
    clue_answers = random.choice([data.places, clue_list])
    while True:
        selection = random.choice(clue_answers)
        if selection != clue_answers[index_list.index(item)]:
            return selection


def select_honest_clues_answers(suspect, clue_list, index_list) -> str:
    clue_answers = random.choice([data.places, clue_list])
    return clue_answers[index_list.index(suspect)]

