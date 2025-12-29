import string
import getpass

def check_pwd():
        lower_count = 0
        upper_count = 0
        num_count = 0
        wspace_count = 0
        special_count= 0

        password = getpass.getpass("Enter your Password")
        strength = 0
        remarks = " "
        Lower_count = upper_count = num_count = wspace_count = special_count = 0

        for char in list(password):
            if char in string.ascii_lowercase:
                lower_count += 1

            elif char in string.ascii_uppercase:
                upper_count += 1
            elif char in string.digits:
                num_count += 1
            elif char == ' ':
                wspace_count += 1
            else:
                special_count += 1

        if lower_count >= 1:
            strength += 1
        if upper_count >=1:
            strength += 1
        if num_count >=1:
            strength += 1
        if wspace_count >=1:
            strength += 1
        if special_count >=1:
            strength += 1

        if strength == 1:
            remarks = "Very bad password please change it"
        elif strength == 2:
            remarks = "Not a good password"
        elif strength == 3:
            remarks = "Weak Password"
        elif strength == 4 :
            remarks = "Can be better"
        elif strength == 5:
            remarks = "Strong Password"

        print("Your Passowrd has : ")
        print(f"{lower_count} lowercase characters")
        print(f"{upper_count} uppercase characters")
        print(f"{num_count} numeric characters")
        print(f"{wspace_count} whitespace characters")
        print(f"{special_count} special characters")

        print("Password Strength is :{strength}")
        print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
        valid = False
        if another_pwd:
            choice = input ('Do you want to change password?":')
        else:
            choice = input('Do you want to check password strength(y/n)')
        while not valid:
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                return False
            else:
                print('Invalid, Try again')

if __name__ == '__main__':
    print("Welcome to password checker")
    user_response = ask_pwd()

    while check_pwd:
        check_pwd()
        check_status = ask_pwd(True)



                                                


