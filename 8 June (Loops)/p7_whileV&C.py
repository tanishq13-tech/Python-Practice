name = "Tanishq"
vowels = set("aeiou")
v_count = 0
c_count = 0
name_lower = name.lower()
i = 0
while i < len(name_lower):
    ch = name_lower[i]
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
    i += 1

print("Number of vowels:", v_count)
print("Number of consonants:", c_count)