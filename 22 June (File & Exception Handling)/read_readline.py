# Read the text from the file using readline.

fp = open("temp.txt","r")

if (fp):
    print("File loaded successfully! ")
else:
    print("File not loaded! ")

print(fp.readline())
fp.close()