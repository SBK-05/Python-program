#      while loop
#    Below Avarage Program
# 1
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)
    
#2
n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)

#3
n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)
#4
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)
