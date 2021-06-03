from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

content_security_policy = {
  'default-src': [
    '\'self\'',
  ],
}

Talisman(app, content_security_policy=content_security_policy)

@app.route('/')
def default_landing_page():
    return "response from flask"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
