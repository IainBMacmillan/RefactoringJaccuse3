from source.jaccuse_original_test import PLACE_FIRST_LETTERS


def query_clue(known_suspects_and_items: list[str]):
    while True:
        ask_about = input('> ').upper()
        if ask_about in 'JZT' or (ask_about.isdecimal() and 0 < int(ask_about) <= len(known_suspects_and_items)):
            return ask_about


def to_location() -> str:
    while True:
        where_to = input('> ').upper()
        return where_to if where_to in PLACE_FIRST_LETTERS.keys() else None
