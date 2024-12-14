from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_donation', methods=['POST'])
def submit_donation():
    name = request.form['name']
    # email = request.form['email']
    # phone = request.form['phone']
    # amount = request.form['amount']
    # message = request.form['message']
    # # Process the form data here
    return redirect(url_for('thank_you', name=name))

@app.route('/thank_you')
def thank_you():
    name = request.args.get('name')
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)