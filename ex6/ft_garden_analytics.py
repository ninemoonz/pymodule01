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
	def __init__(self, name: str, height: int, color: str, prize: int) -> None:
		super().__init__(name, height, color)
		self.prize = prize

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
		print(f"=== {self.owner}'s Garden Report ===")
		print("Plants in garden:")
		for plant in self.plants:
			print(f"- {plant.get_info()}")

	
class GardenManager:
	def __init__(self) -> None:
		self.gardens: list = []

	def add_garden(self, garden: Garden) -> None:
		self.gardens.append(garden)

	class GardenStats:
		def __init__(self) -> None:
			...

	@classmethod
	def create_garden_network(cls, name: list) -> list:
		...
	
	@staticmethod
	def is_valid_height(height: int) -> bool:
		return height >= 0


if __name__ == "__main__":
	def ft_garden_analytics():
		print("=== Garden Management System Demo")
		print()
		tyler = Garden("Tyler")
		tree = Plant("Oak tree", 340)
		rose = FloweringPlant("Rose", 20, "red")
		sun = PrizeFlower("Tulip", 30, "blue", 40)
		tyler.add_plant(tree)
		tyler.add_plant(rose)
		tyler.add_plant(sun)
		print()
		tyler.grow_all(3)
		print()
		tyler.get_report()


	ft_garden_analytics()