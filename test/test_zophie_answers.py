import random
from initial_test_data import test_data
from source.zophie_answers import ZophieClues

zophie_clues: ZophieClues = ZophieClues(test_data)


def test_honest_suspect_zophie_response():
    # interviewee: CECIL EDGAR VANDERTON honest zophie suspect
    clue_types = random.choice([test_data.suspects, test_data.places, test_data.items])
    for test_idx in range(15):
        answer = zophie_clues.select_zophie_response(test_data,
                                                     'CECIL EDGAR VANDERTON',
                                                       clue_types)
        assert answer in ['SENATOR SCHMEAR', 'ZOO', 'RAINBOW FLAG']


def test_lying_suspect_zophie_response():
    # interviewee: DUKE HAUTDOG lying zophie suspect gives answer not matching himself or culprit
    clue_types = random.choice([test_data.suspects, test_data.places, test_data.items])
    for test_idx in range(20):
        answer = zophie_clues.select_zophie_response(test_data,
                                                     'DUKE HAUTDOG',
                                                       clue_types)
        assert answer not in ['SENATOR SCHMEAR', 'ZOO', 'RAINBOW FLAG',
                          'DUCK POND', 'DUKE HAUTDOG', 'CLEAN UNDERPANTS']

def test_building_zophie_answers():
    # test above proves liars don't tell on themselves, so simplifies
    # assert to lying about culprit details
    for test_idx in range(20):
        clues = zophie_clues.suspects_zophie_answers(test_data)
        assert clues['CECIL EDGAR VANDERTON'] in ['SENATOR SCHMEAR', 'ZOO', 'RAINBOW FLAG']
        assert clues['DUKE HAUTDOG'] not in ['SENATOR SCHMEAR', 'ZOO', 'RAINBOW FLAG']
        assert clues['MAXIMUM POWERS'] not in ['SENATOR SCHMEAR', 'ZOO', 'RAINBOW FLAG']
