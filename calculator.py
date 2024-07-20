print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1 = int(input("Enter the First value:-"))
num2 = int(input("Ener the Second value :-"))

opr = input("Enter the Opr...")
#condition 
if(opr == "+"):
    print(num1+num2)
elif(opr == "-"):
    print(num1-num2)
elif(opr == "*"):
    print(num1*num2)
elif(opr == "/"):
    print(num1/num2)
else:
    print("Invalid Operator4")