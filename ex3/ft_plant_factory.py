class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        if self.name == "Potato":
            self.height += 3
        elif self.name == "Tomato":
            self.height += 2
        elif self.name == "Bamboo":
            self.height += 15
        else:
            self.height += 1

    def get_info(self):
        print(
            f"Created: {self.name}: "
            f"{self.height}cm, {self.age} days old"
            )


def ft_plant_factory(plants: list[Plant]):
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.get_info()


if __name__ == "__main__":
    plants = [
        Plant("Bamboo", 20, 45),
        Plant("Rose", 28, 12),
        Plant("Tomato", 35, 20),
        Plant("Strawberry", 22, 84),
        Plant("Pepper", 44, 42)
    ]

    ft_plant_factory(plants)
