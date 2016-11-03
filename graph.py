from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

'''
#Simple Hello World
@app.route('/')
def hello_world():
    return 'Hello World'
if __name__ == '__main__':
    app.run(debug=True)
'''
'''
# from flask import Flask, redirect, url_for, request
# redirect to new page after login.html
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods =['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name = user))
'''
'''
# using template
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)
'''
@app.route('/')
def index():
    return render_template('ds-cvs-1.html')

if __name__ == '__main__':
    app.run(host='localhost',port=5454,debug=True)