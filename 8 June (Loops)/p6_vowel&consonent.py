name = "rishikesh"
li = ["a","e","i","o","u"]
count = 0

for i in name:
    if(i in li):
        count += 1
print("Number of vowels:",count)
print("Number of consonents:", len(name)-count)

