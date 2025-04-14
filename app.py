import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/site.webmanifest')
def manifest():
    return send_from_directory('.', 'site.webmanifest')

@app.route('/')
def coming_soon():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
