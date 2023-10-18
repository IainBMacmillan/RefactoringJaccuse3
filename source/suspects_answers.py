import random
from source.initial_data import test_data as data, GameData

liars = data.liars
culprit = data.culprit


def suspects_answers(data: GameData):
    clues: dict[str, dict[str, str]] = {}
    for interviewee in data.suspects:
        clues[interviewee] = {}
        if interviewee not in data.liars:
            for item in data.items:
                clues[interviewee][item] = select_honest_answers(item, data.suspects, data.items, data.places)
            for suspect in data.suspects:
                clues[interviewee][suspect] = select_honest_answers(suspect, data.items, data.suspects, data.places)
        elif interviewee in data.liars:
            for item in data.items:
                clues[interviewee][item] = select_liar_answers(item, data.suspects, data.items, data.places)
            for suspect in data.suspects:
                clues[interviewee][suspect] = select_liar_answers(suspect, data.items, data.suspects, data.places)
    return clues


def select_liar_answers(ask_about_clue, clue_list, index_list, places) -> str:
    clue_answers = random.choice([places, clue_list])
    while True:
        selection = random.choice(clue_answers)
        if selection != clue_answers[index_list.index(ask_about_clue)]:
            return selection


def select_honest_answers(ask_about_clue, clue_list, index_list, places) -> str:
    clue_answers = random.choice([places, clue_list])
    return clue_answers[index_list.index(ask_about_clue)]
