print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1 + name2
combined_name_lower = combined_name.lower()
t = combined_name_lower.count("t")
r = combined_name_lower.count("r")
u = combined_name_lower.count("u")
e = combined_name_lower.count("e")

true = t+r+u+e

l = combined_name_lower.count("l")
o = combined_name_lower.count("o")
v = combined_name_lower.count("v")
e = combined_name_lower.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score >90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >=40) and (love_score<=50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  