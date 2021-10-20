ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    return ANIMALS

def create_animal(animal):
    max_id = ANIMALS[-1]["id"]

    new_id = max_id + 1

    animal["id"] = new_id

    ANIMALS.append(animal)

    return animal


def get_single_animal(id):
    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


def delete_animal(id):
    animal_index = -1

    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index

    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id, new_animal):
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = new_animal
            break