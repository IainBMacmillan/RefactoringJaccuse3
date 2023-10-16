import sys
import filecmp
from source.prep_game_data import DetectiveNotes


class MyWriter:

    def __init__(self, stdout, filename):
        self.stdout = stdout
        self.logfile = open(filename, 'w')

    def write(self, text):
        self.stdout.write(text)
        self.logfile.write(text)

    def close(self):
        self.stdout.close()
        self.logfile.close()

    def flush(self):
        ...


notepad: DetectiveNotes = DetectiveNotes()
details = {'place': 'DUCK POND', 'suspect': 'DUKE HAUTDOG', 'item': 'CLEAN UNDERPANTS'}
clue = 'ESPRESSA TOFFEEPOT'


def test_setup_detective_notes():
    writer = MyWriter(sys.stdout, 'detective_notes_results.txt')
    sys.stdout = writer
    print(f'   Test 1 - initial commands')
    notepad.display_notes(2)
    print(f'\n   Test 2 - added local clues')
    notepad.update_clues(details)
    notepad.display_notes(2)
    print(f'\n    Test 3 - added query_clue')
    notepad.update_clues(details, clue)
    notepad.display_notes(2)


def test_detective_notes():
    assert filecmp.cmp('detective_notes_results.txt', 'expected_detective_notes.txt', shallow=False)
