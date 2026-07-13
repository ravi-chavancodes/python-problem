#Problem: Longest Consecutive Increasing Word
"""
sentence = input("Enter a sentence: ").split()

best = ""

for word in sentence:
    ok = True

    for i in range(len(word) - 1):
        if word[i] >= word[i + 1]:
            ok = False
            break

    if ok and len(word) > len(best):
        best = word

print("Answer:", best if best else "No valid word")
"""

# upper case lower case
"""
text = input("Enter text: ")

upper = sum(c.isupper() for c in text)
lower = sum(c.islower() for c in text)

print("Uppercase:", upper)
print("Lowercase:", lower)
"""

