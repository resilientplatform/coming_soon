import os

from flask import Flask, request, redirect, render_template, send_from_directory
from datetime import datetime

app = Flask(__name__)

@app.before_request
def redirect_to_https():
    if request.headers.get('X-Forwarded-Proto', 'http') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)
    
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml', mimetype='application/xml')

@app.route('/site.webmanifest')
def manifest():
    return send_from_directory('.', 'site.webmanifest')

@app.route('/')
def home():
    current_year = datetime.now().year
    return render_template('index.html', current_year=current_year)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))