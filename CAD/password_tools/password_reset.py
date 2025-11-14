from connection import db, auth
import requests


def send_password_reset_link(email):
    """Trigger Firebase Auth password reset email."""
    try:
        auth.send_password_reset_email(email)
        print(f"[INFO] Firebase password reset email sent to {email}")
        return True, f"Password reset email sent to {email}."
    except requests.exceptions.HTTPError as http_err:
        error_json = http_err.response.json()
        print(f"[HTTP ERROR] Firebase response: {error_json}")
        return False, f"Firebase Error: {error_json}"
    except Exception as e:
        print(f"[ERROR] Exception in send_password_reset_email(): {e}")
        return False, f"Error sending reset email: {e}"



# ---------------- TEST DEMO ----------------
if __name__ == "__main__":
    email = input("Enter your email: ").strip()
    success, msg = send_password_reset_link(email)
    print(msg)