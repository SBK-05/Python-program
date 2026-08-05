#1
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#2
n = int(input("Enter how many numbers: "))

largest = int(input("Enter number: "))

for i in range(1, n):
    num = int(input("Enter number: "))
    if num > largest:
        largest = num

print("Largest =", largest)    

#3
n = int(input("Enter how many numbers: "))

smallest = int(input("Enter number: "))

for i in range(1, n):
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num

print("Smallest =", smallest)
