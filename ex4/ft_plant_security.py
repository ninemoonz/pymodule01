class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = ""
        self._height = 0
        self._age = 0
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str) -> None:
        if len(name) == 0:
            print(f"\nInvalid Operation attempted: name \"{self._name}\" [REJECTED]")
            print(f"Security: No name rejected\n")
            return
        self._name = name
    
    def get_name(self) -> str:
        return self._name

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print(f"Height update rejected\n")
            return 
        self._height = height
        print(f"Height Updated: {self._height}cm [OK]")

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print(f"Age update rejected\n")
            return
        self._age = age
        print(f"Age updated: {self._age} days [OK]")

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current state: {self._name}: {self._height}cm, {self._age} days old")

<<<<<<< HEAD
if __name__ == "__main__":
    def ft_garden_security():
        print("=== Garden Security System ===")
        plant1 = SecurePlant("Rose", 10, 11)
        plant1.set_age(-1)
        plant1.get_info()
=======

def ft_garden_security(name: str, height: int, age: int):
    plant = SecurePlant(name, height, age)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.get_name()}: {plant.get_height()}cm, {plant.get_age()} days old")
    print()
    plant.set_height(height)
    plant.get_height()
    plant.set_age(age)
    plant.get_age()
    print()
    plant.get_info()
>>>>>>> 6860722b21db06a6f941304024aacb689261b6a6

if __name__ == "__main__":
    ft_garden_security("Rose", 23, 43)
