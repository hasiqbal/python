# add a match case block

user_prompt = "Type add, view or exit: "
name_prompt = "Enter your name:"

names = []
while True:
    name = input(user_prompt)
    name = name.strip()

    match name:
        case 'add':
            name = input(name_prompt)
            names.append(name)
        case 'view':
            for items in names:
                print (items)
        case 'exit':
            break

print("This is your final list:", names, "Goodbye!")