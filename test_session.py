from CAD.security.session import Session

print("A) Authenticated?", Session.is_authenticated())      # expect: False
Session.set(uid="demo123", role="doctor", clinic_id="clinicA")
print("B) Authenticated?", Session.is_authenticated())      # expect: True
print("C) Has role 'doctor'?", Session.has_role("doctor"))  # expect: True
print("D) Has role 'patient'?", Session.has_role("patient"))# expect: False
Session.clear()
print("E) Authenticated?", Session.is_authenticated())      # expect: False
