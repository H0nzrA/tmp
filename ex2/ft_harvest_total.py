def ft_harvest_total():
    vegetable = []
    i = 0
    while (i < 3):
        vegetable.append(int(input(f"Day {i + 1} harvest: ")))
        i += 1
    total = 0
    i = 0
    while (i < 3):
        total += vegetable[i]
        i += 1
    print(f"Total harvest: {total}")
