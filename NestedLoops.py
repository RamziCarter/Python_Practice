#Nested Loops

Rows = int(input("How many rows would you like in your shape?: "))
Columns = int(input("How many columns would you like in your shape?: "))
symbol = (input("What symbold do you want to use?: "))

for i in range(Rows):
    for j in range(Columns):
        print(symbol, end="")
    print()
