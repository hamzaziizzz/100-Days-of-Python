# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_of_heights = 0
for height in student_heights:
    sum_of_heights += height

average_height = round(sum_of_heights / len(student_heights))
print(average_height)
