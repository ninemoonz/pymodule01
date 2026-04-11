class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        if len(name) == 0:
            self._name = ""
        else:
            self._name = name
        if height < 0:
            self._height = 0
        else:
            self._height = height
        if age < 0:
            self._age = 0
        else:
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
            print("Height update rejected")
            return 
        self._height = height
        print(f"Height Updated: {self._height}cm")

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current state: {self._name}: "
              f"{self._height}cm, {self._age} days old")


if __name__ == "__main__":
    plant = SecurePlant("Rose", 24, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.get_name()}: "
          f"{plant.get_height()}cm, {plant.get_age()} days old")
    print()

    plant.set_height(30)
    plant.set_age(25)

    plant.get_height()
    plant.get_age()
    print()
    plant.set_height(-3)
    plant.set_age(-5)
    print()

    plant.get_info()
