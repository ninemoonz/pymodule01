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
plant2 = plant("tomato", 32, 50)
plant3 = plant("carrot", 20, 42)


def ft_plant_growth():
    days = int(input("how many days will you grow plants?: "))
    print("=== Day 1 ===")
    print(plant1.get_info())

    for day in range(days):
        plant1.grow(1)
        plant1.age_day()

    print("=== Day 7===")
    print(plant1.get_info())

ft_plant_growth()
