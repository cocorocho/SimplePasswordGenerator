import string, random, sys, time, pyperclip

alphabet = string.ascii_lowercase

digits = [str(i) for i in range(10)]

symbols = ["!", "@", ".", "*"]

choices = 1, 2, 3

password = list()

def generate_password(length):

    password.append(random.choice(alphabet).upper())

    for digit in range(length - 1):

        choice = random.choice(choices)

        total_digits = len([i for i in password if i.isdigit()])

        total_symbols = len([i for i in password if i in symbols])


        if choice == 1:

            password.append(random.choice(alphabet))

        elif choice == 2:

            if total_digits <= length / 3:

                password.append(random.choice(digits))

            elif total_symbols <= length / 4:

                password.append(random.choice(symbols))

            else:

                password.append(random.choice(alphabet))


        elif choice == 3:

            if total_symbols <= length / 4:

                password.append(random.choice(symbols))

            elif total_digits <= length / 3:

                password.append(random.choice(digits))

            else:

                password.append(random.choice(alphabet))
                  
         
    return "".join(password)
    


def get_input():
    
    while True:

        try:
            
            pw_length = int(input("Password Length: "))

            return pw_length

        except ValueError:

            print("\nYou must enter a number\n")

            continue

        except KeyboardInterrupt:

            sys.stdout.write("\nExiting")

            sys.exit(0)
            
        break   

pw_length = get_input()

def print_password():

    generated_password = generate_password(pw_length)

    pyperclip.copy(generated_password)

    clipboard_msg = "* Copied to clipboard *"

    sys.stdout.write("""

==================================================================


{}




{}                   


==================================================================

""".format(generated_password.center(66), clipboard_msg.center(66)))

print_password()

ask_restart = input("Press any key to generate new password, or press q to exit: ")


while True:
    
    if ask_restart.lower() == "q":

        sys.stdout.write("\nExiting")        

        sys.exit(0)

    else:

        password = list()

        pw_length = get_input()

        print_password()

        ask_restart = input("Press any key to generate new password, or press q to exit: ")

        

        

        

