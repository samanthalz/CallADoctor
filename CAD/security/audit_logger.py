from connection import db
from datetime import datetime

def log_event(uid: str, role: str, action: str, target: str = None, meta: dict = None):
    """
    Write a minimal, privacy-conscious audit event.
    Do NOT store passwords, tokens, or full PII.
    """
    try:
        entry = {
              # Use Firebase server time for a trusted, consistent timestamp (not the local clock).
            "ts": {".sv": "timestamp"},   # server timestamp
            "uid": uid or "", # Actor identity (internal IDs only). Empty string if missing to keep schema consistent.
            "role": role or "", # Actor role (e.g., "patient", "doctor", "clinic_admin", "super_admin").
            "action": action,            # e.g., "LOGIN_SUCCESS", "VIEW_PATIENT", "UPDATE_RECORD"
            "target": target or "",      # e.g., patient_id or record_id (if allowed)
            "meta": meta or {}           # small extras (page name, counts, etc.), no sensitive data
        }
        db.child("audit_logs").push(entry)
    except Exception as e:
        # Soft-fail: never crash the UI due to logging failure
        print(f"[AUDIT] logging failed: {e}")
