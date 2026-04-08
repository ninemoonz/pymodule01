class Plant:
	def __init__(self, name: str, height: int) -> None:
		self.name = name
		self.height = height
		self.initial_height = height
		
	def grow(self):
		self.height += 1
		print(f"{self.name} grew 1cm")

	def get_info(self):
		return f"{self.name}: {self.height}"


class FloweringPlant(Plant):
	def __init__(self, name: str, height: int, color: str) -> None:
		super().__init__(name, height)
		self.color = color
		self.is_blooming: bool = False

	def bloom(self) -> None:
		self.is_blooming = True

	def get_info(self) -> None:
		if self.is_blooming:
			status = "blooming"
		else:
			status = "not blooming"
		return f"{self.name}: {self.height}cm, {self.color} flower ({status})"


class PrizeFlower(FloweringPlant):
	def __init__(self, name: str, height: int, color: str, prize: int) -> None:
		super().__init__(name, height, color)
		self.prize = height / 2

class Garden:
	def __init__(self, owner: str) -> None:
		self.owner = owner
		self.plants: list = []
	
	def add_plant(self, plant: Plant) -> None:
		self.plants.append(plant)
		print(f"Added {plant.name} to {self.owner}'s garden")
	
	def grow_all(self) -> None:
		print(f"{self.owner} is helping all plants grow...")
		for plant in self.plants:
			plant.grow()

	def get_report(self) -> None:
		...

	
class GardenManager:
	def __init__(self) -> None:
		self.gardens: list = []

	def add_garden(self, garden: Garden) -> None:
		self.gardens.append(garden)

	class GardenStats:
		...

	@classmethod
	def create_garden_network(cls, name: list) -> list:
		...
	
	@staticmethod
	def is_valid_height(height: int) -> bool:
		...


if __name__ == "__main__":
	def ft_garden_analytics():
		print("=== Garden Management System Demo")
		print()
		

	ft_garden_analytics()