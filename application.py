from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

# flask routes
@app.route("/")
def index():
  tshirts = ['cat_tshirt.png', 'lama_tshirt.png']
  return render_template("index.html", tshirts=tshirts)

@app.route("/works")
def works():
  return render_template("works.html")

@app.route("/mac-leaflet")
def macLeaflet():
  return render_template("mac-leaflet.html")

@app.route("/k15t/atlassian-virtual-summit")
def k15tAtlassianVirtualSummit():
  return render_template("atlassian-virtual-summit.html")
  
@app.route("/k15t/team-up-forum")
def k15tTeamUpForum():
  return render_template("team-up-forum.html")

@app.route("/k15t/careers")
def k15tCareers():
  return render_template("careers.html")

@app.route("/k15t/webinar")
def k15tWebinar():
  return render_template("webinar.html")

@app.route("/k15t/support")
def k15tSupport():
  title = 'Support Engineer at K15t'
  photos = {
    'k15t_benjy.jpg': 'Benjy in the office next to my table, March 2018',
    'k15t_benjy_newoffice.jpg': 'Benjy is checking out the new office space, November 2017',
    'k15t_roman_stairs.jpg': 'Me on the stairs in the K15t office building, June 2017',
    'k15t_work_place.jpg': 'My work place, July 2015'
  }
  photos_sample = random.sample(photos.items(), 2)
  return render_template("k15t_support.html", title=title, photos_sample=photos_sample)

@app.route("/podcasts/around-design/ep1")
def podcastAroundDesignEp1():
  title = 'Graphical design for the first episode of the \u00ABPodcast Around Design\u00BB'
  return render_template("podcast_cover_ep1.html", title=title)

@app.route("/podcasts/around-design/cover")
def podcastAroundDesignCover():
  title = 'Graphical design for the \u00ABPodcast Around Design\u00BB cover'
  return render_template("podcast_cover.html", title=title)

@app.route("/catch/support-engineer")
def catchSupportEngineer():
  title = 'Support Engineer at Catch Software'
  return render_template("catch_support.html", title=title)

@app.route("/catch/consultant")
def catchImplementationConsultant():
  title = 'Implementation Consultant at Catch Software'
  return render_template("catch_consultant.html", title=title)
  
@app.route("/catch/tester")
def catchTester():
  title = 'Test Analyst at Catch Software'
  return render_template("catch_tester.html", title=title)


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