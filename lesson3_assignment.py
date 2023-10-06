wind_speed = int(input("Enter wind speed: "))

if wind_speed >=74 and wind_speed < 96:
    print("Category 1 hurricane")
elif wind_speed >=96 and wind_speed < 111:
    print("Category 2 hurricane")
elif wind_speed >=111 and wind_speed < 131:
    print("Category 3 hurricane")
elif wind_speed >=131 and wind_speed < 156:
    print("Category 4 hurricane")
elif wind_speed >=156:
    print("Category 5 hurricane")
else:
    print("Invalid entry")
