"""
file: main.py
author: Corban Pendrak
date: 4Mar24
purpose: Encode and decode 8-digit strings of numbers for Lab 6 of COP3502C
"""


# TODO: Create this function
def decode(encoded_password: str) -> str:
    pass


def encode(password: str) -> str:
    """
    Adds 3 to each digit in the password restrained by modulus 10.
    :param password: 8-digit integer password string
    :return: encoded password
    """
    return "".join(str((int(digit) + 3) % 10) for digit in password)


def main():
    # Main function
    encoded_password = ""
    while True:
        print("""
Menu
-------------
1. Encode 
2. Decode
3. Quit""")

        menu_option = input("Please enter an option: ")

        if menu_option == "1":
            # Encode password
            password = input("Please enter your password to encode: ")

            # Validate password
            if len(password) != 8 or not password.isdigit():
                print("ERROR: Password must be 8-digits and only integers.")

            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif menu_option == "2":
            # Display and decode password
            # Validation
            if encoded_password == "":
                print("ERROR: No encoded password stored.")

            password = decode(encoded_password)
            print(f"The encoded passoword is {encoded_password}, and "
                  f"the original password is {password}")
        elif menu_option == "3":
            # Quit program
            break


if __name__ == "__main__":
    # Basic testing
    programming = True
    fun = True
    assert programming is fun
    assert encode("12345555") == "45678888"
    assert decode("45678888") == "12345555"
    assert decode(encode("00009962")) == "00009962"
    assert encode(decode("00009962")) == "00009962"

    # Only run if main program
    main()
