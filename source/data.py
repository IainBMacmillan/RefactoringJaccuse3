from dataclasses import dataclass
from random import shuffle, randint, sample, choice

SUSPECTS: list = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS',
                  'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS: list = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES',
               'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES: list = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM',
                'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']


@dataclass
class GameData:
    def __init__(self, places, suspects, items,
                 liars=None, zophie=None, culprit=None) -> None:
        self.places: list[str] = places
        self.suspects: list[str] = suspects
        self.items: list[str] = items
        self.liars: list[str] = sample(suspects, randint(3, 4)) if liars is None else liars
        self.zophie_suspects: list[str] = sample(suspects, randint(3, 4)) if zophie is None else zophie
        self.culprit: str = choice(suspects)if culprit is None else culprit


shuffle(PLACES)
shuffle(SUSPECTS)
shuffle(ITEMS)

game_data: GameData = GameData(PLACES, SUSPECTS, ITEMS)

# reusable test data that is not randomised
test_places = sorted(PLACES)
test_suspects = sorted(SUSPECTS)
test_items = sorted(ITEMS)
# for idx, p in enumerate(test_places):
#     print(f'P: {p:<20} S: {test_suspects[idx]:<21} I: {test_items[idx]}')
'''
test data
P: ALBINO ALLIGATOR PIT S: BILL MONOPOLIS        I: 5 DOLLAR GIFT CARD
P: BOWLING ALLEY        S: CECIL EDGAR VANDERTON I: ANIME VHS TAPE
P: CITY HALL            S: DR. JEAN SPLICER      I: CANDLESTICK
P: DUCK POND            S: DUKE HAUTDOG          I: CLEAN UNDERPANTS
P: HIPSTER CAFE         S: ESPRESSA TOFFEEPOT    I: FLASHLIGHT
P: OLD BARN             S: MAXIMUM POWERS        I: HAMSTER WHEEL
P: UNIVERSITY LIBRARY   S: MRS. FEATHERTOSS      I: JAR OF PICKLES
P: VIDEO GAME MUSEUM    S: RAFFLES THE CLOWN     I: ONE COWBOY BOOT
P: ZOO                  S: SENATOR SCHMEAR       I: RAINBOW FLAG
liars = 3 from middle,
zophie_suspects = 1st 3 even ones 
# culprit = last one, SENATOR SCHMEAR
'''

test_liars = ['DUKE HAUTDOG', 'ESPRESSA TOFFEEPOT', 'MAXIMUM POWERS']
zophie_suspects = ['CECIL EDGAR VANDERTON', 'DUKE HAUTDOG', 'MAXIMUM POWERS']
# test_culprit = 'DUKE HAUTDOG'
test_culprit = 'SENATOR SCHMEAR'

test_data: GameData = GameData(test_places, test_suspects, test_items,
                               test_liars, zophie_suspects, test_culprit)
