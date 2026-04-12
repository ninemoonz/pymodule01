class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.stat = Plant.PlantStat(self.name)

    @staticmethod
    def check_year_old(plant_age: int) -> None:
        if plant_age > 365:
            print(f"Is {plant_age} days more than a year? -> True")
        else:
            print(f"Is {plant_age} days more than a year? -> False")

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("unknown", 0, 0)

    def grow(self) -> None:
        self.height += 6
        self.stat.grow_count += 1

    def age(self) -> None:
        self.days += 3
        self.stat.age_count += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")
        self.stat.show_count += 1

    class PlantStat:
        def __init__(self, name: str) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
            self.name = name

        def stat_info(self) -> None:
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, "
                  f"{self.show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom_stat = False

    def bloom_grow(self) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.bloom_stat = True
        self.grow()
        self.age()

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom_stat:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self.stat = Tree.TreeStat(self.name)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk:.1f}cm")

    def produce_shade(self) -> None:
        self.stat.shade += 1
        print(f"[asking the {self.name} to produce shade]")
        print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{self.height:.1f}cm long and "
                f"{self.trunk:.1f}cm wide."
            )

    class TreeStat(Plant.PlantStat):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self.shade = 0
        
        def stat_info(self) -> None:
            super().stat_info()
            print(f"{self.shade} shade")


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed = 0


if __name__ == "__main__":
    rose = Flower("rose", 13, 24, "red")
    oak = Tree("oak", 200, 456, 30)

    print("=== Garden statistics ===")
    print("Check year-old")
    Plant.check_year_old(20)
    Plant.check_year_old(365)
    print()
    print("=== Flower")
    rose.show()
    rose.stat.stat_info()
    rose.bloom_grow()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    oak.stat.stat_info()
    oak.produce_shade()
    oak.stat.stat_info()
