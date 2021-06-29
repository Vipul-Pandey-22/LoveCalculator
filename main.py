# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

string = name1 + name2
combined_str = string.lower()

t = combined_str.count("t")
r = combined_str.count("r")
u = combined_str.count("u")
e = combined_str.count("e")

TRUE = t + r + u + e

l = combined_str.count("l")
o = combined_str.count("o")
v = combined_str.count("v")
e = combined_str.count("e")

LOVE = l + o + v + e

love_score = int(str(TRUE)+str(LOVE))
# print(love_score)

if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go to together coke and mentos.")

elif (love_score >=40) and (love_score <=50):
  print(f"Your love score is {love_score}, you are alright together.")

else:
  print(f"Your love score is {love_score}")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇


