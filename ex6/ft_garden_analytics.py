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
        return cls("Unknown plant", 0, 0)

    def grow(self) -> None:
        self.stat.grow_increment()

    def age(self) -> None:
        self.days += 3
        self.stat.age_increment()

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")
        self.stat.show_increment()

    class PlantStat:
        def __init__(self, name: str) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self.name = name

        def grow_increment(self) -> None:
            self._grow_count += 1

        def age_increment(self) -> None:
            self._age_count += 1

        def show_increment(self) -> None:
            self._show_count += 1

        def stat_info(self) -> None:
            print(f"[statistics for {self.name.capitalize()}]")
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, "
                  f"{self._show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom_stat = False

    def grow(self) -> None:
        super().grow()
        self.height += 4

    def bloom(self) -> None:
        self.bloom_stat = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom_stat:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed = 0

    def grow(self) -> None:
        super().grow()
        self.height += 23

    def bloom(self) -> None:
        super().bloom()
        self.seed += 134

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed}")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self.stat = Tree.TreeStat(self.name)

    def grow(self) -> None:
        super().grow()
        self.height += 12

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


def display_stats(plant: Plant) -> None:
    plant.stat.stat_info()


if __name__ == "__main__":
    rose = Flower("rose", 13, 24, "red")
    oak = Tree("oak", 200, 456, 30)
    sun = Seed("sunflower", 145, 20, "yellow")

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year_old(20)
    Plant.check_year_old(366)
    print()

    print("=== Flower")
    rose.show()
    display_stats(rose)
    print(f"asking the {rose.name} to grow and bloom")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()
    
    print("=== Tree")
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print()
    print("=== Seed")
    sun.show()
    print(f"[make {sun.name} grow, age and bloom]")
    sun.bloom()
    sun.age()
    sun.grow()
    sun.show()
    display_stats(sun)
    print()
    print("=== Anonymous")
    unknown = Plant.anonymous_plant()
    unknown.show()
    display_stats(unknown)
