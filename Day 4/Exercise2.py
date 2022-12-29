import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
meal_buyer = random.randint(0, len(names)-1)
person_who_will_pay = names[meal_buyer]
print(person_who_will_pay + " is going to buy the meal today!")