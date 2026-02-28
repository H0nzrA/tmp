def print_recursion(iteration: int):
    if (iteration > 1):
        print_recursion(iteration - 1)
    print(f"Day {iteration}")


def ft_count_harvest_recursive():
    iter = int(input("Days until harvest: "))
    print_recursion(iter)
    print("Harvest time!")
