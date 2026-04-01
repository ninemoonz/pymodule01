class SecurePlant:
    def __init__(self, height: int, age: int):
        self._height = 0
        self._age = 0

    def set_height(self, x: int):
        self._height = x

    def get_height(self):
        if self._height > 0:
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


plant1 = SecurePlant(0, 0)
plant1.set_height(12)
plant1.set_age(10)


def ft_garden_security():
    print('=== Garden Security System ===')
    plant1.get_height()
    plant1.get_age()


ft_garden_security()
