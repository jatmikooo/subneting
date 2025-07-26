from flask import Flask, render_template, request
from subnet_calc import calculate_subnet
from werkzeug.middleware.dispatcher import DispatcherMiddleware

flask_app = Flask(__name__)  # Ini penting!

@flask_app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        cidr_input = request.form['cidr']
        result = calculate_subnet(cidr_input)
    return render_template('index.html', result=result)

# Bungkus dengan DispatcherMiddleware
app = DispatcherMiddleware(None, {
    '/subneting': flask_app
})

