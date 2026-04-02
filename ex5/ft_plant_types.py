class Plant:
	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age
	
	def get_info(self):
		print(f"name: {self.name}, height: {self.height}cm, age: {self.age} days")


class Flower(Plant):
	def __init__(self, name: str, height: int, age: int, color: str):
		super().__init__(name, height, age)
		self.color = color

	def bloom(self):
		print(self.name, "bloom")


class Tree(Plant):
	def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self, s: int):
		return s

class Vegetable(Plant):
	def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value
		

if __name__ == "__main__":
	def ft_plant_types():
		rose = Flower("Rose", 25, 30, "red")
		oak = Tree("Oak", 500, 1852, )
		print("=== Garden Plant Types ===")
