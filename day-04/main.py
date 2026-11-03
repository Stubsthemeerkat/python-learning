def pass_check():
    password = input("Welcome to the password check system. Enter your password: ")
    final_score = 5

##Checks each criterion of the password and updates the final score accordingly
    if len(password) >= 16:
        print("Length: Passed")
    else:
        print("Length: Failed")
        final_score -= 1
    if any(char.isupper() for char in password):
        print("Uppercase: Passed")
    else:
        print("Uppercase: Failed")
        final_score -= 1
    if any(char.islower() for char in password):
        print("Lowercase: Passed")
    else:
        print("Lowercase: Failed")
        final_score -= 1
    if any(char.isdigit() for char in password):
        print("Digit: Passed")
    else:
        print("Digit: Failed")
        final_score -= 1
    if any(char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for char in password):
        print("Punctuation: Passed")
    else:
        print("Punctuation: Failed")
        final_score -= 1
    print("Final score:", final_score)

##Checks final score of password strength
    if final_score == 5:
        print("Password is very strong")
    elif final_score == 4:
        print("Password is strong")
    elif final_score == 3:
        print("Password is medium")
    elif final_score == 2:
        print("Password is weak")
    else:
        print("Password is very weak")

pass_check()
