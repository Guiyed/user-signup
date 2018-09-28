from flask import Flask, request, redirect, render_template, url_for
import regenValidators
#import validators



app = Flask(__name__)
app.config['DEBUG'] = True
  
confirmation = '' 

@app.route('/')
def index():
  return render_template('index.html', title='Signup Assigment | Home')

@app.route("/signup", methods = ['GET','POST'])
def signup():  
  global confirmation
  confirmation = ''

  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    retype = request.form['retypepass']
    email = request.form['email']

    usernameError = regenValidators.validateUsername(username)
    passwordError = regenValidators.validatePassword(password)
    retypeError = regenValidators.validateRetype(password,retype)
    emailError = regenValidators.validateEmail(email)


    if not usernameError and not passwordError and not retypeError and not emailError:
      confirmation = 'ok'
      return redirect('/welcome?username={0}'.format(username))
      #return redirect('/welcome?username={0}'.format(username)+'&confirmation=ok')

    else:
      return render_template('signup.html',title='Signup Assigment | Signup', username= username, email= email, usernameError= usernameError, passwordError= passwordError, retypeError= retypeError, emailError= emailError)

  else:
    return render_template('signup.html',title='Signup Assigment | Signup')
  

@app.route('/welcome', methods = ['GET'])
def submitted():    
   return render_template('welcome.html',title='Signup Assigment | Welcome',user = request.args.get('username'), submit= confirmation)


app.run()
