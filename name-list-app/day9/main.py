user_prompt = "Type add, show, edit, remove, or exit: "
name_prompt = "Enter your name:"
edit_prompt = "Number of item in the list to edit?:"
new_name = "What is the new name?:"
remove_name = "Which number name to remove?:"



while True:
    name = input(user_prompt)
    name = name.strip()
    

    if name.startswith('add'):
        newName = name[4:]
        with open('names.txt', 'r') as file:
            names = file.readlines()

        names.append(newName + '\n')

        with open('names.txt', 'w') as file:
            file.writelines(names)

    elif name.startswith('show'):
        with open('names.txt', 'r') as file:
            names = file.readlines()

        for index, item in enumerate(names):
            item = item.strip("\n")
            row = f"{index+1} - {item}"
            print(row)

    elif name.startswith('edit'):
        try: 
            edit_number = int(name[5:])
            edit_number = edit_number - 1

            with open('names.txt', 'r') as file:
                names = file.readlines()

            edited_name = input(new_name)
            names[edit_number] = edited_name + '\n'

            with open('names.txt', 'w') as file:
                file.writelines(names)
        except ValueError:
            print('Invalid value')
            continue

    elif name.startswith('remove'):
        try: 
            number_in_list = int(name[7:])

            with open('names.txt', 'r') as file:
                names = file.readlines()

                names = [name.strip('\n') for name in names]

            index = (number_in_list - 1)
            name_to_remove = names[index].strip('\n')
            names.pop(index)

            with open('names.txt', 'w') as file:
                file.writelines(names)

            message = f"Name {name_to_remove} was removed from the list"
            print(message)
        
        except IndexError:
            print('Index not in list')
            continue

    elif name.startswith('exit'):
        break
    else:
        print("Command not valid")

print("This is your final list:", names, "Goodbye!")
