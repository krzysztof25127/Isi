# Za pomocą pętli stworzyć 1000 losowych 6 znakowych wyrazów [A-Z][a-z][0-9] i zapisać je do pliku passwords.txt.

import random
def generate_random_password(length=6):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))


def save_passwords_to_file(file_path, count=1000):
    with open(file_path, 'w') as file:
        for _ in range(count):
            password = generate_random_password()
            file.write(password + '\n')


if __name__ == "__main__":
    save_passwords_to_file('passwords.txt')