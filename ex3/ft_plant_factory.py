class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(
            f"Created: {self.name.capitalize()}"
            f"({self.height}cm, {self.age} days)"
            )

def ft_plant_factory():
    plants = [
        Plant("potato", 20, 45),
        Plant("rose", 28, 12),
        Plant("tomato", 35, 20),
        Plant("strawberry", 22, 84),
        Plant("pepper", 44, 42)
    ]

    print("=== Plant Factory Output ===")
    for i, plant in enumerate(plants):
        plant.get_info()
    
    print(f"\nTotal plants created: {len(plants)}")

if __name__ == "__main__":
    ft_plant_factory()
