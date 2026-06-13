# Q1 Accept two numbers and print the greatest between them.
# Input: 14, 7
# Output: 14 is greater
# if 14 > 7:
#     print(" 14 is greater")
# else:
#     print("Koi numabe nahi hai ")


# Q2. Accept gender from user and print a greeting message.
# Input: M
# Output: Good Morning Sir

# mag = input("please imtar the M ");
# if mag == 'm'or mag == 'M':
#     print("good Morning Manish");
# else:
#     print("please entar the M");


# Q3 Accept an integer and check if it is even or odd.
# Input: 9
# Output: 9 is Odd

# num = int(input("please entar the numaber "));
# if num % 2 == 0:
#     print("this is a sum number");
# else:
#     print("this is a odd numar");



# Q4 Accept name and age — check if the user is a valid voter (18+).
# Input: manish, 21
# Output: Hello Shery, you are a valid voter ✅

# name = "Manish"
# age = int(input("please entar the numaber "));
# if age >= 18:
#     print(f"hame {name} jo ki voat de sakte hai");
# else:
#     print("not a voat");


# Q5 Accept a year and check if it is a leap year.
# Input: 2024
# Output: 2024 is a leap year ✅

# year = int(input("intar the valide year "));

# if year % 4 == 0 and 1000 <= year <= 9999:
#     print(f"{year} is a leap year ");
# else:
#     print("noy a leap year");



# Q6 — Temperature Ladder Accept temperature in °C and print a description.
# Input: -5 Freezing Cold 🥶
# Input: 25 Pleasant 😊
# Input: 45 Very Hot 🔥

temp = int(input("intar the Temperature "));
if 10 >= temp:
    print("Freezing Cold 🥶")
elif 25 >= temp and 11 <= temp:
    print("Pleasant 😊");
elif 37 >= temp and 26 <= temp:
    print(" Hot🔥");
elif temp >=38:
    print("Very Hot 🔥");
else:
    print("please entar the valid number");

