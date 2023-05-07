# add a match case block

user_prompt = "Type add, view, edit or exit: "
name_prompt = "Enter your name:"
edit_prompt =  "Number of item in list to edit:"
new_name = "What is the new name:"

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
        case 'edit':
            edit_number = int(input(edit_prompt))
            edit_number = edit_number - 1
            edited_name = input(new_name)
            names[edit_number] = edited_name
        case 'exit':
            break

print("This is your final list:", names, "Goodbye!")