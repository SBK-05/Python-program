#  average program
#  1
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1, 2):
    sum = sum + i

print("Sum =", sum)

#2
n = int(input("Enter n: "))

sum = 0

for i in range(2, n + 1, 2):
    sum = sum + i

print("Sum =", sum)

#3
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print(i)

#4
n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c    

#5
n = int(input("Enter n: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)    
