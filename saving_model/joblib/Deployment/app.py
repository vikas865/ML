from flask import Flask

app=Flask(__name__)

@app.route('/')
def base():
    return 'Hellow World'

app.run()