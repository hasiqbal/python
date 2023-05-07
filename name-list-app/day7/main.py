 
user_prompt = "Type add, show, edit, complete or exit: "
name_prompt = "Enter your name:"
edit_prompt =  "Number of item in list to edit?:"
new_name = "What is the new name>:"
remove_name = "Which number name to remove?:"


while True:
    name = input(user_prompt)
    name = name.strip()

    match name:
        case 'add':
            name = input(name_prompt) + "\n"
            file = open('name-list-app/day6/names.txt','r')
            names = file.readlines()
            names.append(name)
            file = open('name-list-app/day6/names.txt', 'w')
            file.writelines(names)
            file.close()

        case 'show':
            file = open('name-list-app/day6/names.txt','r')
            names = file.readlines()
            file.close()
            
            for index, item in enumerate(names):
                item = item.strip("\n")
                row = f"{index+1} -{item}"
                print(row)
       
        case 'edit':
            edit_number = int(input(edit_prompt))
            edit_number = edit_number - 1
            edited_name = input(new_name)
            names[edit_number] = edited_name

        case 'complete':
            for item in names:
                number_in_list = int(input(remove_name)) - 1
                names.pop(number_in_list)
                
        case 'exit':
            break

print("This is your final list:", names, "Goodbye!")
