def main():
    for index in range(1, 101):
        divisible_by_three = index % 3 == 0
        divisible_by_five = index % 5 == 0
        if divisible_by_three and divisible_by_five:
            print("Fizzbuzz")
        elif divisible_by_three:
            print("Fizz")
        elif divisible_by_five:
            print("buzz")
        else:
            print(index)

if __name__ == "__main__":
    main ()
    