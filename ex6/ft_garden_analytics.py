class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self, grow: int) -> None:
        self.height += grow
        print(f"{self.name} grew {grow}cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def get_info(self) -> str:
        if self.is_blooming:
            status = "blooming"
        else:
            status = "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flower ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height, color)

    def get_score(self) -> int:
        if self.is_blooming:
            return self.height + 10
        return self.height

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Prize point: {self.get_score()}"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, grow: int) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(grow)

    def get_report(self) -> None:
        stats = GardenManager.GardenStats(self.plants)
        total = stats.total_growth()
        regular, flowering, prize = stats.count_types()

        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print()
        print(f"Plants added: {len(self.plants)}, Total growth: {total}cm")
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, "
            f"{prize} prize flowers"
            )


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def total_growth(self) -> int:
            total = 0
            for plant in self.plants:
                total += plant.height - plant.initial_height
            return total

        def count_types(self) -> tuple:
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def garden_scores(self) -> None:
        print("Garden scores - ", end="")
        for garden in self.gardens:
            score = 0
            for plant in garden.plants:
                score += plant.height
            print(f"{garden.owner}: {score} ", end="")

    @classmethod
    def create_garden_network(cls, names: list) -> "GardenManager":
        manager = cls()
        for name in names:
            manager.add_garden(Garden(name))
        return manager

    @staticmethod
    def is_valid_height(height: int) -> bool:
        return height >= 0


if __name__ == "__main__":
    def ft_garden_analytics():
        print("=== Garden Management System Demo")
        print()
        manager = GardenManager.create_garden_network(["Tyler", "Tara"])
        tyler = manager.gardens[0]
        tara = manager.gardens[1]

        tree = Plant("Oak tree", 174)
        rose = FloweringPlant("Rose", 20, "red")
        sun = PrizeFlower("Tulip", 15, "blue")
        rose.bloom()
        sun.bloom()
        tyler.add_plant(tree)
        tyler.add_plant(rose)
        tyler.add_plant(sun)
        tara.plants.append(tree)
        tara.plants.append(rose)
        print()

        tyler.grow_all(6)
        print()

        tyler.get_report()
        manager.garden_scores()
        print()

        all_valid = True
        for garden in manager.gardens:
            for plant in garden.plants:
                if not GardenManager.is_valid_height(plant.initial_height) \
                        or not GardenManager.is_valid_height(plant.height):
                    all_valid = False
        print()
        print(f"Height validation test: {all_valid}")
        print(f"Total gardens managed: {len(manager.gardens)}")

    ft_garden_analytics()
