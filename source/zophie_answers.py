import random
from dataclasses import dataclass
from source.initial_data import GameData


@dataclass
class ZophieClues:
    def __init__(self, initial_data: GameData):
        self.clues = self.suspects_zophie_answers(initial_data)

    def suspects_zophie_answers(self, initial_data: GameData):
        zophie_clues = {}
        for interviewee in initial_data.zophie_suspects:
            kind_of_clue: list[str] = random.choice([initial_data.suspects, initial_data.places, initial_data.items])
            zophie_clues[interviewee] = self.select_zophie_response(initial_data, interviewee, kind_of_clue)
        return zophie_clues

    def select_zophie_response(self, game_data, interviewee, clues_type) -> str:
        if interviewee not in game_data.liars:
            return clues_type[game_data.suspects.index(game_data.culprit)]
        elif interviewee in game_data.liars:
            while True:
                selection = random.choice(game_data.items)
                if selection != clues_type[game_data.suspects.index(game_data.culprit)]:
                    return selection

    def ask_about_zophie(self, current_person) -> str:
        if current_person in self.clues:
            print(f' They give you this clue: "{self.clues[current_person]}"')
            return self.clues[current_person]
        print('"I don\'t know anything about ZOPHIE THE CAT."')
        return ''  # same as None but as a string
