class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = False

    def flower_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom_state(self) -> None:
        self.bloom = True
        print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        print("=== Flower")
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Color: {self.color}")
        if self.bloom:
            print(f"{self.name} has bloomed")
        if not self.bloom:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def tree_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        shade = (self.trunk_diameter / 100) * (self.height / 100)
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    def __init__(
            self, name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def vegetable_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")

    def vegetable_nut(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    def ft_plant_types():
        rose = Flower("rose", 25, 30, "red")
        oak = Tree("Oak", 500, 1852, 50)
        carrot = Vegetable("Carrot", 15, 43, "winter", "Vitamin A")
        print("=== Garden Plant Types ===")
        print()
        rose.flower_info()
        rose.bloom()
        print()
        oak.tree_info()
        oak.produce_shade()
        print()
        carrot.vegetable_info()
        carrot.vegetable_nut()

    ft_plant_types()