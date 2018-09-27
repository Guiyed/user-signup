from flask import Flask, request, redirect, render_template
import validators


app = Flask(__name__)
app.config['DEBUG'] = True
  
  
@app.route('/')
def index():
  return render_template('index.html', title='Signup Assigment | Home')

@app.route("/signup", methods = ['GET','POST'])
def signup():  

  usernameError = ''
  passwordError = ''
  retypeError = ''
  emailError = ''
  
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    retype = request.form['retypepass']
    email = request.form['email']

    if validators.validateUsername(username):
      return redirect('/signup')
    else:
      #return redirect('/form')
      #return redirect(url_for('form'))
      return redirect('/form?error="error"')
  else:
    return render_template('signup.html',title='Signup Assigment | Signup', usernameError= usernameError, passwordError= passwordError, retypeError= retypeError, emailError= emailError)

  

@app.route('/welcome', methods = ['GET'])
def submitted():      
   return render_template('welcome.html',title='Signup Assigment | Welcome',user = request.args.get('username'), submit = request.args.get('confirmation'))
        
   
"""
    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/form-submit?time={0}'.format(time))
    else:
      return render_template('signup.html', title='Signup Assigment | Home', usernameError= usernameError,
          passwordError= passwordError, retypeError= retypeError, emailError= emailError)

    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)
"""


app.run()
