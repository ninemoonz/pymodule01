class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = ""
        self._height = 0
        self._age = 0
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, n: str) -> None:
        if len(n) == 0:
            print(f"\nInvalid Operation attempted: name \"{self._name}\" [REJECTED]")
            print(f"Security: No name rejected\n")
            return
        self._name = n
        print(f"Plant created: {self._name}")

    
    def get_name(self) -> str:
        return self._name

    def set_height(self, h: int) -> None:
        if h < 0:
            print(f"\nInvalid Operation attempted: height {h}cm [REJECTED]")
            print(f"Security: Negative height rejected\n")
            return 
        self._height = h
        print(f"Height Updated: {self._height}cm [OK]")

    def get_height(self) -> int:
        return self._height

    def set_age(self, a: int) -> None:
        if a < 0:
            print(f"\nInvalid Operation attempted: age {a} days [REJECTED]")
            print(f"Security: Negative age rejected\n")
            return
        self._age = a
        print(f"Age updated: {self._age} days [OK]")

    
    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current plant: {self._name} ({self._height}cm, {self._age} days)")

if __name__ == "__main__":
    def ft_garden_security():
        print("=== Garden Security System ===")
        plant1 = SecurePlant("Rose", 10, 11)
        plant1.set_age(-1)
        plant1.get_info()


ft_garden_security()
