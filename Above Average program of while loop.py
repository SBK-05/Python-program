#1
n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

#2
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n%10
    sum = sum + digit
    n = n//10

print("Sum of digits =", sum)    

#3
n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

#4
n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)    
