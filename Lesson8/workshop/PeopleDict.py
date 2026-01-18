import json
import os.path

class PeopleDict:
    def __init__(self, filename='people.json'):
        self.filename = filename
        self._data = {}  # Cache
        self._load_from_file()
        # print(self._data) <- to check if _data contains info from file

    # Add or actualize person data
    def _add_person(self, username, info: dict):
        self._data[username] = info
        self._save_to_file()

    # Get data for single person
    def _get_person(self, username):
        return self._data.get(username)

    def __getitem__(self, username):
        return self._get_person(username)

    def __setitem__(self, username, info):
        self._add_person(username, info)

    # Allows us to iterate over all persons
    def __iter__(self):
        return iter(self._data)

    # Returns (username, data)
    def items(self):
        return self._data.items()

    def _save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self._data, file, ensure_ascii=False, indent=4)

    def _load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self._data = json.load(file)
            except json.JSONDecodeError:
                print("Wrong json file")
                self._data = {}


if __name__ == "__main__":
    pd = PeopleDict()

    # pd.add_person('john.doe', {"name": "John", "age": 30, "city": "New York"}) <- old version, masked with __setitem__
    # print(pd._data) print just for test

    # Adding persons
    pd['john.doe'] = {"name": "John", "age": 30, "city": "New York"}
    pd['jan.kowalski'] = {"name": "Jan", "age": 20, "city": "Warsaw"}

    # Getting person
    print(pd['john.doe'])
    print(pd['jan.kowalski'])

    # Iterate over all persons
    for username in pd:
        print(f"User: {username}")

    # Full data od persons
    for username, info in pd.items():
        print(f"{username} -> {info}")