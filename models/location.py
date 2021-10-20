class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, location_id, address):
        self.id = id
        self.location_id = location_id
        self.address = address

new_location = Location(3, 3, "213 Munber Ave")