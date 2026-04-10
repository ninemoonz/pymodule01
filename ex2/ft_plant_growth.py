class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        if self.name == "Potato":
            self.height += 3
        elif self.name == "Tomato":
            self.height += 2
        elif self.name == "Bamboo":
            self.height += 15
        else:
            self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def week_simulation(plant: Plant, days=7):
    init_height = plant.height
    print("=== Garden Plant Growth ===")
    for i in range(1, days + 1):
        plant1.get_info()
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
    print(f"Growth this week: {plant.height - init_height}cm")


if __name__ == "__main__":
    plant1 = Plant("Bamboo", 27, 30)
    plant2 = Plant("Tomato", 30, 14)
    plant3 = Plant("Rose", 23, 15)

    week_simulation(plant1)
