# README

Bird's Eye Tweets is a Flask app built using tweepy, a Python wrapper for the Twitter API, and Leaflet.js To run:
1. Log in to CS50 IDE 
2. Navigate to the directory in which you want to clone the project. On the command line:
3. `git clone -b cs50/2019/spring/project/implementation https://github.com/submit50/JSTRO`
4. `cd implementation`
5. `sudo pip3 install tweepy`
6. `touch config.py` and add the following lines* (replace the empty string with your key):
- `CONSUMER_KEY = ''`
- `CONSUMER_SECRET = ''`
- `ACCESS_TOKEN = ''`
- `ACCESS_TOKEN_SECRET = ''`
7. `flask run` 

The goal of this project is to visualize the location of tweets on a world map and then display them. On the home screen, there are a couple filtering options for tweet selection. First, the number of tweets to display can be chosen. Keep in mind that higher numbers and less common languages you choose, the longer it may take results to display. Languages are ordered in their order of popularity on Twitter according this site: (https://thenextweb.com/shareables/2013/12/10/61-languages-found-twitter-heres-rank-popularity/). One or multiple languages can also be selected. Finally, you can toggle between whether to show the map in street view or in satellite view. 

Clicking "Fetch Tweets" will populate tweets on the map that have coordinate data associated with them. Clicking a marker will show the city and country from which the tweet was generated, as well as its exact coordinates. It will also populate the contents of the tweet in the bottom left of the screen. From the tweet embed, you can view the timeline of the user, or you can select a different marker, and the new marker's tweet will replace the previous one.  

*To generate Twitter API access token and token secret, you must create a Twitter developer account and create an application. Please follow the instructions here: https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html