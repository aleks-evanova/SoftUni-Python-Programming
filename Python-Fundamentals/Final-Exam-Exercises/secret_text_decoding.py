concealed_message = input()


while True:

    command = input().split(':|:')

    if command[0] == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break

    if command[0] == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]

        print(concealed_message)

    elif command[0] == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message = concealed_message + substring[::-1]
        else:
            print("error")
        print(concealed_message)

    elif command[0] == "ChangeAll":
        find_substring = command[1]
        replacement = command[2]
        concealed_message = concealed_message.replace(find_substring, replacement)
        print(concealed_message)






