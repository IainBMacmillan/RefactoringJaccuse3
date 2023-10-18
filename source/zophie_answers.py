import random

from source.initial_data import test_data as data, GameData

def suspects_zophie_answers(inital_data: GameData = data):
    zophie_clues = {}
    for interviewee in inital_data.zophie_suspects:
        kind_of_clue: list[str] = random.choice([inital_data.suspects, inital_data.places, inital_data.items])
        zophie_clues[interviewee] = select_zophie_response(inital_data, interviewee, kind_of_clue)
    return zophie_clues


def select_zophie_response(data, interviewee, clues_type: list[str] = None) -> str:
    if interviewee not in data.liars:
        return clues_type[data.suspects.index(data.culprit)]
    elif interviewee in data.liars:
        while True:
            selection = random.choice(data.items)
            if selection != clues_type[data.suspects.index(data.culprit)]:
                return selection
