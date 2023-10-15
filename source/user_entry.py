from source.initial_data import move_to_location

known_clues = ['ADAM', 'APPLE', 'EVE']

def query_clue(known_suspects_and_items: list[str]) -> str:
    while True:
        ask_about = input('> ').upper()
        if ask_about in 'JZT' or (ask_about.isdecimal() and 0 < int(ask_about) <= len(known_suspects_and_items)):
            return ask_about


def to_location() -> str:
    while True:
        where_to = input('> ').upper()
        return where_to if where_to in move_to_location.keys() else None


def run_to_location() -> str:
    # used to test the mocker function against to_location
    return to_location()
