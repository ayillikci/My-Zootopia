import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_info(data):
    """Generates a string with all the animal information serialized as HTML."""
    output = ''
    for animal in data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations")
        type_ = animal.get("characteristics", {}).get("type")
        
        # Create an HTML card for each animal
        output += '<li class="cards__item">\n'
        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if locations and len(locations) > 0:
            output += f"Location: {locations[0]}<br/>\n"
        if type_:
            output += f"Type: {type_}<br/>\n"
        output += '</li>\n'  # Close the list item
    return output

def replace_template_content(template_path, output_path, animal_info):
    """Replaces the placeholder in the HTML template with animal info and writes to a new file."""
    with open(template_path, "r") as file:
        template = file.read()
    
    # Replace the placeholder with animal info
    updated_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_info)
    
    # Write to a new HTML file
    with open(output_path, "w") as file:
        file.write(updated_html)

if __name__ == "__main__":
    # Load the data
    animals_data = load_data('animals_data.json')
    
    # Generate the animal information string
    animal_info = generate_animal_info(animals_data)
    
    # Replace content in the HTML template
    replace_template_content('animals_template.html', 'animals.html', animal_info)
    
    print("HTML file generated as 'animals.html'. Open it in a browser to view the result.")
