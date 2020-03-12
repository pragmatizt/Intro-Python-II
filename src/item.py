# Implement an item class to hold item information.

def Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.