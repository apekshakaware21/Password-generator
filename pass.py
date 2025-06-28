import random
import string
import pyperclip


def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected!")

    while True:
        password = ''.join(random.choice(char_pool) for _ in range(length))
        # Ensure password contains at least one of each selected type
        if ( (not use_upper or any(c.isupper() for c in password)) and
             (not use_lower or any(c.islower() for c in password)) and
             (not use_digits or any(c.isdigit() for c in password)) and
             (not use_symbols or any(c in string.punctuation for c in password)) ):
            return password


def save_passwords(passwords, filename='passwords.txt'):
    with open(filename, 'w') as file:
        for pwd in passwords:
            file.write(pwd + '\n')
    print(f"✅ Passwords saved to {filename}")


def main():
    print("🔐 Secure Password Generator 🔐")
    num = int(input("How many passwords to generate?: "))
    length = int(input("Enter password length (Recommended 12-20): "))

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    passwords = []

    for _ in range(num):
        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"🔑 {pwd}")
        passwords.append(pwd)

    # Copy last password to clipboard
    pyperclip.copy(passwords[-1])
    print("📋 Last password copied to clipboard!")

    # Save to file
    save = input("Do you want to save the passwords to a file? (y/n): ").lower()
    if save == 'y':
        save_passwords(passwords)

    print("🎉 Done! Stay safe!")

if __name__ == "__main__":
    main()
