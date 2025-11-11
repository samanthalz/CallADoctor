from functools import wraps
from PyQt5.QtWidgets import QMessageBox
from .session import Session

def _deny(msg: str):
    box = QMessageBox()
    box.setWindowTitle("Access denied")
    box.setText(msg)
    box.setIcon(QMessageBox.Warning)
    box.exec()
    return None

def require_role(*allowed_roles: str):
    """Block the function unless the current session role is allowed."""
    def deco(fn):
        @wraps(fn)
        def wrap(*a, **k):
            if Session.current is None:
                return _deny("Please log in.")
            if Session.current.role not in allowed_roles:
                return _deny(f"Required role: {', '.join(allowed_roles)}")
            return fn(*a, **k)
        return wrap
    return deco

def require_self_or_assigned(get_patient_uid):
    """
    Patients: only allow access to their own patient_uid.
    Doctors/clinic_admin/super_admin: allow; the function can then verify assignment/clinic scope.
    Pass a function that extracts patient_uid from the target function's args.
    """
    def deco(fn):
        @wraps(fn)
        def wrap(*a, **k):
            if Session.current is None:
                return _deny("Please log in.")
            target_uid = get_patient_uid(*a, **k)
            if Session.current.role == "patient" and target_uid != Session.current.uid:
                return _deny("Patients can only access their own records.")
            return fn(*a, **k)
        return wrap
    return deco
