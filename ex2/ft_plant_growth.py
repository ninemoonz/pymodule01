class plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        if self.name == "potato":
            self.height += 2
        elif self.name == "tomato":
            self.height = self.height + 5
        elif self.name == "rose":
            self.height + 3

    def age_day(self):
        self.age += 1

    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = plant("potato", 27, 30)
plant2 = plant("tomato", 30, 14)
plant3 = plant("rose", 23, 15)


def ft_plant_growth():
    start_height = plant2.height
    print("=== Day 1 ===")
    print(plant2.get_info())

    for day in range(7):
        plant2.grow()
        plant2.age_day()

    print("=== Day 7===")
    print(plant2.get_info())
    height_result = plant2.height - start_height
    print(f"Growth this week: +{height_result} cm")


ft_plant_growth()
