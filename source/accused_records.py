from dataclasses import dataclass
from source.initial_data import MAX_ACCUSATIONS


@dataclass
class AccusedRecords:
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
