print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Enter text:")
print("Character to find: r")
for letter in text:
    if letter == 'r': 
        count += 1    
print(f"{count} letters 'r' found in '{text}'")