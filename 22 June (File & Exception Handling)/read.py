# Read the text from the file.

fp = open("temp.txt","r")

if (fp):
    print("File loaded successfully! ")
else:
    print("File not loaded! ")

print(fp.read())
fp.close()