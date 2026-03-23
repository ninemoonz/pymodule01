class plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

plant1 = plant("potato", 20, 50)

print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")