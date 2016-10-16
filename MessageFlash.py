from flask import Flask, redirect, url_for, render_template, request, abort, flash
# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'any random string' #it requires the secret key
@app.route('/')
def index():
    return render_template('messageflashindex.html')
@app.route('/login', methods = ['GET', 'POST'])

def login():
   error = None

   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index'))
   return render_template('messageflashlogin.html', error = error)

if __name__ == '__main__':
    app.run(host='localhost',port=5454,debug=True)