def user_input(commands: dict[str, str]) -> str:
    while True:
        keystroke = input('> ').upper()
        if keystroke is None:
            continue
        if keystroke in commands.keys():
            return keystroke


def query_clue(commands: dict[str, str]) -> str:
    return user_input(commands)


def to_location(commands: dict[str, str]) -> str:
    return user_input(commands)
