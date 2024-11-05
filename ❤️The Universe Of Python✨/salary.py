salary=int(input("Enter you salary:"))
age=int(input("Enter you age:"))
if(salary>=2000 or age<=25):
    loan=input("Enter the loan ammount:")
    if(loan<=50000):
        print("you are eligible for loan")
    elif(loan>50000):
        print("maximum loan amount is 50000")
else:
    print("You are not eligible for loan")