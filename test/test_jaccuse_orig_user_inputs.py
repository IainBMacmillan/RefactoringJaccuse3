from source.user_entry import query_clue, to_location
from unittest import mock


def test_to_location():
    with mock.patch("builtins.input", return_value='Q'):
        assert to_location() == 'Q'

def test_query_clue_alphabet():
    clues_3 = ['HARVEY', 'RATTLE', 'DIANA']
    with mock.patch("builtins.input", return_value='J'):
        assert query_clue(clues_3) == 'J'

def test_query_clue_numeric():
    clues_3 = ['HARVEY', 'RATTLE', 'DIANA']
    with mock.patch("builtins.input", return_value='2'):
        assert query_clue(clues_3) <= '3'