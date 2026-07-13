def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(giorno_corrente):
        print(f"Day {giorno_corrente}")

        if giorno_corrente == n:
            print("Harvest time!")
            return

        helper(giorno_corrente + 1)

    helper(1)
