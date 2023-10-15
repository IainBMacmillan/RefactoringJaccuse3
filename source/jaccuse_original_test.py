import random
import time
from dataclasses import dataclass
from source.initial_data import test_data as data, move_to_location, moves_display_format
from source.user_entry import query_clue, to_location

SUSPECTS = data.suspects
ITEMS = data.items
PLACES = data.places
TIME_TO_SOLVE = 300
MAX_ACCUSATIONS = 3

PLACE_FIRST_LETTERS = move_to_location
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
PLACE_FIRST_LETTERS['Q'] = 'QUIT GAME'
LONGEST_PLACE_NAME_LENGTH = moves_display_format


@dataclass
class GameClock:
    def __init__(self, duration=TIME_TO_SOLVE):
        self.start = time.time()
        self.end = self.start + duration

    def is_time_over(self) -> bool:
        return time.time() > self.end

    def display_time_remaining(self) -> None:
        minutes_left = int(self.end - time.time()) // 60
        seconds_left = int(self.end - time.time()) % 60
        print()
        print(f'Time left: {minutes_left} min, {seconds_left} sec')

    def display_time_taken(self) -> None:
        minutes_taken = int(time.time() - self.start) // 60
        seconds_taken = int(time.time() - self.start) % 60
        print()
        print(f'Good job! You solved it in {minutes_taken} min, {seconds_taken} sec.')


def jaccuse_game():
    game_intro()
    running_game()


def running_game():
    timer: GameClock = GameClock()

    liars = data.liars
    culprit = data.culprit
    current_location = 'TAXI'

    clues = suspects_answers(liars)
    zophie_clues = suspects_zophie_answers(culprit, liars)
    accusations_left: int = MAX_ACCUSATIONS
    accused_suspects: list[str] = []
    known_suspects_and_items: list[str] = []
    visited_places = {}

    game_running: bool = True
    while game_running:
        if timer.is_time_over():
            print('You have run out of time!')
            game_running = False
            continue
        if accusations_left == 0:
            print('You have accused too many innocent people!')
            culprit_index = SUSPECTS.index(culprit)
            print('It was {} at the {} with the {} who catnapped her!'.format(culprit, PLACES[culprit_index],
                                                                              ITEMS[culprit_index]))
            print('Better luck next time, Detective.')
            game_running = False
            continue

        timer.display_time_taken()

        if current_location == 'TAXI':
            print(' You are in your TAXI. Where do you want to go?')
            for show_place in sorted(PLACES):
                if show_place in visited_places:
                    place_info = visited_places[show_place]
                    name_label = '(' + show_place[0] + ')' + show_place[1:]
                    spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(show_place))
                    print('{} {}{}'.format(name_label, spacing, place_info))
            print('(Q)UIT GAME')
            where_to = to_location()
            if where_to == 'Q':
                print('Thanks for playing!')
                game_running = False
            current_location = PLACE_FIRST_LETTERS[where_to]
            continue

        print(' You are at the {}.'.format(current_location))
        current_location_index = PLACES.index(current_location)
        the_person_here = SUSPECTS[current_location_index]
        the_item_here = ITEMS[current_location_index]
        print(' {} with the {} is here.'.format(the_person_here, the_item_here))

        if the_person_here not in known_suspects_and_items:
            known_suspects_and_items.append(the_person_here)
        if ITEMS[current_location_index] not in known_suspects_and_items:
            known_suspects_and_items.append(ITEMS[current_location_index])
        if current_location not in visited_places.keys():
            visited_places[current_location] = '({}, {})'.format(the_person_here.lower(), the_item_here.lower())

        if the_person_here in accused_suspects:
            print('They are offended that you accused them,')
            print('and will not help with your investigation.')
            print('You go back to your TAXI.')
            print()
            input('Press Enter to continue...')
            current_location = 'TAXI'
            continue

        print()
        print('(J) "J\'ACCUSE!" ({} accusations left)'.format(accusations_left))
        print('(Z) Ask if they know where ZOPHIE THE CAT is.')
        print('(T) Go back to the TAXI.')
        for i, suspectOrItem in enumerate(known_suspects_and_items):
            print('({}) Ask about {}'.format(i + 1, suspectOrItem))

        ask_about = query_clue(known_suspects_and_items)

        if ask_about == 'J':
            accusations_left -= 1
            if the_person_here == culprit:
                print('You\'ve cracked the case, Detective!')
                print('It was {} who had catnapped ZOPHIE THE CAT.'.format(culprit))
                timer.display_time_remaining()
                game_running = False
            else:
                accused_suspects.append(the_person_here)
                print('You have accused the wrong person, Detective!')
                print('They will not help you with anymore clues.')
                print('You go back to your TAXI.')
                current_location = 'TAXI'

        elif ask_about == 'Z':
            if the_person_here not in zophie_clues:
                print('"I don\'t know anything about ZOPHIE THE CAT."')
            elif the_person_here in zophie_clues:
                print(' They give you this clue: "{}"'.format(zophie_clues[the_person_here]))
                if zophie_clues[the_person_here] not in known_suspects_and_items and \
                        zophie_clues[the_person_here] not in PLACES:
                    known_suspects_and_items.append(zophie_clues[the_person_here])

        elif ask_about == 'T':
            current_location = 'TAXI'
            continue

        else:
            thing_being_asked_about = known_suspects_and_items[int(ask_about) - 1]
            if thing_being_asked_about in (the_person_here, the_item_here):
                print(' They give you this clue: "No comment."')
            else:
                print(' They give you this clue: "{}"'.format(clues[the_person_here][thing_being_asked_about]))
                # Add non-place clues to the list of known things:
                if clues[the_person_here][thing_being_asked_about] not in known_suspects_and_items and \
                        clues[the_person_here][thing_being_asked_about] not in PLACES:
                    known_suspects_and_items.append(clues[the_person_here][thing_being_asked_about])

        input('Press Enter to continue...')


