from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# flask routes
@app.route("/")
def index():
  tshirts = ['cat_tshirt.png', 'lama_tshirt.png']
  return render_template("index.html", tshirts=tshirts)

@app.route("/works")
def works():
  return render_template("works.html")

@app.route("/k15t/atlassian-virtual-summit")
def atlassianVirtualSummit():
  return render_template("atlassian-virtual-summit.html")

# setting the static folder to root of the website when running in DEBUG (on local machine)
# in PROD static resources should be handled by Apache or Nginx
if app.config['DEBUG']:
    from werkzeug.middleware.shared_data import SharedDataMiddleware
    import os
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
      '/': os.path.join(os.path.dirname(__file__), '')
    })

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}