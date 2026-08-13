text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

# Display the reversed string
print("Reversed string:", reverse)
