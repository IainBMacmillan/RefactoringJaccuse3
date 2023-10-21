from dataclasses import dataclass
from source.initial_data import format_visited_places


@dataclass
class VisitedPlaces:
    def __init__(self):
        self.locations: dict[str, str] = {}

    def add_location(self, local_details) -> None:
        if local_details["place"] in self.locations.keys():
            return
        self.locations[local_details["place"]] = (f'({local_details["suspect"].lower()}, '
                                                  f'{local_details["item"].lower()})')

    def display_locations(self) -> None:
        sorted_locations = dict(sorted(self.locations.items()))
        for place, suspect_item in sorted_locations.items():
            place_command = '(' + place[0] + ')' + place[1:]
            spacing = " " * (format_visited_places - len(place))
            print(f'{place_command} {spacing}{suspect_item}')
