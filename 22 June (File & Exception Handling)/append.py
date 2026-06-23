# Add text next to existing text using append (a)

fp = open("temp.txt","a")

if (fp):
    print("File loaded successfully! ")
else:
    print("File not loaded! ")

fp.writelines("Using Append")
fp.close()