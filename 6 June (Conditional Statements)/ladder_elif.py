name = input("Enter the name of student: ")
sub1 = int(input("Enter the marks in subject 1: "))
sub2 = int(input("Enter the marks in subject 2: "))

total = sub1 + sub2
percentage = total/200*100

print("\n")
print("<----------------------------------------------------------------------->")
print("Name of the student = ", name)
print("Marks in Subject 1 = ", sub1)
print("Marks in Subject 2 = ", sub2)
print("Total of marks in all the subjects = ", total)
print("Percentage = ", percentage, "%")
if(90 <= percentage <= 100):
    print("Grade: A")
elif(80 <= percentage < 90):
    print("Grade: B")
elif(70 <= percentage < 80):
    print("Grade: C")
elif(60 <= percentage < 70):
    print("Grade: D")
elif(50 <= percentage < 60):
    print("Grade: G")
elif(40 <= percentage < 50):
    print("Grade: H")
elif(33 <= percentage < 40):
    print("Grade: I")
else:
    print("Grade: Fail")