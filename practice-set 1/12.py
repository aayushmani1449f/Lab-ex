sentence = input().lower()
vowel_count = 0

for char in sentence:
    if char in "aeiou":
        vowel_count = vowel_count + 1

print(vowel_count)