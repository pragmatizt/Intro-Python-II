class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories

class Egg(Food):
    def __init__(self):
        super().__init__("egg", "This is an egg", 20)

class Ramen(Food):
    def __init__(self):
        super().__init__("ramen", "Delicious - and easy to make!", 25)


# class Weapon(Item):
#     def __init__(self, name, description, damage):
#         super().__init__(name, description)  # It looks like we don't need to include damage as a param in super()
#         self.damage = damage

# class Axe(Weapon):
#     def __init__(self):
#         super().__init__("axe", "built for splitting logs... and heads", 50)