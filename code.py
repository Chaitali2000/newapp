from flask import Flask
app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    return '!!!...Welcome to my app..!!!'

app.run(port=4545, host="0.0.0.0")    
