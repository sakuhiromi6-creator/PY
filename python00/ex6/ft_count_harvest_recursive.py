def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(current_day):
        print(f"Day {current_day}")

        if current_day == n:
            print("Harvest time!")
            return

        helper(current_day + 1)

    helper(1)

# if __name__ == "__main__":
#   ft_count_harvest_recursive()
