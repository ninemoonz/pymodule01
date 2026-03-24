class plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int):
        self.height += cm

    def age_day(self):
        self.age += 1

    def get_info(self):
        return (
            self.name + ": " +
            str(self.height) + "cm, " +
            str(self.age) + " days old"
            )


plant1 = plant("potato", 27, 30)
start_height = plant1.height


def ft_plant_growth():
    days = int(input("how many days will you grow plants?: "))
    print("=== Day 1 ===")
    print(plant1.get_info())

    for day in range(days):
        plant1.grow(1)
        plant1.age_day()

    print("=== Day 7===")
    print(plant1.get_info())
    height_result = plant1.height - start_height
    print(f"Growth this week: +{height_result} cm")

ft_plant_growth()
