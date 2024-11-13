from flask import Flask, render_template

app = Flask(__name__, 
            static_folder='../static', 
            template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')