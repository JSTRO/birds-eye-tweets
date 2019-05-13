import tweepy
from flask import Flask, render_template, request
import geocoder
import osmapi

CONSUMER_KEY = 'OVu6M4pmuK3DPJSo6XE72GffF'
CONSUMER_SECRET = '8HlsYKZ4JTIx1hRlSKhJ0J1St3LI2qUsOJwyVUdVlqlgCP67K6'
ACCESS_TOKEN = '278113459-dq03DbFq0MovpkK9EkxlV4Tf889FYnozLCbGDwk0'
ACCESS_TOKEN_SECRET = 'tZPrZOhwN5PCWrfMDBwEHt60rwkbuOgMJqpcPbKL6fMcE'

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

  # keyword = request.form.get('submit')

  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,)

  statuses = []

  class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
      super().__init__()
      # self.counter = 0
      self.limit = int(request.form.get('number'))

    def on_status(self, status):
      # print("on status", status.text)
      if len(statuses) < self.limit:
        if status.place is not None:
          statuses.append(status)
      else:
        return False

    def on_error(self, status_code):
      if status_code == 420:
        #returning False in on_data disconnects the stream
        return False

  myStreamListener = MyStreamListener()

  myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

  myStream.filter(languages=[str(request.form.get('lang'))], locations=[-180,-90,180,90])

  markers = [MapMarker(s.text, s.place.bounding_box.coordinates[0][0],
                       s.place.full_name, s.id) for s in statuses]

  return render_template('./submit.html', markers=markers)


class MapMarker(object):
  def __init__(self, text, coords, name, id):
    self.text = text
    self.coords = coords[::-1]
    self.name = name
    self.id = id

if __name__ == "__main__":
  app.run(debug=True)


