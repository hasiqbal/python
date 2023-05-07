# a program that prompts the user to input their name repeatedly.
# Then, the program repeatedly prints out the name with the first letter capitalized.
# The name is added to a list and printed

user_prompt = "Enter your name: "
names = []
while True:
    name = input(user_prompt)
    names.append(name)
    print(names)
