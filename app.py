from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    images = [
        url_for('static', filename='images/socialwork.jpg'),
        url_for('static', filename='images/treeplant.jpg'),
        url_for('static', filename='images/Suvidha-3.jpg')
    ]
    return render_template('about.html', images=images)

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/donors')
def donors():
    return render_template('donors.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/gallery')
def gallery():
    return render_template('events.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)