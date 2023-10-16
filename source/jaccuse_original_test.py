from source.initial_data import test_data as data, move_to_location, moves_display_format
from source.prep_game_data import MAX_ACCUSATIONS, GameClock, Accusations, DetectiveNotes, suspects_zophie_answers, \
    suspects_answers
from source.user_entry import query_clue, to_location

SUSPECTS = data.suspects
ITEMS = data.items
PLACES = data.places


def jaccuse_game():
    display_game_intro()
    running_game()


def display_game_intro():
    print("""J'ACCUSE! (a mystery game)")
    By Al Sweigart al@inventwithpython.com 
    Inspired by Homestar Runner\'s "Where\'s an Egg?" game 

    You are the world-famous detective, Mathilde Camus. 
    ZOPHIE THE CAT has gone missing, and you must sift through the clues. 
    Suspects either always tell lies, or always tell the truth. Ask them 
    about other people, places, and items to see if the details they give are 
    truthful and consistent with your observations. Then you will know if 
    their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE 
    CAT in time and accuse the guilty party? 
    """)
    input('Press Enter to begin...')


def running_game():
    timer: GameClock = GameClock()

    liars = data.liars
    culprit = data.culprit
    current_location = 'TAXI'

    clues = suspects_answers(liars)
    zophie_clues = suspects_zophie_answers(culprit, liars)
    accusations: Accusations = Accusations(MAX_ACCUSATIONS)
    accused_suspects: list[str] = []
    detectives_notes: DetectiveNotes = DetectiveNotes()
    visited_places = {}

    game_running: bool = True
    while game_running:
        if timer.is_time_over():
            print('You have run out of time!')
            game_running = False
            continue
        if accusations.is_none_left():
            display_accused_over(culprit)
            game_running = False
            continue

        timer.display_time_remaining()

        if current_location == 'TAXI':
            print(' You are in your TAXI. Where do you want to go?')
            display_visited_places(visited_places)
            print('(Q)UIT GAME')
            where_to = to_location(move_to_location)
            if where_to == 'Q':
                print('Thanks for playing!')
                game_running = False
            current_location = move_to_location[where_to]
            continue

        print(f' You are at the {current_location}.')
        local_details: dict[str:str] = get_current_details(current_location)
        print(f' {local_details["suspect"]} with the {local_details["item"]} is here.')

        detectives_notes.update_clues(local_details)
        update_visited_places(local_details, visited_places)

        if local_details["suspect"] in accused_suspects:
            display_previously_accused()
            current_location = 'TAXI'
            continue

        detectives_notes.display_notes(accusations.remaining())
        ask_about = query_clue(detectives_notes.notes)

        if ask_about == 'J':
            accusations.reduce()
            accused_suspects.append(local_details["suspect"])
            if local_details["suspect"] == culprit:
                display_winners_info(culprit, timer)
                game_running = False
            else:
                display_wrongly_accused()
                current_location = 'TAXI'

        elif ask_about == 'Z':
            ask_about_zophie(local_details["suspect"], detectives_notes.notes, zophie_clues)
            current_location = current_location

        elif ask_about == 'T':
            current_location = 'TAXI'

        else:  # numerical clue from known_suspects_items
            given_clue = ask_about_suspect_clues(ask_about, clues, local_details, detectives_notes.notes)
            detectives_notes.update_clues(local_details, given_clue)
            current_location = current_location

        input('Press Enter to continue...')


def update_visited_places(local_details, visited_places):
    if local_details["place"] not in visited_places.keys():
        visited_places[local_details["place"]] = f'({local_details["suspect"]}, {local_details["item"]})'


def get_current_details(current_location) -> dict[str, str]:
    current_location_index = PLACES.index(current_location)
    current_person = SUSPECTS[current_location_index]
    current_item = ITEMS[current_location_index]
    local_details = {'place': current_location, 'suspect': current_person, 'item': current_item}
    return local_details


def ask_about_suspect_clues(ask_about, clues, local_details, known_suspects_and_items) -> str:
    thing_being_asked_about = known_suspects_and_items[int(ask_about) - 1]
    if thing_being_asked_about in (local_details["suspect"], local_details["item"]):
        given_clue = None
        print(' They give you this clue: "No comment."')
    else:
        given_clue = clues[local_details["suspect"]][thing_being_asked_about]
        print(f'They give you this clue: "{given_clue}"')
    return given_clue


def ask_about_zophie(current_person, known_suspects_and_items, zophie_clues):
    if current_person not in zophie_clues:
        print('"I don\'t know anything about ZOPHIE THE CAT."')
    elif current_person in zophie_clues:
        print(f' They give you this clue: "{zophie_clues[current_person]}"')
        if zophie_clues[current_person] not in known_suspects_and_items and \
                zophie_clues[current_person] not in PLACES:
            known_suspects_and_items.append(zophie_clues[current_person])


def display_wrongly_accused():
    print('You have accused the wrong person, Detective!')
    print('They will not help you with anymore clues.')
    print('You go back to your TAXI.')


def display_winners_info(culprit, timer):
    print('You\'ve cracked the case, Detective!')
    print(f'It was {culprit} who had catnapped ZOPHIE THE CAT.')
    timer.display_time_taken()


def display_detectives_known_clues(accusations, known_suspects_and_items):
    print()
    print('(J) "J\'ACCUSE!" ({} accusations left)'.format(accusations.remaining()))
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for clue_ref, suspectOrItem in enumerate(known_suspects_and_items, start=1):
        print(f'({clue_ref}) Ask about {suspectOrItem}')


def display_previously_accused():
    print('They are offended that you accused them,')
    print('and will not help with your investigation.')
    print('You go back to your TAXI.')
    print()
    input('Press Enter to continue...')


def update_known_suspects_items(known_suspects_and_items: list[str], local_details: dict[str:str], given_clue=None):
    if given_clue is not None and given_clue not in PLACES and given_clue not in known_suspects_and_items:
        known_suspects_and_items.append(given_clue)
    if local_details["suspect"] not in known_suspects_and_items:
        known_suspects_and_items.append(local_details["suspect"])
    if local_details["item"] not in known_suspects_and_items:
        known_suspects_and_items.append(local_details["item"])


def display_visited_places(visited_places) -> None:
    for show_place in sorted(PLACES):
        if show_place in visited_places:
            place_info = visited_places[show_place]
            name_label = '(' + show_place[0] + ')' + show_place[1:]
            spacing = " " * (moves_display_format - len(show_place))
            print(f'{name_label} {spacing}{place_info}')


def display_accused_over(culprit) -> None:
    print()
    print(f'You have accused too many innocent people!')
    print()
    culprit_index = SUSPECTS.index(culprit)
    print(f'It was {culprit} at the {PLACES[culprit_index]} with the {ITEMS[culprit_index]} who catnapped her!')
    print(f'Better luck next time, Detective.')


def main():
    jaccuse_game()


if __name__ == '__main__':
    main()
