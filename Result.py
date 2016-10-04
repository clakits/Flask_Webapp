from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   # static render the temple
   #dict = {'phy':50,'che':60,'maths':70}
   #return render_template('result.html', result = dict)
   # the following code requires request module
    if request.method == 'POST':

if __name__ == '__main__':
   app.run(host='localhost',port=5454,debug=True)