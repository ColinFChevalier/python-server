from models import Animal, Location
import json
import sqlite3

ANIMALS = []

# def create_animal(animal):
#     max_id = ANIMALS[-1]["id"]

#     new_id = max_id + 1

#     animal["id"] = new_id

#     ANIMALS.append(animal)

#     return animal

def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['species'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_animal['id'] = id


    return json.dumps(new_animal)


def get_single_animal(id):
    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

# def delete_animal(id):
#     animal_index = -1

#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             animal_index = index

#     if animal_index >= 0:
#         ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


# def update_animal(id, new_animal):
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             ANIMALS[index] = new_animal
#             break

def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
    for row in dataset:

    # Create an animal instance from the current row
        animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                    row['location_id'], row['customer_id'])

    # Create a Location instance from the current row
        location = Location(row[['id'], row['location_name'], row['location_address']])

    # Add the dictionary representation of the location to the animal
        animal.location = location.__dict__

    # Add the dictionary representation of the animal to the list
        animals.append(animal.__dict__)

        # for row in dataset:

        #     # Create an animal instance from the current row.
        #     # Note that the database fields are specified in
        #     # exact order of the parameters defined in the
        #     # Animal class above.
        #     animal = Animal(row['id'], row['name'], row['breed'],
        #                     row['status'], row['location_id'],
        #                     row['customer_id'])

        #     animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)

def get_animal_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.breed,
            c.status,
            c.location_id,
            c.customer_id
        from Animal c
        WHERE c.location_id = ?
        """, ( location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)