#!/usr/bin/python3

class Plant:

    def __init__(
            self,
            garden: str,
            plant_name: str,
            height: int,
            age: int) -> None:
        self.garden = garden
        self.name = plant_name
        self.height = height
        self.age = age

    def print_garden_info(self):
        print(f"=== Welcome to {garden} ===")
        print(f"Plant: {self.name.capitalize()}")
        print(f"Height: {self.height} cm")
        print(f"Age: {self.age} days")
        print("\n=== End of Program ===")


if __name__ == "__main__":
    garden = "Plant Lab"
    name = "Rose"
    height = 15
    age = 18
    plant = Plant(garden, name, height, age)
    plant.print_garden_info()