def game_intro():
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


def suspects_zophie_answers(culprit, liars):
    zophie_clues = {}
    for interviewee in data.zophie_suspects:
        kind_of_clue = random.randint(1, 3)
        if kind_of_clue == 1:
            if interviewee not in liars:
                zophie_clues[interviewee] = culprit
            elif interviewee in liars:
                while True:
                    zophie_clues[interviewee] = random.choice(SUSPECTS)
                    if zophie_clues[interviewee] != culprit:
                        break
        elif kind_of_clue == 2:
            if interviewee not in liars:
                zophie_clues[interviewee] = PLACES[SUSPECTS.index(culprit)]
            elif interviewee in liars:
                while True:
                    zophie_clues[interviewee] = random.choice(PLACES)
                    if zophie_clues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                        break
        elif kind_of_clue == 3:
            if interviewee not in liars:
                zophie_clues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
            elif interviewee in liars:
                while True:
                    zophie_clues[interviewee] = random.choice(ITEMS)
                    if zophie_clues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                        break
    return zophie_clues


def suspects_answers(liars):
    clues = {}
    for i, interviewee in enumerate(SUSPECTS):
        if interviewee in liars:
            continue

        clues[interviewee] = {}
        clues[interviewee]['debug_liar'] = False
        for item in ITEMS:
            if random.randint(0, 1) == 0:
                clues[interviewee][item] = PLACES[ITEMS.index(item)]
            else:
                clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
        for suspect in SUSPECTS:
            if random.randint(0, 1) == 0:
                clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
            else:
                clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]
    for i, interviewee in enumerate(SUSPECTS):
        if interviewee not in liars:
            continue

        clues[interviewee] = {}
        for item in ITEMS:
            if random.randint(0, 1) == 0:
                while True:
                    clues[interviewee][item] = random.choice(PLACES)
                    if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                        break
            else:
                while True:
                    clues[interviewee][item] = random.choice(SUSPECTS)
                    if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                        break
        for suspect in SUSPECTS:
            if random.randint(0, 1) == 0:
                while True:
                    clues[interviewee][suspect] = random.choice(PLACES)
                    if clues[interviewee][suspect] != PLACES[SUSPECTS.index(suspect)]:
                        break
            else:
                while True:
                    clues[interviewee][suspect] = random.choice(ITEMS)
                    if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                        break
    return clues


def main():
    jaccuse_game()


if __name__ == '__main__':
    main()
