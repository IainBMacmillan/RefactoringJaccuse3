from dataclasses import dataclass
from random import shuffle, randint, sample, choice


def moves() -> dict[str, str]:
    place_first_letters: dict[str, str] = {}
    for place in PLACES:
        place_first_letters[place[0]] = place
    place_first_letters['Q'] = 'QUIT GAME'
    return place_first_letters


@dataclass
class GameData:
    def __init__(self, places, suspects, items,
                 liars=None, zophie=None, culprit=None) -> None:
        self.places: list[str] = places
        self.suspects: list[str] = suspects
        self.items: list[str] = items
        self.liars: list[str] = sample(suspects, randint(3, 4)) if liars is None else liars
        self.zophie_suspects: list[str] = sample(suspects, randint(3, 4)) if zophie is None else zophie
        self.culprit: str = choice(suspects) if culprit is None else culprit


SUSPECTS: list = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS',
                  'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS: list = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES',
               'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES: list = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM',
                'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300
MAX_ACCUSATIONS = 3
directions_from_taxi: dict[str, str] = moves()
format_visited_places = len(max(PLACES, key=len))


shuffle(PLACES)
shuffle(SUSPECTS)
shuffle(ITEMS)

game_data: GameData = GameData(PLACES, SUSPECTS, ITEMS)
