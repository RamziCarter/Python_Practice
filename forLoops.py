import time

#for loop is a statement that will execute a block a code a certain
#amount of times

#while loop = unlimited
#for loop = limited

#for i in range(36):
#    print(i)

for i in range(5, 11):
    if i > 5 and i < 11:
        print ("This is in the range 6 - 10: " + str(i))
    else:
        print(i)


for x in "Happy Birthday!":
    print(x)

for j in range(10, 0, -1):
    print(j)
    time.sleep(1) #cause delay between each iteration!
print("Happy Belated Birthday!!!!!!!!!")
