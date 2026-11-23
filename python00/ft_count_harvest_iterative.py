def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count_days(current):
        if current > days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count_days(current + 1)

    count_days(1)
