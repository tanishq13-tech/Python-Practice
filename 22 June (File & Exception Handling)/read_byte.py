# Read the text from the file upto how much byte given.

fp = open("temp.txt","r")

if (fp):
    print("File loaded successfully! ")
else:
    print("File not loaded! ")

print(fp.read(4))
fp.close()