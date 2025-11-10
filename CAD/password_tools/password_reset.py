## Using email OTP (bsed on current UI)

from connection import db

import random
import time
from datetime import datetime, timedelta
import yagmail

# ---------------- EMAIL CONFIG ----------------
# create a new gmail acc for this application and replace the below 
yag = yagmail.SMTP("youremail@gmail.com", "your_app_password")


# ---------------- OTP FUNCTIONS ----------------
def send_email_otp(email):
    """Generate, send, and store OTP in Firebase."""
    otp = random.randint(1000, 9999)
    expiry_time = datetime.now() + timedelta(minutes=5)
    expiry_timestamp = int(expiry_time.timestamp())

    # # Send email
    # subject = "Your Verification OTP"
    # contents = f"Your OTP code is {otp}. It expires in 5 minutes."
    # yag.send(to=email, subject=subject, contents=contents)
    # print(f"[INFO] Sent OTP to {email}: {otp}")

    # Store OTP in Firebase under "one-time-password" node
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
            patient_data = patient.val()
            if patient_data.get("patient_ic") == ic_number:
                return patient_data.get("patient_email")
        return None
    except Exception as e:
        print(f"[ERROR] Error fetching patient data: {e}")
        return None


# ---------------- TEST DEMO ----------------
if __name__ == "__main__":
    # Step 1: Get IC number input
    ic_number = input("Enter your 12-digit IC number: ").strip()

    if not ic_number.isdigit() or len(ic_number) != 12:
        print("[ERROR] Invalid IC number. It must be exactly 12 digits.")
        exit()

    # Step 2: Fetch patient email from Firebase
    email = get_patient_email(ic_number)

    if not email:
        print("[ERROR] No patient found with that IC number.")
        exit()

    print(f"[INFO] Found patient email: {email}")

    # Step 3: Send OTP
    send_email_otp(email)

    # Step 4: Ask user for OTP
    entered = input("Enter the OTP sent to your email: ")

    # Step 5: Verify OTP
    success, msg = verify_email_otp(email, entered)
    print(msg)


    # update pw (auth)
