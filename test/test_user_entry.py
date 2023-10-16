from source.user_entry import query_clue, to_location

clues3 = {'J': 'ADAM', '2': 'APPLE', '3': 'EVE'}
direction = {'A': 'ALLIGATOR PIT', 'D': 'DUCK POND', 'Q': 'QUIT GAME'}

def test_to_location(mocker):
    mocker.patch("builtins.input", return_value='Q')
    assert to_location(direction) == 'Q'


def test_query_clue_alphabet(mocker):
    mocker.patch("builtins.input", return_value='J')
    assert query_clue(clues3) == 'J'


def test_query_clue_numeric(mocker):
    mocker.patch("builtins.input", return_value='2')
    assert query_clue(clues3) <= '3'
