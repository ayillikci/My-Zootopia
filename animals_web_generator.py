import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animal_details(data):
    """Prints name, diet, first location, and type of each animal."""
    for animal in data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations")
        type_ = animal.get("characteristics", {}).get("type")
        
        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")
        if type_:
            print(f"Type: {type_}")
        print()  # Add a blank line between animals

if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    print_animal_details(animals_data)
