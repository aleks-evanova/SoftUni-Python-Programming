# Validating usernames and passwords using REGEX

import re

number_of_inputs = int(input())
successful_registration_count = 0

for user_input in range(number_of_inputs):
    username_password = input()

    pattern = r'([U]\$)([A-Z]{1}[a-z]{2,})\1([P]\@\$)([a-z]{5,}\d{1,})([P]\@\$)'
    username_pass_validation = re.search(pattern, username_password)
    if username_pass_validation:
        successful_registration_count += 1
        username = username_pass_validation.group(2)
        password = username_pass_validation.group(4)
        print('Registration was successful')
        print(f'Username: {username}, Password: {password}')
    else:
        print('Invalid username or password')

print(f"Successful registrations: {successful_registration_count}")