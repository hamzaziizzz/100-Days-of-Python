# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90 - age
days = years * 365
weeks = years * 52
months = years * 12

print("You have {} days, {} weeks, and {} months left.".format(days, weeks, months))