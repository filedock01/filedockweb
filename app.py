from flask import redirect
from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/ios-app')
def ios_app():
    return render_template('ios_app.html')

@app.route('/android-app')
def android_app():
    return redirect("https://play.google.com/store/apps/details?id=com.ignito.filedockuser")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/.well-known/assetlinks.json')
def assetlinks():
    return send_from_directory(
        'static/.well-known',
        'assetlinks.json',
        mimetype='application/json'
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/app-ads.txt')
def app_ads():
    return send_from_directory(
        'static',
        'app-ads.txt',
        mimetype='text/plain'
    )
if __name__ == '__main__':
    app.run(debug=True)
