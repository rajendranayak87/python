from flask import Flask,render_template
app = Flask(__name__)
@app.route('/result1')
def marks():
    marks={'maths':50,'science':45,'kannada':90}
    return render_template('result1.html',result1=marks)


if __name__ == '__main__':
   app.run(debug = True)
app.run()