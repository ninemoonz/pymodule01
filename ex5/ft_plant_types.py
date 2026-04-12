class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloom_state = False

    def flower_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        self.bloom_state = True
        print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom_state:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def tree_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        shade = (self.trunk_diameter / 100) * (self.height / 100)
        print(
                f"{self.name} now produces a shade of {shade:.0f}cm long and "
                f"{self.trunk_diameter}cm wide"
            )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter} cm")


class Vegetable(Plant):
    def __init__(
            self, name: str,
            height: int,
            age: int,
            harvest_season: str
            ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def vegetable_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")

    def vegetable_nut(self, grow_days: int) -> None:
        print(f"[make {self.name} grow and age for {grow_days} days]")
        self.nutritional_value += grow_days

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 20, 14, "red")
    tulip = Flower("Tulip", 24, 30, "pink")

    oak = Tree("Oak", 400, 240, 30)
    ginkgo = Tree("Ginkgo", 320, 120, 19)

    carrot = Vegetable("Carrot", 14, 45, "November")
    broccoli = Vegetable("Broccoli", 10, 20, "May")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    carrot.show()
    carrot.vegetable_nut(20)
    carrot.show()
