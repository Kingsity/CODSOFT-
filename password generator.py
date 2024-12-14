import random
import string

def generate_simple_password(length):
    """Generate a simple password with random uppercase and lowercase letters."""
    all_chars = string.ascii_letters  # Only letters
    return ''.join(random.choices(all_chars, k=length))

def generate_hard_password(length):
    """Generate a hard password with at least one uppercase letter, one lowercase letter, and one number."""
    if length < 3:
        print("Hard password length must be at least 3.")
        return None
    
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    password_chars += random.choices(string.ascii_letters + string.digits, k=length - 3)
    random.shuffle(password_chars)
    return ''.join(password_chars)

def generate_complicated_password(length):
    """Generate a complicated password with letters, numbers, and symbols."""
    if length < 4:
        print("Complicated password length must be at least 4.")
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one of each required character type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with a mix of all character types
    all_chars = lowercase + uppercase + digits + symbols
    password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle the list to ensure randomness
    random.shuffle(password_chars)

    return ''.join(password_chars)

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        complexity = input("\nChoose password complexity (Simple, Hard, Complicated): ").strip().lower()
        if complexity not in ['simple', 'hard', 'complicated']:
            print("Invalid choice. Please choose 'Simple', 'Hard', or 'Complicated'.")
            continue
        
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1 character.")
                continue
            
            if complexity == 'simple':
                password = generate_simple_password(length)
            elif complexity == 'hard':
                password = generate_hard_password(length)
            else:  # complicated
                password = generate_complicated_password(length)
            
            if password:
                print(f"\nGenerated Password: {password}")
            
            # Confirmation prompt
            continue_prompt = input("\nWould you like to generate another password? (yes/no): ").strip().lower()
            if continue_prompt != 'yes':
                print("Exiting the Password Generator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the application directly
main()