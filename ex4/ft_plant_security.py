class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_name(self, name: str) -> None:
        if len(name) == 0:
            print(f"\nInvalid Operation attempted: name "
                  f"\"{self._name}\" [REJECTED]")
            print("Security: No name rejected")
            return
        self._name = name
    
    def get_name(self) -> str:
        return self._name

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected\n")
            return 
        self._height = height
        print(f"Height Updated: {self._height}cm [OK]")

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days [OK]")

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current state: {self._name}: "
              f"{self._height}cm, {self._age} days old")


def ft_garden_security(name: str, height: int, age: int):
    plant = SecurePlant(name, height, age)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.get_name()}: "
          f"{plant.get_height()}cm, {plant.get_age()} days old")
    print()

    plant.set_height(height)
    plant.set_age(age)

    plant.get_height()
    plant.get_age()
    print()

    plant.get_info()


if __name__ == "__main__":
    ft_garden_security("Rose", 23, 43)
