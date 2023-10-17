from source.prep_game_data import Accusations

guesses: Accusations = Accusations()

def test_initialised_accusations():
    assert guesses.remaining() == 3


def test_is_none_left_False():
    assert guesses.is_none_left() != True


def test_add_accused():
    guesses.add_an_accused('ADAM')
    assert guesses.was_accused('ADAM')
    assert guesses.remaining() == 2


def test_wasnt_accused():
    assert guesses.was_accused('EVE') == False
    assert guesses.remaining() == 2

def test_max_guesses():
    guesses.add_an_accused('BRENDA')
    assert (guesses.remaining() == 1)
    guesses.add_an_accused('SNAKE')
    assert guesses.remaining() == 0
    assert guesses.is_none_left()

    guesses.add_an_accused('CAIN')
    assert guesses.remaining() == 0
    assert guesses.is_none_left()
