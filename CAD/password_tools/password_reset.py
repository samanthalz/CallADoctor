from connection import db, auth
import random
import time
from datetime import datetime, timedelta
import requests
import yagmail

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
app_email = os.getenv("APP_EMAIL")
app_password = os.getenv("APP_PW")

# ---------------- EMAIL CONFIG ----------------
yag = yagmail.SMTP(
    user=app_email,
    password=app_password,
    host='smtp.gmail.com',
    port=465,
    smtp_starttls=False,
    smtp_ssl=True
)

# ---------------- OTP FUNCTIONS ----------------
def send_email_otp(email):
    """Generate, send, and store OTP in Firebase."""
    otp = random.randint(1000, 9999)
    expiry_time = datetime.now() + timedelta(minutes=5)
    expiry_timestamp = int(expiry_time.timestamp())

    # Send OTP email
    subject = "Your Verification OTP"
    contents = f"Your OTP code is {otp}. It expires in 5 minutes."
    ## yag.send(to=email, subject=subject, contents=contents)
    print(f"[INFO] Sent OTP to {email}: {otp}")
    print(f"{subject}: {contents}")

    # Store OTP in Firebase
    data = {
        "email": email,
        "otp": str(otp),
        "expiry": expiry_timestamp
    }
    db.child("one-time-password").child(email.replace('.', '_')).set(data)


def verify_email_otp(email, entered_otp):
    """Check if the entered OTP is correct and not expired."""
    try:
        record = db.child("one-time-password").child(email.replace('.', '_')).get()
        if not record.val():
            return False, "No OTP record found."

        otp_data = record.val()
        stored_otp = otp_data.get("otp")
        expiry = otp_data.get("expiry")

        if int(time.time()) > expiry:
            return False, "OTP expired. Please request a new one."

        if str(entered_otp) == stored_otp:
            # Remove OTP after successful verification
            db.child("one-time-password").child(email.replace('.', '_')).remove()
            return True, "OTP verified successfully."
        else:
            return False, "Incorrect OTP."
    except Exception as e:
        return False, f"Error verifying OTP: {e}"


def get_patient_email(ic_number):
    """Fetch patient email using their IC number."""
    try:
        patients = db.child("patients").get()
        for patient in patients.each():
            data = patient.val()
            if data.get("patient_ic") == ic_number:
                return data.get("patient_email")
        return None
    except Exception as e:
        print(f"[ERROR] Error fetching patient data: {e}")
        return None
    
def get_clinic_email(ca_id):
    """Fetch clinic email using their ca_id."""
    try:
        clinic_admins = db.child("clinic_admin").get()
        for clinic in clinic_admins.each():
            data = clinic.val()
            if data.get("ca_id") == ca_id:
                return data.get("ca_email")
        return None
    except Exception as e:
        print(f"[ERROR] Error fetching clinic data: {e}")
        return None

def get_doctor_email(user_id):
    """Fetch doctor email using their user_id."""
    try:
        doctors = db.child("doctors").get()
        for doctor in doctors.each():
            data = doctor.val()
            if data.get("user_Id") == user_id:
                return data.get("doc_email")
        return None
    except Exception as e:
        print(f"[ERROR] Error fetching doctor data: {e}")
        return None


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


# ---------------- COMBINED FLOW ----------------
def password_reset_flow():
    ic_number = input("Enter your 12-digit IC number: ").strip()

    if not ic_number.isdigit() or len(ic_number) != 12:
        print("[ERROR] Invalid IC number. It must be exactly 12 digits.")
        return

    email = get_patient_email(ic_number)
    if not email:
        print("[ERROR] No patient found with that IC number.")
        return

    print(f"[INFO] Found patient email: {email}")

    # Step 1: Send OTP
    send_email_otp(email)

    # Step 2: Verify OTP
    entered = input("Enter the OTP sent to your email: ")
    success, msg = verify_email_otp(email, entered)
    print(msg)
    if not success:
        return

    # Step 3: Send Firebase password reset email
    success, msg = send_password_reset_link(email)
    print(msg)


# ---------------- TEST DEMO ----------------
if __name__ == "__main__":
    password_reset_flow()
