
user_prompt = "Type add, show, edit, remove or exit: "
name_prompt = "Enter your name:"
edit_prompt = "Number of item in list to edit?:"
new_name = "What is the new name>:"
remove_name = "Which number name to remove?:"


while True:
    name = input(user_prompt)
    name = name.strip()

    match name:
        case 'add':
            name = input(name_prompt) + "\n"
            with open('names.txt', 'r') as file:
                names = file.readlines()

            names.append(name)

            with open('names.txt', 'w') as file:
                file.writelines(names)

        case 'show':
            with open('names.txt', 'r') as file:
                names = file.readlines()

            for index, item in enumerate(names):
                item = item.strip("\n")
                row = f"{index+1} -{item}"
                print(row)

        case 'edit':
            edit_number = int(input(edit_prompt))
            edit_number = edit_number - 1

            with open('names.txt', 'r') as file:
                names = file.readlines()

            edited_name = input(new_name)
            names[edit_number] = edited_name + '\n'

            with open('names.txt', 'w') as file:
                file.writelines(names)

        case 'remove':

            number_in_list = int(input(remove_name))

            with open('names.txt', 'r') as file:
                names = file.readlines()

            index = (number_in_list - 1)
            name_to_remove = names[index].strip('\n')
            names.pop(index)

            with open('names.txt', 'w') as file:
                file.writelines(names)

            message = f"Name {name_to_remove} was removed from list"
            print(message)

        case 'exit':
            break

print("This is your final list:", names, "Goodbye!")
