import sys
import filecmp
import contextlib

from source.prep_game_data import DetectiveNotes

class MyWriter:

    def __init__(self, stdout, filename):
        self.console = stdout
        self.logfile = open(filename, 'w')

    def write(self, text):
        self.console.write(text)
        self.logfile.write(text)

    def close(self):
        self.console.close()
        self.logfile.close()

    def flush(self):
        self.console.flush()
        self.file.flush()


"""  use this to run tests to files
path = folder and filename
with open(path, 'w') as f:
    with contextlib.redirect_stdout(f):
        print('Hello, World')
"""

notepad: DetectiveNotes = DetectiveNotes()
details = {'place': 'DUCK POND', 'suspect': 'DUKE HAUTDOG', 'item': 'CLEAN UNDERPANTS'}
clue_person = 'ESPRESSA TOFFEEPOT'
clue_item = 'FLASHLIGHT'
clue_place = 'HIPSTER CAFE'

"""
if running pytest from terminal get a FileNotFoundError: [Errno 2] No such file or 
directory: '\\prep_data\\results\\detective_notes_results_3.txt'
hence adding test\\ to folder locations below. 
if running from Pycharm, remove test\\ from folder locations below.
"""
folder_results: str = 'test\\prep_data\\results\\'
folder_expected: str = 'test\\prep_data\\expected\\'

file_1 = 'detective_notes_results_1.txt'
file_2 = 'detective_notes_results_2.txt'
file_3 = 'detective_notes_results_3.txt'
file_4 = 'detective_notes_results_4.txt'
file_5 = 'detective_notes_results_5.txt'

file_list = [file_1, file_2, file_3, file_4, file_5]
def test_detective_notes_initial_commands():
    path = f'{folder_results}{file_1}'
    with open(path, 'w') as f:
        with contextlib.redirect_stdout(f):
            print(f'   Test 1 - initial commands')
            notepad.display_notes(2)


def test_detective_notes_added_local_clues():
    path = f'{folder_results}{file_2}'
    with open(path, 'w') as f:
        with contextlib.redirect_stdout(f):
            print(f'\n   Test 2 - added local clues')
            notepad.update_clues(details)
            notepad.display_notes(2)


def test_detective_notes_added_given_clue_person():
    path = f'{folder_results}{file_3}'
    with open(path, 'w') as f:
        with contextlib.redirect_stdout(f):
            print(f'\n    Test 3 - added query_clue_person')
            notepad.update_clues(details, clue_person)
            notepad.display_notes(2)


def test_detective_notes_added_given_clue_place():
    path = f'{folder_results}{file_4}'
    with open(path, 'w') as f:
        with contextlib.redirect_stdout(f):
            print(f'\n    Test 4 - added query_clue_place')
            notepad.update_clues(details, clue_place)
            notepad.display_notes(2)


def test_detective_notes_added_given_clue_item():
    path = f'{folder_results}{file_5}'
    with open(path, 'w') as f:
        with contextlib.redirect_stdout(f):
            print(f'\n    Test 5 - added query_clue_item')
            notepad.update_clues(details, clue_item)
            notepad.display_notes(2)


def test_detective_notes_results():
    master, mismatch, errors = filecmp.cmpfiles(folder_results, folder_expected, file_list, shallow=False)
    assert len(master) == 5
    assert len(mismatch) == 0
    print(mismatch)
    assert len(errors) == 0
    print(errors)

