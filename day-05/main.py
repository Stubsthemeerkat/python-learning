def pass_check():
    password = input("Welcome to the password check system. Enter your password: ")

##Checks each criterion of the password and updates the final score accordingly
    def check_length(password):
        if len(password) >= 16:
            return True
        else:
            return False
    if check_length(password):
        print("Length: Passed")
    else:
        print("Length: Failed")

    def check_uppercase(password):
        return any(char.isupper() for char in password)
    if check_uppercase(password):
        print("Uppercase: Passed")
    else:
        print("Uppercase: Failed")

    def check_lower(password):
        return any(char.islower() for char in password)
    if check_lower(password):
        print("Lowercase: Passed")
    else:
        print("Lowercase: Failed")

    def check_digit(password):
        return any(char.isdigit() for char in password)
    if check_digit(password):
        print("Digit: Passed")
    else:
        print("Digit: Failed")

    def check_punctuation(password):
        return any(char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for char in password)
    if check_punctuation(password):
        print("Punctuation: Passed")
    else:
        print("Punctuation: Failed")
# ##Checks final score of password strength

    def calculate_score(password):
        score = 0
        if check_length(password):
            score += 1
        if check_uppercase(password):
            score += 1
        if check_lower(password):
            score += 1
        if check_digit(password):
            score += 1
        if check_punctuation(password):
            score += 1
        return score

    final_score = calculate_score(password)
    print("Final score:", final_score)

pass_check()