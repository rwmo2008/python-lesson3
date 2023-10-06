#multiple if conditions
age = int(input("How old are you? "))
registered = input("Are you registered (y/n) ")

#if age >= 18:
#    if registered == "y":


#and
if age >= 18 and registered == "y":
        print("You are ready to vote!")
else:
    print("You are not ready to vote.")

#or
if registered == "Y" or registered == "y":
    print("You are registered.")

