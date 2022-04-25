#Q1 average of three numbers
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
avg=(n1+n2+n3)/3
print("Average of three number",avg)

#Q2 Incomr Tax
gross_income=int(input("Enter gross income"))
dependent=int(input("Number of dependents"))
tax_income=gross_income-10000-(dependent*3000)
tax=0.2*tax_income
print("The person has to pay",tax,"to income tax officer")

#Q3 List 
n1=int(input("No of students"))
lts=["Name","Gender","Course Name","CGPA"]
for j in range(n1):
    nlts=[]
    SID=int("Enter SID:")
    Name=input("Enter SID:")
    Gender=input("Enter Name:")#Gender should be F/M and U for unknown
    Course_Name=input("Enter the Course:")
    CGPA=float("Enter CGPA")
    nlts.append(SID)
    nlts.append(Name)
    nlts.append(Gender)
    nlts.append(Course_Name)
    nlts.append(CGPA)
    print(lts)
    print(nlts)
    
#Q4 Marks of students
s1=float(input("Enter marks of first student="))
s2=float(input("Enter the marks of second student="))
s3=float(input("Enter the marks of third student="))
s4=float(input("Enter the marks of fourth student="))
s5=float(input("Enter the marks of fifth studdent="))
slst=[s1,s2,s3,s4,s5]
slst.sort()
print(slst)

#Q5
    #(a)
color=["Red","Green","White","Black","Pink","Yellow" ]
color.pop(3)
print(color)


    #(b)
color[3]="Purple" 
print(color)   