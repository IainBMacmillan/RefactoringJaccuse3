from source.initial_data import test_data as data, GameData, directions_from_taxi, format_visited_places
from source.suspects_answers import suspects_answers
from source.detective_notes import DetectiveNotes
from source.accused_records import AccusedRecords
from source.game_timer import GameClock
from source.zophie_answers import ZophieClues
from source.user_entry import query_clue, to_location

SUSPECTS = data.suspects
ITEMS = data.items
PLACES = data.places


def jaccuse_game(setup_data: GameData):
    display_game_intro()
    running_game(setup_data)


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


def running_game(data_set: GameData):
    timer: GameClock = GameClock()
    zophie_clues: ZophieClues = ZophieClues(data_set)
    accused_records: AccusedRecords = AccusedRecords()
    detectives_notes: DetectiveNotes = DetectiveNotes()
    clues = suspects_answers(data_set)
    visited_places = {}
    current_location = 'TAXI'

    game_running: bool = True
    while game_running:
        if is_game_over(current_location, timer, accused_records):
            game_running = False
            continue
        # if current_location == 'QUIT GAME':
        #     print('Thanks for playing!')
        #     game_running = False
        #     continue
        # if timer.is_time_over():
        #     print('You have run out of time!')
        #     game_running = False
        #     continue
        # if accused_records.is_none_left():
        #     display_accused_over(data_set.culprit)
        #     game_running = False
        #     continue

        timer.display_time_remaining()

        if current_location == 'TAXI':
            print(' You are in your TAXI. Where do you want to go?')
            display_visited_places(visited_places)
            print('(Q)UIT GAME')
            where_to = to_location(directions_from_taxi)
            current_location = directions_from_taxi[where_to]
            continue

        print(f' You are at the {current_location}.')
        local_details: dict[str:str] = get_current_details(current_location)
        print(f' {local_details["suspect"]} with the {local_details["item"]} is here.')

        detectives_notes.update_clues(local_details, PLACES)
        update_visited_places(local_details, visited_places)

        if accused_records.was_accused(local_details["suspect"]):
            accused_records.display_previously_accused()
            current_location = 'TAXI'
            continue

        detectives_notes.display_notes(accused_records.remaining())
        ask_about = query_clue(detectives_notes.notes)

        if ask_about == 'J':
            accused_records.add_an_accused(local_details["suspect"])
            if local_details["suspect"] == data_set.culprit:
                display_winners_info(data_set.culprit, timer)
                game_running = False
            else:
                accused_records.display_wrongly_accused()
                current_location = 'TAXI'

        elif ask_about == 'Z':
            zophie_answer = zophie_clues.ask_about_zophie(local_details["suspect"])
            detectives_notes.update_clues(local_details, PLACES, zophie_answer)
            current_location = current_location

        elif ask_about == 'T':
            current_location = 'TAXI'

        else:  # numerical clue from known_suspects_items
            given_clue = ask_about_suspect_clues(ask_about, clues, local_details, detectives_notes)
            detectives_notes.update_clues(local_details, PLACES, given_clue)
            current_location = current_location

        input('Press Enter to continue...')


def is_game_over(quit: str, timer: GameClock, accused: AccusedRecords) -> bool:
    if quit == 'QUIT GAME':
        print('Thanks for playing!')
        return True
    if timer.is_time_over():
        print('You have run out of time!')
        return True
    if accused.is_none_left():
        display_accused_over(data.culprit)
        return True


def update_visited_places(local_details, visited_places):
    if local_details["place"] not in visited_places.keys():
        visited_places[local_details["place"]] = (f'({local_details["suspect"].lower()}, '
                                                  f'{local_details["item"].lower()})')


def get_current_details(current_location) -> dict[str, str]:
    current_location_index = PLACES.index(current_location)
    current_person = SUSPECTS[current_location_index]
    current_item = ITEMS[current_location_index]
    local_details = {'place': current_location, 'suspect': current_person, 'item': current_item}
    return local_details


def ask_about_suspect_clues(ask_about_idx, clues, local_details, detective_notes) -> str:
    ask_about_clue = detective_notes.notes[ask_about_idx]
    if ask_about_clue in (local_details["suspect"], local_details["item"]):
        given_clue = None
        print(' They give you this clue: "No comment."')
    else:
        given_clue = clues[local_details["suspect"]][ask_about_clue]
        print(f'They give you this clue: "{given_clue}"')
    return given_clue


def display_winners_info(culprit, timer):
    print('You\'ve cracked the case, Detective!')
    print(f'It was {culprit} who had catnapped ZOPHIE THE CAT.')
    timer.display_time_taken()


def display_visited_places(visited_places) -> None:
    for show_place in sorted(PLACES):
        if show_place in visited_places:
            place_info = visited_places[show_place]
            name_label = '(' + show_place[0] + ')' + show_place[1:]
            spacing = " " * (format_visited_places - len(show_place))
            print(f'{name_label} {spacing}{place_info}')


def display_accused_over(culprit) -> None:
    print()
    print(f'You have accused too many innocent people!')
    print()
    culprit_index = SUSPECTS.index(culprit)
    print(f'It was {culprit} at the {PLACES[culprit_index]} with the {ITEMS[culprit_index]} who catnapped her!')
    print(f'Better luck next time, Detective.')
