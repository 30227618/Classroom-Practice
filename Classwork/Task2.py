#Classwork_Task2
#Mohammed Ahmed

import random

def generate_custom_email(full_name: str, domain: str )-> str:
    """
    Generates an email address in the format:
    [first_initial][lastname][random_number]@helpme.net
    The random number is between 8 and 121 (inclusive).
    """
    # Split the full name into a list of words (['bob', 'carter'])
    name_parts = full_name.lower().split()

    # check that we have two names
    if len(name_parts) < 2:
        # Handle cases where input doesn't have a first and last name
        raise ValueError(
            "Input string must contain at least a first and last name separated by a space."
        )

    first_name = name_parts[0]
    last_name = name_parts[-1] 

    # Extract the first initial
    first_initial = first_name[0]

    # Generate a random number between 8 and 121 (inclusive)
    random_num = random.randint(8, 121)

    # Assemble and return the final email string
    email = f"{first_initial}{last_name}{random_num}{domain}"

    return email

def main():
    print(generate_custom_email(full_name  ="Frank Abagnale",  domain= "@trustme.org"))
    print(generate_custom_email(domain= "@scrapmetal.org", full_name  ="victor lustig"))

if __name__ == "__main__":
    main()