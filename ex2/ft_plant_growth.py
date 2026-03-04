#!/usr/bin/python3


class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = age

    def get_info(self):
        p = f"{self.name.capitalize()}: {self.height} cm, {self.current_age} days old"
        print(p)

    def grow(self, height: int, day: int):
        temp = self.height
        if (day < 0):
            return
        i = 1
        while (i < day):
            self.height += height
            self.current_age += 1
            i += 1
        print(f"Growth this week: +{self.height - temp}cm")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    rose.grow(2, 8)
    print("=== Day 7 ===")
    rose.get_info()
