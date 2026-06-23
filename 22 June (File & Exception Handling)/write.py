# Create the file when file not exists.
# Or Re-write the exising file.

fp = open("temp.txt","w")

if (fp):
    print("File loaded successfully! ")
else:
    print("File not loaded! ")

fp.write("Date: 22/06/2026. ")
fp.write("Time: 13:30. ")
fp.write("I am learning file handling. ")
fp.close()