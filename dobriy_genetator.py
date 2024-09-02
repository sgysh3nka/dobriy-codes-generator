import random
import string

def generate_code(length):
    letters = string.ascii_uppercase
    numbers = string.digits
    characters = letters + numbers
    code = ''.join(random.choices(characters, k=length))
    return code

def generate_codes_to_file(file_path, num_codes, code_length):
    with open(file_path, 'w') as file:
        for _ in range(num_codes):
            random_code = generate_code(code_length)
            file.write(random_code + '\n')

generate_codes_to_file('dobriy_codes.txt', 10, 7)
print("Success!")
print("Check dobriy_codes.txt")
input('Press enter to exit!')
