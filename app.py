from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
        # Here you can handle the form data, e.g., save it to a database or send an email
    return f"Thank you, {name}! We have received your message."
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)

    
        