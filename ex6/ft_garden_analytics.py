class Plant:
	def __init__(self, name: str, height: int) -> None:
		self.name = name
		self.height = height


class FloweringPlant(Plant):
	def __init__(self, name: str, height: int, color: str):
		super().__init__(name, height)
		self.color = color


class PrizeFlower(FloweringPlant):
	def __init__(self, name: str, height: int, color: str, prize: int):
		super().__init__(name, height, color)
		self.prize = prize


class GardenManager:
	def __init__(self, manager_name: str):
		self.manager_name = manager_name

	def add_plant():
		...
	
	def grow_plant():
		...
	
	def get_report():
		...

	class GardenStats:
		...


if __name__ == "__main__":
	def ft_garden_analytics():
		...

	ft_garden_analytics()