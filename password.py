import random
import string
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to ensure complexity.")
        return None
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)
def main():
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
