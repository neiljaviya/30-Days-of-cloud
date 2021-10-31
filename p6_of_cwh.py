#Grad Table of students
m=int(input("Hey, Enter Your Marks out of 100\n"))

if(m>90):
    print("Excellent")
elif(m>80 and m<=90):
    print("A")
elif(m>60 and m<=80):
    print("B")
elif(m>45 and m<=60):
    print("C")
elif(m>35 and m<=45):
    print("D")
else:
    print("Sorry!, You are fail")

