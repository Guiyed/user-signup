def validateUsername(username):
  if username == "":
    return False
  if " " in username or not username.isalpha() or len(username) > 20 or len(username) < 3:
    return False  
  return True


def validatePassword(password):
  if password == "":
    return False
  if " " in password or len(password) > 20 or len(password) < 3:
    return False    
  return True

def validateRetype(element,retype):
  return element == retype


def validateEmail(email):
  if " " in email or len(email) > 20 or len(email) < 3:
    return False
  if email.count('@') != 1 or email.count('.') != 1:
    return False
  return True
