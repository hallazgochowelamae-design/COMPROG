
def find_largest(n1, n2, n3):
    if n1 >= n2 and n1 >= n3a:
        return "n1", n1
    elif n2 >= n1 and n2 >= n3:
        return "n2", n2
    else:
        return "n3", n3

n1 = float(input("Enter your first number: "))
n2 = float(input("Enter your second number: "))
n3 = float(input("Enter your third number: "))


number, largest = find_largest(n1, n2, n3)

if largest.is_integer():
    largest = int(largest)

print(f"number {number} is the largest number with a value of {largest}")