#Nested statement


number = int(input("Enter a number : "))

if number > 1:
    print("Your number is greater than 1")
    if number > 50:
        print("Your number is greater than 50")
    else:
        print("Your number is less than 50")
        if number < 30:
            print("Your number is less than 30")
            


print("This program is done!")