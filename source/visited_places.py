from dataclasses import dataclass
from source.initial_data import GameData, format_visited_places


@dataclass
class VisitedPlaces:
    def __init__(self):
        self.locations: dict[str, str] = {}

    def add_location(self, local_details) -> None:
        if local_details["place"] in self.locations.keys():
            return
        self.locations[local_details["place"]] = (f'({local_details["suspect"].lower()}, '
                                                  f'{local_details["item"].lower()})')

    def display_locations(self, data: GameData) -> None:
        for show_place in sorted(data.places):
            if show_place in self.locations:
                place_info = self.locations[show_place]
                name_label = '(' + show_place[0] + ')' + show_place[1:]
                spacing = " " * (format_visited_places - len(show_place))
                print(f'{name_label} {spacing}{place_info}')
