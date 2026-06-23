# Read the text from the file using readlines which makes the list of text in file.

fp = open("temp.txt","r")

if (fp):
    print("File loaded successfully! ")
else:
    print("File not loaded! ")

print(fp.readlines())
fp.close()