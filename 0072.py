num = int(input("guess the number:"))

if num % 10 == 0:
    print(f"{num} It is a multiple of 10")
else:
    print(f"{num} It is not a multiple of 10")
