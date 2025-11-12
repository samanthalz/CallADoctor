import re
# import bcrypt
from zxcvbn import zxcvbn


def check_password_strength(password: str) -> str:
    """
    Check password strength based on multiple criteria.
    Returns a message indicating strength or issues.
    """
    min_length = 8
    errors = []

    if len(password) < min_length:
        errors.append(
            f"Password must be at least {min_length} characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain at least one special character.")

    pw_strength = check_password_strength2(password)

    if pw_strength['score'] <= 2: 
        errors.append("Password Not Strong Enough")

    if errors:
        return "Weak Password:\n" + "\n".join(f"- {err}" for err in errors)
    else:
        return "Strong Password"


def check_password_strength2(password: str):
    """
    Check password strength using zxcvbn.
    Ranks password strength based on commonly used password patterns
    """
    result = zxcvbn(password)

    print(f"Password score: {result['score']}")
    print(f"Feedback: {result['feedback']['suggestions']}")
    print(
        f"Crack time estimate: "
        f"{result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

    return result


# def hash_password(password: str) -> bytes:
#     """
#     Hashes a password using bcrypt.
#     Returns the hashed password as bytes.
#     """
#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed


# def verify_password(password: str, hashed: bytes) -> bool:
#     """
#     Verifies a plaintext password against a hashed one.
#     Returns True if they match, False otherwise.
#     """
#     return bcrypt.checkpw(password.encode('utf-8'), hashed)


def main():
    print("=== Password Strength Demo ===")
    password = input("Enter a password to test: ")

    # Check strength
    print("\nChecking password strength...")
    strength_result = check_password_strength(password)
    print(strength_result)

    # # If strong enough, hash it
    # if "Strong Password" in strength_result:
    #     print("\nHashing password...")
    #     hashed_pw = hash_password(password)
    #     print(f"Hashed password (stored securely): {hashed_pw.decode('utf-8')}")

    #     # Verify password
    #     verify_input = input("\nRe-enter password to verify: ")
    #     if verify_password(verify_input, hashed_pw):
    #         print("Password verified successfully!")
    #     else:
    #         print("Password verification failed.")
    # else:
    #     print("\nPlease choose a stronger password before hashing.")


if __name__ == "__main__":
    main()
