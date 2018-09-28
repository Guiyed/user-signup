def validateUsername(username):
  if username == "":
    return 'User is empty'
  elif " " in username or not username.isalpha() or len(username) > 20 or len(username) < 3:
    return 'User must contains between 3 and 20 alphanumeric characters'  
  
  return ''


def validatePassword(password):
  if password == "":
    return "Password is empty"
  elif " " in password or len(password) > 20 or len(password) < 3:
    return 'Password must be between 3 and 20 characters'    
  return ''

def validateRetype(element,retype):
  if len(element) > 0:
    if element != retype:
      return "Passwords do not match"
      
  return ''


def validateEmail(email):
  if email:
    if " " in email or len(email) > 20 or len(email) < 3:
      return "Email must be between 3 and 20 characters and cannot contains empty '  ' spaces "
    elif email.count('@') != 1 or email.count('.') != 1:
      return "Email must contains one '@' and one '.' "

  return ''