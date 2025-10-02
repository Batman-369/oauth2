def even_odd_checker():
    numbers = []
    n = int(input("How many numbers do you want to check? "))
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        if num % 2 == 0:
            print(f"{num} is Even")
            numbers.append((num, "Even"))
        else:
            print(f"{num} is Odd")
            numbers.append((num, "Odd"))

    print("\nSummary:")
    for num, result in numbers:
        print(f"{num} --> {result}")

even_odd_checker()
