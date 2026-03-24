class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


plant1 = plant("potato", 20, 50)
plant2 = plant("tomato", 14, 24)
plant3 = plant("banana", 420, 140)
plants = [plant1, plant2, plant3]


def ft_garden_data():
    i = 0
    for i in range(3):
        print(
            f"{plants[i].name}: "
            f"{plants[i].height}cm, "
            f"{plants[i].age} days old"
            )
