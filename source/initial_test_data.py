from source.initial_data import GameData, PLACES, SUSPECTS, ITEMS


test_places = sorted(PLACES)
test_suspects = sorted(SUSPECTS)
test_items = sorted(ITEMS)

# allows testing of output to be consistent and not use the randomising for the game_data
test_liars = ['DUKE HAUTDOG', 'ESPRESSA TOFFEEPOT', 'MAXIMUM POWERS']
zophie_suspects = ['CECIL EDGAR VANDERTON', 'DUKE HAUTDOG', 'MAXIMUM POWERS']
# test_culprit = 'DUKE HAUTDOG'
test_culprit = 'SENATOR SCHMEAR'

test_data: GameData = GameData(test_places, test_suspects, test_items,
                               test_liars, zophie_suspects, test_culprit)
'''
# to re-create the test records below, run the following script
  for idx, p in enumerate(test_places):
     print(f'P: {p:<20} S: {test_suspects[idx]:<21} I: {test_items[idx]}')

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
