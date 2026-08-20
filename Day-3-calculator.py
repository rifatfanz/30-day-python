#intro 
print("My Calculator")
print("By MHR")

while True:
    #1 First Input
    num1_input = input("Number 1: ")
    if num1_input.lower() == "exit":
        print(" Calculator Closed ")
        break
    try:
        num1 = float(num1_input)
    except ValueError:
        print("Wrong input. please insert a valid number")
        continue

    #2 Operation 
    print("(+) (-) (*) (/) or Exit ")
    op = input(" What will you do? ").lower()
    if op == "exit":
        print(" Calculator Closed ")
        break

    elif op in ["+", "-", "*", "/"]: 

        #3 Second Input
        num2_input = input("Number 2: ")
        if num2_input.lower() == "exit":
            print(" Calculator Closed ")
            break
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Wrong input. please insert a valid number")
            continue

        #4 Calculation Part
        if op == "+":
            print("Ans: ", num1 + num2)
        elif op == "-":
            print("Ans: ", num1 - num2)
        elif op == "*":
            print("Ans: ", num1 * num2)
        elif op == "/":
            if num2 != 0:  # age check koro 0 kina
                print("Ans: ", num1 / num2)
            else:
                print("Error: Infinity ") # 0 diye vag kora jay na
    else:
        print("Wrong Operation..!! + - * / Something of these")