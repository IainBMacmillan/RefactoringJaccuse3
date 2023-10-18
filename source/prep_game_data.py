import random

from source.initial_data import test_data as data

liars = data.liars
culprit = data.culprit


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

