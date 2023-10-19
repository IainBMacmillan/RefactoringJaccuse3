import random
from dataclasses import dataclass
from source.initial_data import GameData


@dataclass
class SuspectAnswers:

    def __init__(self, data: GameData):
        self.clues: dict[str, dict[str, str]] = self.__set_suspects_answers(data)

    def get_answer(self, ask_about_idx, local_details, detective_notes) -> str:
        ask_about_clue = detective_notes.notes[ask_about_idx]
        if ask_about_clue in (local_details["suspect"], local_details["item"]):
            given_clue = None
            print(' They give you this clue: "No comment."')
        else:
            given_clue = self.clues[local_details["suspect"]][ask_about_clue]
            print(f'They give you this clue: "{given_clue}"')
        return given_clue

    def __set_suspects_answers(self, data: GameData):
        clues: dict[str, dict[str, str]] = {}
        for interviewee in data.suspects:
            clues[interviewee] = {}
            if interviewee not in data.liars:
                for item in data.items:
                    clues[interviewee][item] = self.__set_honest_answers(item, data.suspects, data.items, data.places)
                for suspect in data.suspects:
                    clues[interviewee][suspect] = self.__set_honest_answers(suspect, data.items,
                                                                            data.suspects, data.places)
            elif interviewee in data.liars:
                for item in data.items:
                    clues[interviewee][item] = self.__set_liar_answers(item, data.suspects, data.items, data.places)
                for suspect in data.suspects:
                    clues[interviewee][suspect] = self.__set_liar_answers(suspect, data.items,
                                                                          data.suspects, data.places)
        return clues

    def __set_liar_answers(self, ask_about_clue, clue_list, index_list, places) -> str:
        clue_answers = random.choice([places, clue_list])
        while True:
            selection = random.choice(clue_answers)
            if selection != clue_answers[index_list.index(ask_about_clue)]:
                return selection

    def __set_honest_answers(self, ask_about_clue, clue_list, index_list, places) -> str:
        clue_answers = random.choice([places, clue_list])
        return clue_answers[index_list.index(ask_about_clue)]
