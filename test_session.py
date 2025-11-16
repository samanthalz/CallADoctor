from CAD.security.session import Session

# Sanity check: before login there must be NO active session.
# Critical for "fail closed" behavior on protected functions.
print("A) Authenticated?", Session.is_authenticated())      # expect: False

# Simulate login: set a single source of truth (uid, role, clinic scope).
# Other modules should read Session.current instead of passing rights ad-hoc.
Session.set(uid="demo123", role="doctor", clinic_id="clinicA")

# After login, authenticated checks should pass.
print("B) Authenticated?", Session.is_authenticated())      # expect: True

# Role check: the user should be recognized as 'doctor'.
# Used by @require_role("doctor") decorators on sensitive functions.
print("C) Has role 'doctor'?", Session.has_role("doctor"))  # expect: True

# Negative role check: user is NOT a 'patient'.
# Guards like @require_role("patient") must block this user.
print("D) Has role 'patient'?", Session.has_role("patient"))# expect: False

# Simulate logout / session timeout: clear all identity and scope.
Session.clear()

# Post-logout, the app should again "fail closed" (unauthenticated).
# Any guarded function should refuse to run without re-authentication.
print("E) Authenticated?", Session.is_authenticated())      # expect: False
