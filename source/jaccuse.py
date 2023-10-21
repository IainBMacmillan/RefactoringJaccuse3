from source.initial_data import GameData, directions_from_taxi
from source.suspects_answers import SuspectAnswers
from source.visited_places import VisitedPlaces
from source.detective_notes import DetectiveNotes
from source.accused_records import AccusedRecords
from source.game_timer import GameClock
from source.zophie_answers import ZophieClues
from source.user_entry import query_clue, to_location


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
    clue_answers: SuspectAnswers = SuspectAnswers(data_set)
    accused_records: AccusedRecords = AccusedRecords()
    detectives_notes: DetectiveNotes = DetectiveNotes()
    visited_places: VisitedPlaces = VisitedPlaces()
    current_location = 'TAXI'

    game_running: bool = True
    while game_running:
        if is_game_over(current_location, timer, accused_records, data_set):
            game_running = False
            continue

        print()
        print(timer.get_time_remaining())

        if current_location == 'TAXI':
            print(' You are in your TAXI. Where do you want to go?')
            visited_places.display_locations()
            print('(Q)UIT GAME')
            where_to = to_location(directions_from_taxi)
            current_location = directions_from_taxi[where_to]
            continue

        print(f' You are at the {current_location}.')
        local_details: dict[str:str] = get_current_details(current_location, data_set)
        print(f' {local_details["suspect"]} with the {local_details["item"]} is here.')

        detectives_notes.update_clues(local_details, data_set.places)
        visited_places.add_location(local_details)

        if accused_records.was_accused(local_details["suspect"]):
            accused_records.display_previously_accused()
            current_location = 'TAXI'
            continue

        detectives_notes.display_notes(accused_records.remaining())
        ask_about = query_clue(detectives_notes.notes)

        if ask_about == 'J':
            accused_records.add_an_accused(local_details["suspect"])
            if local_details["suspect"] == data_set.culprit:
                accused_records.display_winners_info(data_set.culprit, timer)
                game_running = False
            else:
                accused_records.display_wrongly_accused()
                current_location = 'TAXI'

        elif ask_about == 'Z':
            zophie_answer = zophie_clues.get_zophie_clue(local_details["suspect"])
            detectives_notes.update_clues(local_details, data_set.places, zophie_answer)
            current_location = current_location

        elif ask_about == 'T':
            current_location = 'TAXI'

        else:  # numerical clue from detective's notes listing of known suspects and items
            given_answer = clue_answers.get_answer(ask_about, local_details, detectives_notes)
            detectives_notes.update_clues(local_details, data_set.places, given_answer)
            current_location = current_location

        input('Press Enter to continue...')


def is_game_over(is_quit: str, timer: GameClock, accused: AccusedRecords, data: GameData) -> bool:
    if is_quit == 'QUIT GAME':
        print('Thanks for playing!')
        return True
    if timer.is_time_over():
        print('You have run out of time!')
        return True
    if accused.is_none_left():
        accused.display_losing_info(data)
        return True


def get_current_details(place: str, data: GameData) -> dict[str, str]:
    index = data.places.index(place)
    return {'place': place, 'suspect': data.suspects[index], 'item': data.items[index]}
