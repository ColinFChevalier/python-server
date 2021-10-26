class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

new_location = Location(3, "East", "213 Munber Ave")