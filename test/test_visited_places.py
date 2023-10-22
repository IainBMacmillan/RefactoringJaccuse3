from source.visited_places import VisitedPlaces

travel_record: VisitedPlaces = VisitedPlaces()


def test__location_doesnt_exist():
    travel_record.add_location({'place': 'Glasgow', 'suspect': 'Gregor', 'item': 'Glock'})
    assert travel_record.locations.get('Dundee') is None


def test_location_does_exist():
    travel_record.add_location({'place': 'Inverness', 'suspect': 'Imogen', 'item': 'Implement'})
    travel_record.add_location({'place': 'Dundee', 'suspect': 'Derek', 'item': 'Drapes'})
    travel_record.add_location({'place': 'London', 'suspect': 'Larry', 'item': 'Lighter'})
    assert travel_record.locations.get('Dundee') == '(derek, drapes)'
