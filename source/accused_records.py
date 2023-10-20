from dataclasses import dataclass
from source.initial_data import MAX_ACCUSATIONS, GameData
from source.game_timer import GameClock


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

    def display_winners_info(self, culprit: str, timer: GameClock) -> None:
        print('You\'ve cracked the case, Detective!')
        print(f'It was {culprit} who had catnapped ZOPHIE THE CAT.')
        print(timer.get_time_taken())

    def display_losing_info(self, data: GameData) -> None:
        print()
        print(f'You have accused too many innocent people!')
        print()
        culprit_idx = data.suspects.index(data.culprit)
        print(f'It was {data.culprit} at the {data.places[culprit_idx]} with '
              f'the {data.items[culprit_idx]} who catnapped her!')
        print(f'Better luck next time, Detective.')


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
