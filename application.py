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

@app.route("/podcasts/around-design/ep1")
def podcastAroundDesignEp1():
  title = 'Graphical design for the first episode of the \u00ABPodcast Around Design\u00BB'
  return render_template("podcast_cover_ep1.html", title=title)

@app.route("/podcasts/around-design/cover")
def podcastAroundDesignCover():
  title = 'Graphical design for the \u00ABPodcast Around Design\u00BB cover'
  return render_template("podcast_cover.html", title=title)
  

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