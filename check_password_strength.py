# TODO: Remove comments in production code
def check_password_strength(password:str)->bool:
    """
    Checks the strength of a given password based on specific criteria.
    A password is considered strong if it meets all the following conditions:
    1. Its length is between 8 and 16 characters (inclusive).
    2. It contains at least one uppercase letter.
    3. It contains at least one lowercase letter.
    4. It contains at least one digit.
    5. It contains at least one special character from the set {"!", "@", "#", "$", "%"}.
    Args:
        password (str): The password string to be checked.
    Returns:
        bool: True if the password meets all the strength criteria, False otherwise.
    """

    special_chars = {"!", "@", "#", "$", "%"}
    return (
        len(password)
        <= 16  # Guard clause that prevents password being more than 16 characters
        and len(password) >= 8  # Checks if password is less than 8 characters
        and any(
            c.isupper() for c in password
        )  # Checks if there is an uppercase character in password
        and any(
            c.islower() for c in password
        )  # Checks if there is an lowercase character in password
        and any(
            c.isdigit() for c in password
        )  # Checks is a digit is present in password
        and any(
            c in special_chars for c in password
        )  # Checks if the special characters defined above are present
    )  # This condition returns true only is all the criteria's are met


if __name__ == "__main__":
    password = input("Enter your password: ")
    if check_password_strength(password):
        print("Password is strong! It meets all the criteria.")
    else:
        print("Password does not meet the criteria. Here's why:")
        if len(password) < 8:
            print("- Must be at least 8 characters long.")
        if len(password) > 16:
            print("- Must be at least 8 characters long. less than 16")
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        if not (has_upper and has_lower):
            print("- Must contain both uppercase and lowercase letters.")
        if not any(c.isdigit() for c in password):
            print("- Must include at least one digit.")
        special_chars = {"!", "@", "#", "$", "%"}
        if not any(c in special_chars for c in password):
            print("- Must contain at least one special character from: !, @, #, $, %")
