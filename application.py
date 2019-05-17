from flask import Flask, render_template, request
import tweepy
import os

app = Flask(__name__)

# Set API keys
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# Homepage template
@app.route("/")
def home():
  return render_template('index.html')

# Submit template
@app.route("/submit", methods=['GET', 'POST'])
def submit():

  # OAuth Authentication using Tweepy http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,)

  # Empty statuses list which will hold streamed tweets
  statuses = []

  # Get number entry
  number = int(request.form.get('number'))

  # Open stream listener for Twitter Streaming API http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
  class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
      super().__init__()
      # Set limit for number of tweets streamed
      self.limit = int(request.form.get('number'))

    def on_status(self, status):
      if len(statuses) < self.limit:
        if status.place is not None:
          # Only append status to list if status has a place attribute
          statuses.append(status)
      else:
        return False

    def on_error(self, status_code):
      if status_code == 420:
        # Returning False in on_data disconnects the stream
        return False

  # Get language entry
  language = str(request.form.get('lang'))
  # Create stream object
  myStreamListener = MyStreamListener()

  myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

  # Filter stream by language and bounding box
  myStream.filter(languages=[str(request.form.get('lang'))], locations=[-180,-90,180,90])

  # Create list of MapMarkers
  markers = [MapMarker(s.text, s.place.bounding_box.coordinates[0][0],
                       s.place.full_name, s.id) for s in statuses]

  return render_template('./submit.html', markers=markers, number=number, language=language)

# Custom class which defines relevant properties of the tweet status
class MapMarker(object):
  def __init__(self, text, coords, name, id):
    self.text = text
    self.coords = coords[::-1]
    self.name = name
    self.id = id


if __name__ == "__main__":
  app.run(debug=True)


