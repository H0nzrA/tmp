#!/usr/bin/python3


class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    print("=== Garden plant Registry ===")
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()
