class SecurePlant:
	def __init__(self, name: str, height: int):
		self.name = name
		self._height = height

	def get_height(self):
		if self._height > 0:
			return self.height
		else:
			print(f"Invalid operation attempted: height {self._height}cm [REJECTED]")

	def set_height(self, x):
		self._height = get_height(x)

def ft_garden_security():
	plant1 = SecurePlant("tomato", 0)
	plant1.get_height(22)
	print(plant1._height)
	print(plant1.get_height)

ft_garden_security()