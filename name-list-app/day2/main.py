# A program that prompts the user to input their name once. 
# Then, the program prints out the name once with the first letter capitalized.

user_prompt = "enter your name:"
name = input(user_prompt)
print(name.capitalize)

#a program that prompts the user to input their name once. 
# Then, the program repeatedly prints out the name with the first letter capitalized.

user_prompt = "Enter your name: "
name = input(user_prompt)
while True:
    print(name.capitalize())

#a program that prompts the user to input their name repeatedly. 
# Then, the program repeatedly prints out the name with the first letter capitalized.

user_prompt = "Enter your name: "
while True:
    name = input(user_prompt)
    print(name.capitalize())


