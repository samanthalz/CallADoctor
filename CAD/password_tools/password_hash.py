import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.
    Returns the hashed password as bytes.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def verify_password(password: str, hashed: bytes) -> bool:
    """
    Verifies a plaintext password against a hashed one.
    Returns True if they match, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


def main():
    print("=== Password Hash Demo ===")
    password = input("Enter a password to test: ")

    print("\nHashing password...")
    hashed_pw = hash_password(password)
    print(f"Hashed password (stored securely): {hashed_pw.decode('utf-8')}")

    # Verify password
    verify_input = input("\nRe-enter password to verify: ")
    if verify_password(verify_input, hashed_pw):
        print("Password verified successfully!")
    else:
        print("Password verification failed.")



if __name__ == "__main__":
    main()