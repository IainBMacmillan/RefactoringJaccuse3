from source.accused_records import AccusedRecords

accused_records: AccusedRecords = AccusedRecords()

def test_initialised_accusations():
    assert accused_records.remaining() == 3


def test_is_none_left_False():
    assert accused_records.is_none_left() != True


def test_add_accused():
    accused_records.add_an_accused('ADAM')
    assert accused_records.was_accused('ADAM')
    assert accused_records.remaining() == 2


def test_wasnt_accused():
    assert accused_records.was_accused('EVE') == False
    assert accused_records.remaining() == 2

def test_max_guesses():
    accused_records.add_an_accused('BRENDA')
    assert (accused_records.remaining() == 1)
    accused_records.add_an_accused('SNAKE')
    assert accused_records.remaining() == 0
    assert accused_records.is_none_left()

    accused_records.add_an_accused('CAIN')
    assert accused_records.remaining() == 0
    assert accused_records.is_none_left()
