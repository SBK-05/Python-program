text = input("Enter a string: ")

char = input("Enter the character to count: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("The character", char, "appears", count, "times.")
