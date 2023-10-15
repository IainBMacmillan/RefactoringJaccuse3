from source.user_entry import run_to_location, query_clue, to_location

clues3 = ['ADAM', 'APPLE', 'EVE']


def test_run_to_location(mocker) -> None:
    mocker.patch('source.user_entry.to_location', return_value='Q')
    assert run_to_location() == 'Q'


def test_to_location(mocker):
    mocker.patch("builtins.input", return_value='Q')
    assert to_location() == 'Q'


def test_query_clue_alphabet(mocker):
    mocker.patch("builtins.input", return_value='J')
    assert query_clue(clues3) == 'J'


def test_query_clue_numeric(mocker):
    mocker.patch("builtins.input", return_value='2')
    assert query_clue(clues3) <= '3'
