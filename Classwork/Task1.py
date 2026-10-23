#Classwork_Task1
#Mohammed Ahmed

import secrets
import string

def random_string(size:int = 10) -> str:
    # Create a pool to pick ascii characters from.
    pool = string.ascii_letters
    some_str = "".join(secrets.choice(pool) for _ in range (size))
    return some_str

def main():
    print(random_string())
    print(random_string(16))

if __name__ == "__main__":
    main()