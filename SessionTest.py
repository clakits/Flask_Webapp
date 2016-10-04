from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = 'any random string'

@app.route('/')
def index():
   if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout_session'>click here to log out</a></b>"

   return "You are not logged in <br><a href = '/login_session'></b>" + \
      "click here to log in</b></a>"

@app.route('/login_session', methods = ['GET', 'POST'])
def login_session():
   if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

   return '''

   <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p<<input type = submit value = Login/></p>
   </form>

   '''
@app.route('/logout_session')
def logout_session():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='localhost',port=5454,debug=True)