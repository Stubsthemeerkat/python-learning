## Day 6: Going to be fixing organization and nested functions. Cleaning it up for readability
import getpass

##Checks the length of the password
def check_length(password):
    return len(password) >= 16

##Checks if the password contains at least one uppercase letter
def check_uppercase(password):
    return any(char.isupper() for char in password)

##Checks if the password contains at least one lowercase letter
def check_lower(password):
    return any(char.islower() for char in password)

##Checks if the password contains at least one digit
def check_digit(password):
    return any(char.isdigit() for char in password)

##Checks if the password contains at least one punctuation character
def check_punctuation(password):
    return any(char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for char in password)

def pass_check():
    user_input = getpass.getpass("Welcome to the password check system. Enter your password: ")

    results = {
        'Length': check_length(user_input),
        'Uppercase': check_uppercase(user_input),
        'Lowercase': check_lower(user_input),
        'Digit': check_digit(user_input),
        'Punctuation': check_punctuation(user_input)
    }
    print(f"Your final score is: {sum(results.values())}")
    for requirement, passed in results.items():
        if passed:
            print(f"{requirement}: Passed")
        else:
            print(f"{requirement}: Failed")
pass_check()

