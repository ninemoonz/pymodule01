class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloom_state = False

    def bloom(self) -> None:
        self.bloom_state = True
        print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom_state:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{self.height:.1f}cm long and "
                f"{self.trunk_diameter:.1f}cm wide."
            )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f} cm")


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

    def vegetable_nut(self, grow_days: int) -> None:
        print(f"[make {self.name} grow and age for {grow_days} days]")
        self.nutritional_value += grow_days

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    rose = Flower("rose", 20, 14, "red")
    tulip = Flower("tulip", 24, 30, "pink")

    oak = Tree("oak", 400, 240, 30)
    ginkgo = Tree("ginkgo", 320, 120, 19)

    carrot = Vegetable("carrot", 14, 45, "November")
    broccoli = Vegetable("broccoli", 10, 20, "May")

    def garden_plant_types(flower: Flower, tree: Tree, vegetable: Vegetable):
        print("=== Garden Plant Types ===")
        print("=== Flower")
        flower.show()
        flower.bloom()
        flower.show()
        print()
        print("=== Tree")
        tree.show()
        tree.produce_shade()
        print()
        print("=== Vegetable")
        vegetable.show()
        vegetable.vegetable_nut(20)
        vegetable.show()

    garden_plant_types(rose, ginkgo, broccoli)
