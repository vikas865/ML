from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def base():
    #return 'Welcome to Home Page'
    return render_template('home.html')


@app.route('/galary')
def galary():
    #return 'Welcome to Galary Page'
    return render_template('galary.html')

@app.route('/cart')
def cart():
    return 'Welcome to Cart Page'

@app.route('/contact')
def contact():
    return 'Welcome to contact Page'

app.run(debug=True)