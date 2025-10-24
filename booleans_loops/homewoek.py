# Task 1
# vegetable = input("enter your favorite vegetable here:")
# if len(vegetable) < 2:
#   result = ""
# else: result = vegetable[:2] + vegetable[-2:]

# print(result)

# Task 2
# phone_nr = input("on wich number can we call you? 10 digits: ")

# if len(phone_nr) == 10 and phone_nr.isdigit():
#   print("your nr is valid")
# else:
#   print("enter a valid phone number")

# Task 3
my_name = "gaby"
user_name = input("whats your name? ").strip() #strip is to remove other unnecessary characters like space

if user_name.lower() == my_name:
  print(True)
else:
  print(False)

