import re

def validateUsername(username):
  if username == "":
    return 'User is empty'
  elif not re.match("^[A-Za-z]{3,20}$", username):
    return 'User must contains between 3 and 20 alphanumeric characters'  
    
  return ''


def validatePassword(password):
  if password == "":
    return "Password is empty"
  elif not re.match("^[A-Za-z0-9]{3,20}$", password):
    return 'Password must be between 3 and 20 characters'  

  return ''

def validateRetype(element,retype):
  if len(element) > 0:
    if element != retype:
      return "Passwords do not match"
      
  return ''


def validateEmail(email):
  if email:
    if not re.match("^[A-Za-z0-9]{3,20}@[A-Za-z]+\.[a-zA-Z]+$", email):
      return "Email must be between 3 and 20 characters, must contains one '@', one '.' and no empty '  ' spaces "
  
  return ''

      #^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
      #elif not re.match("[^@]+@[^@]+\.[^@]+", email):


def main():
  user = 'gui'
  passw = '1234'
  mail = 'hd3@q.c'
  print(validateUsername(user))  
  print(validatePassword(passw))   
  print(validateRetype(passw,'1234')) 
  print(validateEmail(mail))

if __name__ == "__main__":
  main()      



 