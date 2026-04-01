class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, x: int):
       if x < 0:
           print(
                f"Invalid operation attempted: "
                f"height {self._height}cm [REJECTED]\n"
                f"Security: Negative height rejected"
            )
            return
        self._height = x

    def get_height(self):
        if self._height >= 0:
            return print(f"Height updated: {self._height}cm [OK]")
        else:
            return print(
                f"Invalid operation attempted: "
                f"height {self._height}cm [REJECTED]\n"
                f"Security: Negative height rejected"
            )

    def set_age(self, y: int):
        self._age = y

    def get_age(self):
        if self._age >= 0:
            return print(f"Age updated: {self._age} days [OK]")
        else:
            return print(
                f"Invalid operation attempted: "
                f"age {self._age} days [REJECTED]\n"
                f"Security: Negative age rejected"
            )

    def set_name(self, z: str):
        self._name = z

    def get_name(self):
        if len(self._name) == 0:
            return print(
                f"Invalid operation attempted: "
                f"No name [REJECTED]\n"
                f"Security: No plant name rejected"
            )
        else:
            return print(f"Plant created: {self._name}")

    def get_info(self):
        print(f"Current plant: {self._name} ({self._height}cm, {self._age} days)")

plant1 = SecurePlant("asdf" ,0, 0)
plant1.set_name("dasima")
plant1.set_height(12)
plant1.set_age(10)


def ft_garden_security():
    print("=== Garden Security System ===")
    plant1.get_name()
    plant1.get_height()
    plant1.get_age()
    plant1.get_info()

ft_garden_security()
