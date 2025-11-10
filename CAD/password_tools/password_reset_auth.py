## waiting for firebase auth setup

from connection import db, auth
import requests

def send_password_reset_link(user_id: str):
    """
    Sends a Firebase password reset email to the user's registered email address.
    user_id: can be IC number or username stored in the 'patients' table.
    """

    try:
        # Step 1: Look up user in the 'patients' table
        patients = db.child("patients").get()
        user_email = None

        if not patients.each():
            print("[ERROR] No patient records found in database.")
            return False, "No patient records found."

        for patient in patients.each():
            data = patient.val()
            if data.get("patient_ic") == user_id or data.get("patient_username") == user_id:
                user_email = data.get("patient_email")
                break

        if not user_email:
            return False, f"No user found with ID: {user_id}"

        print(f"[INFO] Found user email: {user_email}")

        # # Step 2: Send Firebase Auth password reset email
        # auth.send_password_reset_email(user_email)
        # print(f"[INFO] Password reset email sent to {user_email}")
        # return True, f"Password reset email has been sent to {user_email}."
    
        # --- Try to send password reset email ---
        try:
            auth.send_password_reset_email(user_email)
            print("[SUCCESS] Firebase accepted password reset request.")
            return True, f"Password reset email sent to {user_email}"

        except requests.exceptions.HTTPError as http_err:
            # Firebase REST error (e.g., email not in Auth)
            error_json = http_err.response.json()
            print(f"[HTTP ERROR] Firebase response: {error_json}")
            return False, f"Firebase Error: {error_json}"

        except Exception as e:
            print(f"[ERROR] Exception in send_password_reset_email(): {e}")
            return False, f"Error sending reset email: {e}"

    except Exception as e:
        print(f"[ERROR] Failed to send password reset email: {e}")
        return False, f"Error: {e}"


# ---------------- TEST DEMO ----------------
if __name__ == "__main__":
    user_input = input("Enter your IC number or username: ").strip()
    success, message = send_password_reset_link(user_input)
    print(message)
