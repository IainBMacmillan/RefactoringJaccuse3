from dataclasses import dataclass
from source.initial_data import MAX_ACCUSATIONS
@dataclass
class DetectiveNotes:
    def __init__(self, accusations=MAX_ACCUSATIONS):
        self.notes: dict[str, str] = {
                'J': f'"J\'ACCUSE!" ({accusations} accusations left)',
                'Z': f'Ask if they know where ZOPHIE THE CAT is.',
                'T': f'Go back to the TAXI.'}
        self.clue_index = 1

    def update_clues(self, local_details: dict[str:str], places: list[str], given_clue=None):
        if given_clue is not None:
            local_details['given_clue'] = given_clue

        for clue in local_details.values():
            if clue in places:
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


