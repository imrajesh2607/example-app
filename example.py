from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum', methods=['POST'])
def sum_numbers():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
        return f'The sum of {num1} and {num2} is {result}'
    except ValueError:
        return 'Please provide valid numbers.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
