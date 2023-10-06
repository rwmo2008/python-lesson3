#if statement
age = 10
if age == 10:
    print("ten")
print ("how's that?")

#with string
name = "me"
if name == "me":
    print("the same")

#different operators
letter = "C"

if letter < "D":
    print("less than D")
    
if letter > "B":
    print("greater than B")

#unicode order
if letter < "a":
    print ("less than a")

#else statement
if age >= 18:
    print("Congratulations!")
    print("You are old enough to vote.")
else:
    print("Sorry.")
    print("You are not old enough to vote.")

#multiple conditions
year = int(input("Enter year: "))
#if year == 1:
#    print("Freshman")
#if year == 2:
#    print("Sophomore")
#if year == 3:
#    print("Junior")
#if year == 4:
#    print("Senior")

#multiway if statement
#if year == 1:
#    print("Freshman")
#else:
#   if year == 2:
#        print("Sophomore")
#    else:
#        if year == 3:
#            print("Junior")
#        else:   
#            if year == 4:
#                print("Senior")

#elif statements
if year == 1:
    print("Freshman")
elif year == 2:
    print("Sophomore")
elif year == 3:
    print("Junior")
elif year == 4:
    print("Senior")
else:
    print("Invalid year.")
