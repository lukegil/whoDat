from flask import Flask, render_template, url_for, request
import control
app = Flask(__name__)


@app.route('/')
def init():

    data = {}
    data["style_url"] = url_for('static', filename='custom.css')
    
    #request data
    headers = {}
    for key,value in request.headers:
        headers[key] = value
    data["user_agent"] = control.parse_ua(headers["User-Agent"])

    data["ip"] = request.remote_addr
    data["geo"] = control.get_geo(data["ip"])
    data["api_key"] = "AIzaSyBjOQ-fEaoQTO29FSZ-kTM0A28MVCVh8RQ"

    return render_template("index.html", data = data)

if __name__ == '__main__':
    app.run(debug=True)
