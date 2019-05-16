# Design Document

Birds Eye Tweets is a Flask app that visualizes tweets on a map. Twitter's Streaming API was used to request data from Twitter in conjunction with tweepy ((http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html), a Python wrapper for the Twitter API, and Leaflet.js (https://leafletjs.com/), and Javascript library for creating interactive maps.

### application.py

2 templates in `application.py` are defined: `def home()`, which renders `index.html` (the app's home page), and `def submit()`, which contains the logic to both stream and filter tweets and render map markers.

Within `def submit()`, first, a stream listener is created. Within the instance of the stream listener class, a limit of tweets to stream is set according to a user-selected option in the "Number of Results:" dropdown menu of `index.html`. In the `on_status` method, only tweets with a "place" attribute are appended to the 'statuses' list. 

Tweets are further filtered by a user-selected language (corresponding to the language dropdown menu in `index.html`) and a location using `tweepy.Stream()`'s `filter` method. The `locations` parameter is set to [-180,-90,180,90], i.e. a latitude and longitude range covering the whole world. This is done so that only tweets with coordinate data, or a "bounding box" parameter, are streamed. The `MapMarkers()` class is then defined to create a data structure unique to the parameters required from each tweet "Status" to later generate a map marker.

### index.html

Here, a form is created with filters to customize the tweet visualization. Users can select the number of tweets to retrieve, the language of tweets, and can also togggle between "streets" and "satellite" map tile layers.

### map.js

This script displays the world map using Leaflet.js. The `setView()` method sets the default focus of the map on page load to coordinates [0, 0] with a zoom of "1" (zoomed out completely). A tile layer is then applied to the map, along with parameters specifying min and max zoom and id for the tile provider (corresponding to the "Map View" toggle in `index.html`). So that multiple layers are not added with each toggle, with each `onclick()` event, the old tile layer is first removed before the new one is added. 

### submit.html

`submit.html` extends `index.html`, so that when "Fetch Tweets" is pressed, the page maintains the same layout as `index.html`, along with some added features. First is the logic for creating map markers. The `markers` list is iterated through, and for each item in the list, the marker coordinates are passed to the `marker()` method. Both place name and coordinates are then passed to the `bindPopup()` method so that when a marker is clicked, a popup with this information appears.

Below this is the logic to display an embedded tweet when a marker is clicked. The `twttr.widgets.createTweet` function from the Twitter for Websites JavaScript library is passed the tweet's id and a theme, which then displays the embedded tweet on marker click.
