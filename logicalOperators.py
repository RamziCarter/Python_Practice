#logical operators
# and, or, not
#is to check if two or more conditions are true
temperature = float(input("Enter the temperature from outside?: "))

if temperature >= 0 and temperature <= 30:
    print("It is nice enough outside to go and see the world")
    print("Go outside!")

elif temperature < 0 or temperature > 30:
    print("The temperature is not ideal today")
    print("I recommend you stay inside!")

#not turns the value opposite
#if not(temp > 0 and temp < 5) value 3
# turn value opposite of what it would be