print("Input two digits you want to combine")

Input1 = float(input())
Input2 = float(input())
Input3 = str()

print("Add Subtract Divide Multiply")
choose = input()
if(choose == "Add"):
    print(f"{Input1 + Input2}")

if(choose == "Subtract"):
    print(f"{Input1-Input2}")

if(choose == "Divide"):
    print("Quotient: " + f"{Input1 // Input2}")
    print("Remainder: " +  f"{Input1 % Input2}")

if(choose == "Multiply"):
    print(f"{Input1 * Input2}")

print("Good Job on using my calculator :)")