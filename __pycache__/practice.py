#Problem: Longest Consecutive Increasing Word

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