from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class UserContext:
    uid: str
    role: str                 # "patient" | "doctor" | "clinic_admin" | "super_admin"
    clinic_id: Optional[str] = None

class Session:
    current: Optional[UserContext] = None

    @classmethod
    def set(cls, uid: str, role: str, clinic_id: Optional[str] = None):
        cls.current = UserContext(uid=uid, role=role, clinic_id=clinic_id)

    @classmethod
    def clear(cls):
        cls.current = None

    @classmethod
    def is_authenticated(cls) -> bool:
        return cls.current is not None

    @classmethod
    def has_role(cls, *roles: str) -> bool:
        return cls.current is not None and cls.current.role in roles
