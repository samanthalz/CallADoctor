import re
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



def main():
    print("=== Password Strength Demo ===")
    password = input("Enter a password to test: ")

    # Check strength
    print("\nChecking password strength...")
    strength_result = check_password_strength(password)
    print(strength_result)


if __name__ == "__main__":
    main()
